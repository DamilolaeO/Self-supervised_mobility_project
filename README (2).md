# Geo_FM Project

A spatial analysis project exploring origin-destination flows, Points of Interest (POI), 
and deprivation patterns across London and Leeds using Graph Neural Networks (GNN) and Gravity Models.

---

## Project Structure

```
Geo_FM_project/
├── OD_full_script.ipynb       # Origin-Destination flow analysis
├── leeds_full_script.ipynb    # Leeds-specific analysis
├── ldn_full_script.ipynb      # London-specific analysis
├── visualisation.ipynb        # Visualisations and maps
├── config.py                  # Data loading helper
├── requirements.txt           # Python dependencies
└── data/                      # ← You create this folder (see below)
```

---

##  Data Setup (Required Before Running)

The data files are too large to store on GitHub. Please follow these steps:

### Step 1 — Create a `data/` folder
Inside the project folder, create a folder called `data`.

### Step 2 — Download all 9 files and save them into the `data/` folder

| File | Download Link |
|------|--------------|
| `poi_uk.gpkg` | [Download](https://drive.google.com/file/d/1CqaIGhw-WvpavA_CQRjh3dND4EpcnwCk/view?usp=drive_link) |
| `msoa_OD_allactivity.csv.gz` | [Download](https://drive.google.com/file/d/1GehU-zF2Lt4dmNRjV_gwk5zAuOUgs5C0/view?usp=drive_link) |
| `ODWP01EW_OA.csv` | [Download](https://drive.google.com/file/d/1eKjTkw5-cwgH-fWXjy4RoUmxHEseJmay/view?usp=drive_link) |
| `PCD_OA21_LSOA21_MSOA21_LAD_MAY25_UK_LU.csv` | [Download](https://drive.google.com/file/d/1o8tZqunGsQqR_nV0QqZVh_MHtYjX6Iup/view?usp=drive_link) |
| `london_borough.xlsx` | [Download](https://docs.google.com/spreadsheets/d/1LkpjlL_4eE_Tg_QLg4519Ti_KYUbrejD/edit?usp=drive_link) |
| `LSOA_IMD2025.csv` | [Download](https://drive.google.com/file/d/1Zj5VnxAukURE139DoJQRcHFDhOcMRhau/view?usp=drive_link) |
| `new_population_data.csv` | [Download](https://drive.google.com/file/d/1LuPHDAZh-bDFWJZAwVNwo1US8cCWlFfY/view?usp=drive_link) |
| `LSOA_PopCentroids_EW_2021.csv` | [Download](https://drive.google.com/file/d/1OOICy4g8-Q-VgoR0IAW9a5I6FVsKgEl1/view?usp=drive_link) |
| `Lower_layer_Super_Output_Areas.csv` | [Download](https://drive.google.com/file/d/15L7jpKPwPXcTyRFWMcRYMEE5qBcUogzy/view?usp=drive_link) |

### Step 3 — Your `data/` folder should look like this:
```
data/
├── poi_uk.gpkg
├── msoa_OD_allactivity.csv.gz
├── ODWP01EW_OA.csv
├── PCD_OA21_LSOA21_MSOA21_LAD_MAY25_UK_LU.csv
├── london_borough.xlsx
├── LSOA_IMD2025.csv
├── new_population_data.csv
├── LSOA_PopCentroids_EW_2021.csv
└── Lower_layer_Super_Output_Areas.csv
```

---

## Installation

Install all dependencies by running this in your terminal:

```
pip install -r requirements.txt
```

---

## How to Run

Once data is downloaded, open Jupyter Notebook and run the notebooks in this order:

1. `OD_full_script.ipynb`
2. `leeds_full_script.ipynb`
3. `ldn_full_script.ipynb`
4. `visualisation.ipynb`

---

## Requirements

- Python 3.8+
- Jupyter Notebook
- See `requirements.txt` for full list of dependencies
