
from .config import OUTPUT_PATH, OUTPUT_FORMAT
import shutil
import os

def download_results():
    if OUTPUT_FORMAT == "csv":
        file_path = os.path.join(OUTPUT_PATH, "data.csv")
    elif OUTPUT_FORMAT == "json":
        file_path = os.path.join(OUTPUT_PATH, "data.json")
    if os.path.exists(file_path):
        destination_path = os.path.join(os.getcwd(), os.path.basename(file_path))
        shutil.copy(file_path, destination_path)
        print(f"File downloaded to: {destination_path}")
    else:
        print("No file found to download.")
