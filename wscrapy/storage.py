import csv
from datetime import datetime
import requests
import os
from .config import OUTPUT_PATH

def save_data(data):
    output_file = os.path.join(OUTPUT_PATH, "data.csv")
    fieldnames = ['Timestamp', 'Domain', 'URL', 'Location', 'Phone Numbers', 'Emails', 'Title', 'Headers', 'Description', 'IP Address']

    try:
        with open(output_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0:
                writer.writeheader()
            data['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow(data)

        print(f"Data berhasil disimpan ke {output_file}")
    except IOError as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def save_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_name = os.path.basename(url)  
            output_folder = os.path.join(OUTPUT_PATH, "images") 
            os.makedirs(output_folder, exist_ok=True) 
            image_path = os.path.join(output_folder, image_name)
            with open(image_path, 'wb') as image_file:
                image_file.write(response.content)
            print(f"Gambar {image_name} berhasil disimpan.")
        else:
            print(f"Gagal mengambil gambar dari URL: {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan gambar dari URL: {url}. Error: {e}")