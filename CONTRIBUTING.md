# Contributing to Open Andes GPX 🗺️

Thank you for contributing to open mountain data! To maintain high navigation safety standards, all submitted tracks must adhere to the following quality guidelines.

---

## Track Quality Standards

1. **Datum & Format:**
   - Format: Standard **GPX 1.1**.
   - Datum: **WGS84** (EPSG:4326).
   - Coordinates must be recorded in decimal degrees.

2. **Track Cleaning (Mandatory):**
   - **Remove GPS jitter & drifts:** High-altitude cliffs, cirques, and camp resting points cause GPS signals to bounce. Please smooth or delete static cluster points.
   - **Cut rest stops & camp movements:** Tracks should show the active route from trailhead/camp to summit/waypoint, not 8 hours of tent movement.
   - **No motorized sections mixed with foot tracks:** If your file includes a 4WD vehicle approach, save it as a separate segment or file (e.g., `volcan-lascar-4wd-approach.gpx` vs `volcan-lascar-climb.gpx`).

3. **Waypoints Requirements:**
   Every route must contain at least the following waypoints:
   - `TH_...`: Trailhead / End of drivable road (with 2WD or 4WD notation).
   - `CAMP_...`: Established high camps or bivouac spots (noting if water/snow is usually available).
   - `WATER_...`: Seasonal streams, springs, or snow melt points.
   - `SUMMIT_...`: True summit coordinates with official elevation.

4. **File Naming Convention:**
   - All lowercase, hyphen-separated: `[peak-name]-[route-name].gpx`
   - Examples:
     - `cerro-el-plomo-normal.gpx`
     - `ojos-del-salado-chile-normal.gpx`
     - `huayna-potosi-french-route.gpx`

---

## Submission Process (Pull Request)

1. **Fork** this repository.
2. Place your cleaned `.gpx` file inside the appropriate regional folder:
   - `routes/[country]/[region]/[filename].gpx`
3. Add a corresponding entry in `routes/index.json` with the route metadata.
4. Update the corresponding markdown table in `README.md`.
5. Open a **Pull Request** detailing:
   - Date of track recording.
   - Current access conditions or road status.
   - Recommended vehicle type (2WD, High Clearance, 4WD Low Range).
