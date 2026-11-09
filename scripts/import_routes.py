#!/usr/bin/env python3
"""Import track lines from the public route bundle into the Open Andes catalog."""

import argparse
import html
import io
import json
import re
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "routes" / "index.json"
KMZ_URL = "https://www.wikiexplora.com/Wikiexplora.kmz"
SOURCE_PAGE = "https://www.wikiexplora.com/Todas_las_rutas_de_Wikiexplora_en_Google_Earth"
PROJECT_URL = "https://github.com/Rockstar2K/open-andes-gpx"
README = ROOT / "README.md"
KML = "http://www.opengis.net/kml/2.2"
GPX = "http://www.topografix.com/GPX/1/1"
COUNTRIES = {"CHILE": "Chile", "ARGENTINA": "Argentina", "BOLIVIA": "Bolivia",
             "PERÚ": "Perú", "COLOMBIA": "Colombia", "ECUADOR": "Ecuador"}
EXCLUDED = ("wikiexplora urbano", "mountain bike", "bicicleta", "ciclismo", "ciclista")
PLACEHOLDER_STEM = re.compile(r"\d+(?:-\d+)?$")
GENERIC_WORDS = {
    "acercamiento", "alternativa", "ascenso", "atajo", "auto", "camino", "circuito", "descenso",
    "dia", "final", "inicio", "parte", "path", "route", "ruta", "sendero", "track", "tramo",
    "travesia", "trek", "untitled", "variante", "vehicular",
}
FILLER_WORDS = {"a", "al", "completa", "completo", "corta", "corto", "de", "del", "desde", "el",
                "en", "la", "las", "largo", "larga", "los", "normal", "opcional", "por", "sin", "via",
                "vehicular", "y"}


