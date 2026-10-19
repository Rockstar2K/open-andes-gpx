<div align="center">

# Open Andes GPX 🏔️📍

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Awesome Andes](https://img.shields.io/badge/Awesome-Andes%20Mountaineering-blue.svg)](https://github.com/Rockstar2K/awesome-andes-mountaineering)
[![Maintainer](https://img.shields.io/badge/Maintained%20by-Vulcano%20Expediciones-orange.svg)](https://vulcanoexpediciones.com)

**Community-driven, open-access repository of curated and cleaned GPX tracks, approach routes, high camps, and waypoints for mountaineering across the Andes.**

[Explore Routes](#routes-directory) • [How to Contribute](CONTRIBUTING.md) • [Route Index (JSON)](routes/index.json) • [Outdoor Calculators](https://vulcanoexpediciones.com/en/outdoor-calculators)

</div>

---

## Overview

High-altitude navigation in the Andes presents unique challenges: trackless scree fields (*acarreos*), penitente fields, extreme cold affecting battery life, and remote dirt roads requiring 4WD off-road navigation. Many online tracks are cluttered with GPS jitter, unedited rest stops, or outdated approaches.

**Open Andes GPX** provides:
- **Cleaned GPX tracks** (no jitter, no false loops, accurate elevation profiles).
- **Critical waypoints** (trailheads, 4WD roadheads, water sources, high camps, crater rims, true summits).
- **Technical metadata** (elevation gain, maximum altitude, technical difficulty grade, seasonal conditions).
- **Machine-readable catalog** (`routes/index.json`) for open-source developers, GIS researchers, and navigation apps.

---

## Repository Structure

```text
open-andes-gpx/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── routes/
    ├── index.json                  # Complete machine-readable route registry
    ├── chile/
    │   ├── atacama-antofagasta/   # Licancabur, Láscar, Cerro Toco, Sairecabur, Pular...
    │   ├── copiapo-puna/          # Ojos del Salado, Tres Cruces, Incahuasi...
    │   └── central-andes/         # Cerro El Plomo, Marmolejo, San José...
    ├── argentina/
    │   ├── mendoza/               # Aconcagua, Cerro Mercedario...
    │   └── puna-catamarca/        # Monte Pissis, Bonete Chico, Walter Penck...
    ├── bolivia/
    │   ├── cordillera-real/       # Huayna Potosí, Illimani, Pequeño Alpamayo...
    │   └── altiplano/             # Nevado Sajama, Acotango...
    └── peru/
        ├── cordillera-blanca/     # Huascarán, Alpamayo, Pisco...
        └── arequipa-cusco/        # Chachani, Misti, Ausangate...
```

---

## Routes Directory

### 🇨🇱 Northern Chile & Atacama Desert (Antofagasta / Calama / San Pedro)

| Summit / Route | Max Elev. | Elevation Gain (D+) | Difficulty | GPX File | Route Topo & Guide |
|---|---|---|---|---|---|
| **Cerro Toco** (Normal Route) | 5,604 m | +350 m | F (Easy / Scree) | [`cerro-toco-normal.gpx`](routes/chile/atacama-antofagasta/cerro-toco-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/cerro-toco-ascent) |
| **Volcán Láscar** (Crater Rim) | 5,592 m | +650 m | F (Active Volcano) | [`volcan-lascar-crater.gpx`](routes/chile/atacama-antofagasta/volcan-lascar-crater.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/lascar-volcano-ascent) |
| **Volcán Licancabur** (Normal) | 5,920 m | +1,320 m | PD (Steep Scree) | [`volcan-licancabur-normal.gpx`](routes/chile/atacama-antofagasta/volcan-licancabur-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/licancabur-volcano-ascent) |
| **Cerro Sairecabur** (Mine Route) | 5,971 m | +550 m | PD- (High Exposure) | [`cerro-sairecabur-normal.gpx`](routes/chile/atacama-antofagasta/cerro-sairecabur-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/sairecabur-volcano-ascent) |
| **Cerro Jorquencal** (Acclimatization) | 4,990 m | +420 m | F (Trekking) | [`cerro-jorquencal-normal.gpx`](routes/chile/atacama-antofagasta/cerro-jorquencal-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/cerro-jorquencal-ascent) |
| **Cerro Corona** (Puna Ridge) | 5,291 m | +620 m | F (Desert Trek) | [`cerro-corona-normal.gpx`](routes/chile/atacama-antofagasta/cerro-corona-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/cerro-corona-ascent) |
| **Volcán Putana** (Fumaroles) | 5,890 m | +890 m | F+ (Sulfur scree) | [`volcan-putana-normal.gpx`](routes/chile/atacama-antofagasta/volcan-putana-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/putana-volcano-ascent) |
| **Volcán San Pedro** (Twin Crater) | 6,145 m | +1,450 m | PD (Sand & Scree) | [`volcan-san-pedro-normal.gpx`](routes/chile/atacama-antofagasta/volcan-san-pedro-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/san-pedro-volcano-ascent) |
| **Cerro Pular** (Remote Ridge) | 6,233 m | +1,600 m | PD (4WD Remote) | [`cerro-pular-normal.gpx`](routes/chile/atacama-antofagasta/cerro-pular-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/cerro-pular-ascent) |

### 🇨🇱 Puna de Atacama & Copiapó (The 6,000m Giants)

| Summit / Route | Max Elev. | Elevation Gain (D+) | Difficulty | GPX File | Route Topo & Guide |
|---|---|---|---|---|---|
| **Nevado Ojos del Salado** (Chilean Normal) | 6,893 m | +1,093 m (from Tejos) | AD- (Grade II Rock) | [`ojos-del-salado-chile-normal.gpx`](routes/chile/copiapo-puna/ojos-del-salado-chile-normal.gpx) | [Guide](https://vulcanoexpediciones.com/en/expeditions/ojos-del-salado-volcano-ascent) |
| **Nevado Tres Cruces Sur** | 6,749 m | +1,350 m | PD+ (Steep Snow/Scree) | [`tres-cruces-sur-normal.gpx`](routes/chile/copiapo-puna/tres-cruces-sur-normal.gpx) | [Guide](https://vulcanoexpediciones.com) |

### 🇨🇱 Central Andes (Santiago / Valparaíso)

| Summit / Route | Max Elev. | Elevation Gain (D+) | Difficulty | GPX File | Route Topo & Guide |
|---|---|---|---|---|---|
| **Cerro El Plomo** (Normal from Valle Nevado) | 5,424 m | +2,400 m | F+ (Glacier Crossing) | [`cerro-el-plomo-normal.gpx`](routes/chile/central-andes/cerro-el-plomo-normal.gpx) | [Guide](https://vulcanoexpediciones.com) |
| **Cerro Marmolejo** (Normal Route) | 6,108 m | +2,850 m | PD- (Glacier Trek) | [`cerro-marmolejo-normal.gpx`](routes/chile/central-andes/cerro-marmolejo-normal.gpx) | [Guide](https://vulcanoexpediciones.com) |

---

## 🛠️ Field Tools & Utilities

To plan your expedition using these files, explore our free open-access mountaineering calculators:

* **[GPX / KML / KMZ Track Converter](https://vulcanoexpediciones.com/en/outdoor-calculators/gpx-kml-kmz-converter)** — Convert tracks between Garmin, Suunto, Google Earth, and mobile apps.
* **[GPX Track Merger](https://vulcanoexpediciones.com/en/outdoor-calculators/gpx-merge-tracks)** — Combine multiple days or waypoints into a single expedition track.
* **[Naismith & Tobler High-Altitude Hiking Time](https://vulcanoexpediciones.com/en/outdoor-calculators/hiking-time-naismith)** — Estimate real hiking times taking into account elevation gain and hypoxia delays.
* **[Atmospheric Pressure & Oxygen Calculator](https://vulcanoexpediciones.com/en/outdoor-calculators/altitude-to-oxygen)** — Effective oxygen fraction and barometric decay up to 7,000m.

---

## Compatibility

All GPX files in this repository conform to the **GPX 1.1 schema** (`WGS84` datum) and are verified compatible with:
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
