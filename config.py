import os
import gdown
import urllib.request
import geopandas as gpd
import pandas as pd


#  All 9 data file download links

DATA_SOURCES = {
    "poi_uk":           "https://drive.google.com/uc?export=download&id=1CqaIGhw-WvpavA_CQRjh3dND4EpcnwCk",
    "locomizer_OD":     "https://drive.google.com/uc?export=download&id=1GehU-zF2Lt4dmNRjV_gwk5zAuOUgs5C0",
    "flows":            "https://drive.google.com/uc?export=download&id=1eKjTkw5-cwgH-fWXjy4RoUmxHEseJmay",
    "lookup_lsoa":      "https://drive.google.com/uc?export=download&id=1o8tZqunGsQqR_nV0QqZVh_MHtYjX6Iup",
    "london_list":      "https://drive.google.com/uc?export=download&id=1LkpjlL_4eE_Tg_QLg4519Ti_KYUbrejD",
    "imd_data":         "https://drive.google.com/uc?export=download&id=1Zj5VnxAukURE139DoJQRcHFDhOcMRhau",
    "pop_data":         "https://drive.google.com/uc?export=download&id=1LuPHDAZh-bDFWJZAwVNwo1US8cCWlFfY",
    "lsoa_centroids":   "https://drive.google.com/uc?export=download&id=1OOICy4g8-Q-VgoR0IAW9a5I6FVsKgEl1",
    "LSOA_df":          "https://drive.google.com/uc?export=download&id=15L7jpKPwPXcTyRFWMcRYMEE5qBcUogzy",
}


#  These files are too large for direct download
#  using gdown 

LARGE_FILES = {"flows", "lookup_lsoa", "locomizer_OD"}


#  Local cache folder (ignored by git)

DATA_DIR = "data"


def load(key, **kwargs):
    """
    Download a file from Google Drive the first time,
    cache it locally, and return a DataFrame or GeoDataFrame.

    Usage:
        from config import load
        df  = load("flows")
        gdf = load("poi_uk")
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    ext_map = {
        "poi_uk":       ".gpkg",
        "locomizer_OD": ".csv.gz",
        "london_list":  ".xlsx",
    }
    ext = ext_map.get(key, ".csv")
    local_path = os.path.join(DATA_DIR, f"{key}{ext}")

    if not os.path.exists(local_path):
        print(f"Downloading {key}...")
        if key in LARGE_FILES:
            gdown.download(DATA_SOURCES[key], local_path, fuzzy=True)
        else:
            urllib.request.urlretrieve(DATA_SOURCES[key], local_path)
        print(f"✅ Saved to {local_path}")
    else:
        print(f"✅ Loading {key} from cache")

    if ext == ".gpkg":
        return gpd.read_file(local_path, **kwargs)
    elif ext == ".xlsx":
        return pd.read_excel(local_path, **kwargs)
    else:
        return pd.read_csv(local_path, **kwargs)