def slug(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-") or "wikiexplora-route"


def label(value):
    return re.sub(r"<[^>]*>", "", html.unescape(value)).strip()


def page_url(value):
    match = re.search(r'<a\b[^>]*href=[\"\']([^\"\']+)', value, re.I)
    if not match:
        return ""
    url = urllib.parse.urljoin(KMZ_URL, match.group(1))
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    return url if host == "wikiexplora.com" or host.endswith(".wikiexplora.com") else ""


def kmz_bytes(source):
    if source.startswith(("http://", "https://")):
        request = urllib.request.Request(source, headers={"User-Agent": "Open-Andes-GPX importer"})
        with urllib.request.urlopen(request, timeout=120) as response:
            data = response.read()
    else:
        data = Path(source).read_bytes()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        return archive.read("doc.kml")


def parse_kml(data):
    declared = set(re.findall(br"xmlns:([\w.-]+)=", data))
    used = set(re.findall(br"<(?:/)?([\w.-]+):", data))
    missing = used - declared
    if missing:
        declarations = b" ".join(b'xmlns:' + prefix + b'="urn:wikiexplora:' + prefix + b'"' for prefix in missing)
        data = re.sub(br"<kml(?=\s)", b"<kml " + declarations, data, count=1)
    return ET.iterparse(io.BytesIO(data), events=("start", "end"))


def parse_coordinates(text):
    points = []
    for coordinate in text.split():
        values = coordinate.split(",")
        if len(values) < 2:
            continue
        try:
            lon, lat = float(values[0]), float(values[1])
            ele = float(values[2]) if len(values) > 2 and values[2] else None
        except ValueError:
            continue
        if -180 <= lon <= 180 and -90 <= lat <= 90:
            points.append((lat, lon, ele))
    return points


def ensure_link(parent, url, text):
    for link in parent.findall(f"{{{GPX}}}link"):
        if link.get("href") == url:
            return False
    link = ET.SubElement(parent, f"{{{GPX}}}link", {"href": url})
    ET.SubElement(link, f"{{{GPX}}}text").text = text
    ET.SubElement(link, f"{{{GPX}}}type").text = "text/html"
    return True


def ensure_project_links(path, source_url):
    tree = ET.parse(path)
    root = tree.getroot()
    metadata = root.find(f"{{{GPX}}}metadata")
    if metadata is None:
        metadata = ET.Element(f"{{{GPX}}}metadata")
        root.insert(0, metadata)
    changed = ensure_link(metadata, PROJECT_URL, "Open Andes GPX")
    track = root.find(f"{{{GPX}}}trk")
    if track is not None:
        changed |= ensure_link(track, PROJECT_URL, "Open Andes GPX")
        if source_url:
            changed |= ensure_link(track, source_url, "Original Wikiexplora route")
    if changed:
        ET.register_namespace("", GPX)
        tree.write(path, encoding="utf-8", xml_declaration=True)


def gpx_bytes(name, segments, source_url):
    root = ET.Element(f"{{{GPX}}}gpx", {"version": "1.1", "creator": "Open Andes GPX / Wikiexplora"})
    metadata = ET.SubElement(root, f"{{{GPX}}}metadata")
    ET.SubElement(metadata, f"{{{GPX}}}name").text = name
    ensure_link(metadata, source_url, "Original Wikiexplora route")
    ensure_link(metadata, PROJECT_URL, "Open Andes GPX")
    track = ET.SubElement(root, f"{{{GPX}}}trk")
    ET.SubElement(track, f"{{{GPX}}}name").text = name
    ensure_link(track, source_url, "Original Wikiexplora route")
    ensure_link(track, PROJECT_URL, "Open Andes GPX")
    for points in segments:
        if len(points) < 2:
            continue
        segment = ET.SubElement(track, f"{{{GPX}}}trkseg")
        for lat, lon, ele in points:
            point = ET.SubElement(segment, f"{{{GPX}}}trkpt", {"lat": f"{lat:.7f}", "lon": f"{lon:.7f}"})
            if ele is not None:
                ET.SubElement(point, f"{{{GPX}}}ele").text = f"{ele:g}"
    ET.register_namespace("", GPX)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def route_title(source_url):
    title = urllib.parse.unquote(urllib.parse.urlparse(source_url).path.rsplit("/", 1)[-1])
    return re.sub(r"\s+", " ", title.replace("_", " ")).strip()


def words(value):
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return set(re.findall(r"[a-z]+|\d+", normalized))


def is_generic_label(name, title):
    name_words = words(name)
    if not name_words or not (name_words & GENERIC_WORDS):
        return False
    specific_words = name_words - GENERIC_WORDS - FILLER_WORDS - {word for word in name_words if word.isdigit()}
    return not (specific_words & words(title))


def set_route_name(path, name):
    tree = ET.parse(path)
    root = tree.getroot()
    metadata = root.find(f"{{{GPX}}}metadata")
    if metadata is None:
        metadata = ET.Element(f"{{{GPX}}}metadata")
        root.insert(0, metadata)
    metadata_name = metadata.find(f"{{{GPX}}}name")
    if metadata_name is None:
        metadata_name = ET.SubElement(metadata, f"{{{GPX}}}name")
    metadata_name.text = name
    for track in root.findall(f"{{{GPX}}}trk"):
        track_name = track.find(f"{{{GPX}}}name")
        if track_name is None:
            track_name = ET.SubElement(track, f"{{{GPX}}}name")
        track_name.text = name
    ET.register_namespace("", GPX)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def apply_route_renames(existing, renames):
    targets = set()
    prepared = []
    for item, target, name in renames:
        relative = Path(item["gpx_path"])
        if target in targets or (ROOT / target).exists():
            raise FileExistsError(f"Rename target already exists: {target}")
        targets.add(target)
        prepared.append((item, relative, target, name))

    readme = README.read_text()
    for item, relative, target, name in prepared:
        source = ROOT / relative
        destination = ROOT / target
        if not source.is_file():
            raise FileNotFoundError(source)
        source.rename(destination)
        set_route_name(destination, name)
        item["id"] = slug(f"{item['country']}-{item['region']}-{target.stem}")
        item["name"] = name
        item["route"] = name
        item["gpx_path"] = target.as_posix()
        pattern = rf"\[[^\]]*\]\({re.escape(relative.as_posix())}\)"
        readme, replaced = re.subn(pattern, f"[{name}]({target.as_posix()})", readme)
        if replaced != 1:
            raise ValueError(f"Expected one README link for {relative}, found {replaced}")
    INDEX.write_text(json.dumps(existing, ensure_ascii=False, indent=2) + "\n")
    README.write_text(readme)
    return len(prepared)


def rename_placeholder_routes(existing):
    renames = []
    for item in existing:
        relative = Path(item["gpx_path"])
        stem = relative.stem
        if not PLACEHOLDER_STEM.fullmatch(stem):
            continue
        title = route_title(item.get("source_url", ""))
        if not title:
            raise ValueError(f"No route title for {relative}")
        name = f"{title} — Track {stem}"
        target = relative.with_name(f"{slug(title)}-track-{stem}.gpx")
        renames.append((item, target, name))
    return apply_route_renames(existing, renames)


def rename_generic_routes(existing):
    renames = []
    for item in existing:
        title = route_title(item.get("source_url", ""))
        if not title or not is_generic_label(item["name"], title):
            continue
        relative = Path(item["gpx_path"])
        name = f"{title} — {item['name']}"
        target = relative.with_name(f"{slug(title)}-{relative.name}")
        renames.append((item, target, name))
    return apply_route_renames(existing, renames)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default=KMZ_URL, help="KMZ URL or a downloaded .kmz file")
    parser.add_argument("--rename-placeholders", action="store_true",
                        help="replace numeric imported track names with descriptive source-route names")
    parser.add_argument("--rename-generic", action="store_true",
                        help="prefix context-free track labels with their source-route name")
    args = parser.parse_args()

    existing = json.loads(INDEX.read_text())
    if args.rename_placeholders:
        renamed = rename_placeholder_routes(existing)
        print(f"Renamed {renamed} placeholder tracks")
        return
    if args.rename_generic:
        renamed = rename_generic_routes(existing)
        print(f"Renamed {renamed} context-free tracks")
        return

    source_url = args.source if args.source.startswith(("http://", "https://")) else KMZ_URL
    for item in existing:
        if item.get("source") == "Wikiexplora":
            item["project_url"] = PROJECT_URL
            path = ROOT / item["gpx_path"]
            if path.is_file():
                ensure_project_links(path, item.get("source_url", ""))
    indexed_paths = {item["gpx_path"] for item in existing}
    created = 0
    folders, stack, seen = [], [], set()
    name_tag = f"{{{KML}}}name"
    folder_tag = f"{{{KML}}}Folder"
    placemark_tag = f"{{{KML}}}Placemark"
    for event, element in parse_kml(kmz_bytes(args.source)):
        if event == "start":
            stack.append(element)
            if element.tag == folder_tag:
                folders.append("")
            continue

        if element.tag == name_tag and len(stack) > 1 and stack[-2].tag == folder_tag:
            folders[-1] = element.text or ""
        elif element.tag == placemark_tag:
            lines = element.findall(f".//{{{KML}}}LineString/{{{KML}}}coordinates")
            segments = [parse_coordinates(line.text or "") for line in lines]
            segments = [segment for segment in segments if len(segment) > 1]
            if segments:
                parts = [label(item) for item in folders if item]
                route_link = next((url for item in reversed(folders) if (url := page_url(item))), SOURCE_PAGE)
                page_title = next((label(item) for item in reversed(folders) if page_url(item)), "")
                country = COUNTRIES.get(parts[1].upper(), "") if len(parts) > 1 else ""
                if not country or any(term in " ".join(parts).lower() for term in EXCLUDED):
                    element.clear()
                    stack.pop()
                    continue
                region = parts[2] if len(parts) > 2 else (parts[1] if len(parts) > 1 else "")
                track_name = label(element.findtext(f"{{{KML}}}name", default="")).strip()
                if (track_name.lower() in {"", "ruta", "track", "path", "ruta sin título", "sin título", "untitled"}
                        or re.fullmatch(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", track_name)):
                    track_name = page_title
                track_name = track_name or "Wikiexplora route"
                country_dir = slug(country) if country else "other"
                region_dir = slug(region) if region else "unsorted"
                base = Path("routes") / "imported" / country_dir / region_dir / f"{slug(track_name)}.gpx"
                relative = base
                suffix = 2
                while True:
                    path = relative.as_posix()
                    if path in seen:
                        relative = base.with_name(f"{base.stem}-{suffix}.gpx")
                        suffix += 1
                    elif path in indexed_paths and (ROOT / relative).exists():
                        seen.add(path)
                        relative = None
                        break
                    elif (ROOT / relative).exists():
                        relative = base.with_name(f"{base.stem}-{suffix}.gpx")
                        suffix += 1
                    else:
                        break
                if relative is None:
                    element.clear()
                    stack.pop()
                    continue
                target = ROOT / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(gpx_bytes(track_name, segments, route_link))
                existing.append({"id": slug(f"{country_dir}-{region_dir}-{relative.stem}"), "name": track_name, "country": country,
                                 "region": region, "route": track_name, "gpx_path": relative.as_posix(),
                                 "source": "Wikiexplora", "source_url": route_link, "project_url": PROJECT_URL})
                indexed_paths.add(relative.as_posix())
                seen.add(relative.as_posix())
                created += 1
            element.clear()
        elif element.tag == folder_tag:
            folders.pop()
        stack.pop()

    INDEX.write_text(json.dumps(existing, ensure_ascii=False, indent=2) + "\n")
    print(f"Imported {created} tracks into the raw route catalog (KMZ source: {args.source})")


if __name__ == "__main__":
    main()
