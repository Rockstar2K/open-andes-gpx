<div align="center">

# Open Andes GPX 🏔️📍

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Awesome Andes](https://img.shields.io/badge/Awesome-Andes%20Mountaineering-blue.svg)](https://github.com/Rockstar2K/awesome-andes-mountaineering)
[![Maintainer](https://img.shields.io/badge/Maintained%20by-Vulcano%20Expediciones-orange.svg)](https://vulcanoexpediciones.com)

**Community-driven, open-access repository of curated and cleaned GPX tracks, approach routes, high camps, and waypoints for mountaineering across the Andes.**

[Available Routes](#available-routes) • [How to Contribute](CONTRIBUTING.md) • [Route Index (JSON)](routes/index.json) • [Field Tools](https://vulcanoexpediciones.com/en/outdoor-calculators)

</div>

---

## Overview

High-altitude navigation in the Andes presents unique challenges: trackless scree fields (*acarreos*), penitente fields, extreme cold affecting battery life, and remote dirt roads requiring 4WD off-road navigation. Many online tracks are cluttered with GPS jitter, unedited rest stops, or outdated approaches.

**Open Andes GPX** provides:
- **Cleaned GPX tracks** (no jitter, no false loops, accurate elevation profiles).
- **Critical waypoints** (trailheads, 4WD roadheads, base camps, crater rims, true summits).
- **Technical metadata** (elevation gain, maximum altitude, technical difficulty grade, vehicle access requirements).
- **Machine-readable catalog** (`routes/index.json`) for open-source developers, GIS researchers, and navigation apps.

---

## Repository Structure

```text
open-andes-gpx/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── routes/
    ├── index.json                  # Machine-readable route registry
    ├── chile/
    │   └── atacama-antofagasta/    # Curated GPX tracks & waypoints
    │       ├── cerro-toco-normal.gpx
    │       ├── volcan-lascar-crater.gpx
    │       └── volcan-licancabur-normal.gpx
    └── wikiexplora/
        └── [country]/[region]/     # Raw, attributed source-track imports
```

Curated, field-verified routes and raw Wikiexplora imports are kept in separate directories. The latter are source material and have not been reviewed to Open Andes track-quality standards.

---

## Available Routes

Currently available, field-verified routes in Northern Chile / Atacama:

| Summit / Route | Max Elev. | Elevation Gain (D+) | Difficulty | Key Waypoints Included | GPX Track | Route Guide |
|---|---|---|---|---|---|---|
| **Cerro Toco**<br>*(Normal Route from ALMA Road)* | 5,604 m | +370 m | F (Easy / Scree) | • Trailhead / 4WD Parking (5,235 m)<br>• True Summit (5,604 m) | [`cerro-toco-normal.gpx`](routes/chile/atacama-antofagasta/cerro-toco-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/cerro-toco-ascent) |
| **Volcán Láscar**<br>*(Crater Rim & True Summit)* | 5,592 m | +650 m | F+ (Active Volcano) | • Trailhead / 4WD Parking (4,916 m)<br>• Active Crater Rim (5,500 m)<br>• True Summit (5,592 m) | [`volcan-lascar-crater.gpx`](routes/chile/atacama-antofagasta/volcan-lascar-crater.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/lascar-volcano-ascent) |
| **Volcán Licancabur**<br>*(Normal Route from Base Camp)* | 5,916 m | +1,320 m | PD (Steep Scree) | • Base Camp Trailhead (4,615 m)<br>• Summit & Crater Lake (5,916 m) | [`volcan-licancabur-normal.gpx`](routes/chile/atacama-antofagasta/volcan-licancabur-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/licancabur-volcano-ascent) |

### Route Details & Access Summary

- **Cerro Toco (5,604 m):**
  - **Location:** San Pedro de Atacama / Chajnantor Plateau, Chile.
  - **Access:** 4WD or high-clearance vehicle via Paso Jama international highway and ALMA observatory auxiliary road to parking at 5,235 m.
  - **Overview:** Ideal acclimatization peak and introduction to 5,000m+ terrain. Moderate scree slope with panoramic views of the ALMA array and Bolivian border.
- **Volcán Láscar (5,592 m):**
  - **Location:** San Pedro de Atacama / Talabre, Chile.
  - **Access:** 4WD required (low range recommended) via Talabre village and Laguna Lejía dirt track to trailhead at 4,916 m.
  - **Overview:** Ascent to the crater rim of the most active volcano in Northern Chile, passing sulfur fumaroles, and continuing to the true summit.
- **Volcán Licancabur (5,916 m):**
  - **Location:** Chile–Bolivia border (ascended via Laguna Blanca / Hito Cajón side).
  - **Access:** 4WD required to base camp at 4,615 m.
  - **Overview:** Sustained steep volcanic scree with over 1,300m elevation gain, reaching the ancient Inca ruins and crater lagoon at 5,916 m.

---

### 🗺️ Upcoming Routes (Roadmap)

We are actively curating and preparing tracks for additional peaks across the Andes. Contributions from certified guides and experienced mountaineers are welcome!

- **Chile (Puna & Central Andes):** Nevado Ojos del Salado (6,893 m), Nevado Tres Cruces (6,749 m), Cerro Sairecabur (5,971 m), Volcán San Pedro (6,145 m), Cerro El Plomo (5,424 m), Cerro Marmolejo (6,108 m).
- **Argentina:** Aconcagua (6,961 m), Monte Pissis (6,795 m), Cerro Mercedario (6,720 m).
- **Bolivia:** Nevado Sajama (6,542 m), Huayna Potosí (6,088 m), Illimani (6,438 m).
- **Peru:** Huascarán (6,768 m), Nevado Pisco (5,752 m), Nevado Chachani (6,057 m).

Have a cleaned track for one of these? Check out our [Contributing Guidelines](CONTRIBUTING.md) to submit a PR!

---

## 🛠️ Field Tools & Utilities

To plan your expedition using these files, explore our free open-access mountaineering calculators:

* **[GPX / KML / KMZ Track Converter](https://vulcanoexpediciones.com/en/outdoor-calculators/gpx-kml-kmz-converter)** — Convert tracks between Garmin, Suunto, Google Earth, and mobile apps.
* **[GPX Track Merger](https://vulcanoexpediciones.com/en/outdoor-calculators/gpx-merge-tracks)** — Combine multiple days or waypoints into a single expedition track.
* **[Naismith & Tobler High-Altitude Hiking Time](https://vulcanoexpediciones.com/en/outdoor-calculators/hiking-time-naismith)** — Estimate real hiking times taking into account elevation gain and hypoxia delays.
* **[Atmospheric Pressure & Oxygen Calculator](https://vulcanoexpediciones.com/en/outdoor-calculators/altitude-to-oxygen)** — Effective oxygen fraction and barometric decay up to 7,000m.

## Importing Wikiexplora GPX Routes

[Wikiexplora’s all-routes page](https://www.wikiexplora.com/Todas_las_rutas_de_Wikiexplora_en_Google_Earth) publishes a KMZ bundle for Google Earth. The importer downloads that bundle and converts its route lines into individual GPX files. It uses only Python’s standard library; no package installation or Wikiexplora login is needed.

### Run the importer

From the repository root, run:

```sh
python3 scripts/import_wikiexplora.py
```

To use a KMZ file you already downloaded, pass its path:

```sh
python3 scripts/import_wikiexplora.py /path/to/Wikiexplora.kmz
```

### What gets imported

- Tracks in Chile, Argentina, Bolivia, Peru, Colombia, and Ecuador.
- Hiking, trekking, mountaineering, and other non-cycling outdoor route tracks represented by KML `LineString` geometry.
- One GPX file for each track item, with multiple line segments retained as separate GPX track segments and elevation retained where present in the KMZ coordinates.
- Route and region names from the KMZ folders. Filenames are lowercase, hyphen-separated slugs.

Urban routes and cycling or mountain-bike tracks are skipped. Tracks from other countries are skipped. Standalone waypoint placemarks, route descriptions, timestamps, and other KML annotations are not converted.

### Files and metadata

Imported files go under `routes/wikiexplora/[country]/[region]/`. Each file contains the track name and links to both its Wikiexplora route page and the Open Andes repository. The matching `routes/index.json` entry includes the route name, country, region, GPX path, `source_url`, and `project_url`.

The importer preserves existing files rather than overwriting them. Re-running it adds routes with new paths and skips paths already in the index. It also ensures existing Wikiexplora GPX files have the Open Andes project link. It does not refresh coordinates for an already imported route if Wikiexplora changes that route under the same name; compare and review updates separately.

### Review before use

Wikiexplora tracks are raw imports, not field-verified Open Andes routes. Check the route page and GPX before navigation, especially for access, current conditions, and track accuracy. Attribution links are retained; verify the source license terms before republishing the imported data.

---

## Compatibility

GPX files in this repository use **GPX 1.1** and WGS84 coordinates. Compatibility can vary by device or app, so open a file in your intended navigation tool before relying on it in the field.

The Wikiexplora importer writes GPX 1.1 track files. It does not convert standalone waypoint placemarks or validate route accuracy.

Commonly used with:
- **Handheld GPS Devices:** Garmin (eTrex, GPSMAP, Montana, inReach), Coros, Suunto.
- **Mobile Navigation Apps:** [Gaia GPS](https://www.gaiagps.com/), [OsmAnd](https://osmand.net/), [Organic Maps](https://organicmaps.app/), [OruxMaps](https://www.oruxmaps.com/), [Wikiloc](https://www.wikiloc.com/).
- **GIS Software:** QGIS, Google Earth Pro, CalTopo / SARtopo.

---

## Contributing

We warmly welcome contributions from climbers, certified IFMGA/ANGM/AAGM guides, and expedition leaders across South America!

Please read our [Contributing Guidelines](CONTRIBUTING.md) to check our track quality standards before submitting a Pull Request.

---

## License & Attribution

All tracks and geographical datasets in this repository are published under the **[Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)**.

Curated and maintained with ❤️ by the guiding team at **[Vulcano Expediciones](https://vulcanoexpediciones.com)** — Specialist High-Altitude Guiding & Logistics in Northern Chile & the Andes.

