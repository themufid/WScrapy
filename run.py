from wscrapy.scraper import extract_data
from wscrapy.downloader import download_results

def main():
    start_url = "https://www.w3schools.com/"
    
    print(f"Memulai scraping dari: {start_url}")
    extract_data(start_url)
    download_results()
    print("Proses scraping selesai.")

if __name__ == "__main__":
    main()