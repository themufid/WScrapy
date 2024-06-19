import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import re
import socket
import os
from .storage import save_data, save_image
from .config import OUTPUT_PATH

visited_urls = set()  

start_url = "https://www.almufid.tech"  

def extract_data(url):
    try:
        crawl(url)
    except Exception as e:
        print(f"Terjadi kesalahan saat crawling: {e}")

def crawl(url):
    global visited_urls
    if url in visited_urls:
        return
    visited_urls.add(url)

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        extract_page_data(url, soup)
        extract_images(url, soup)  
       
        links = soup.find_all('a', href=True)
        for link in links:
            next_url = urljoin(url, link['href'])
            if is_valid_url(next_url):
                crawl(next_url)
    else:
        print(f"Gagal mengambil halaman {url}. Status code: {response.status_code}")

def extract_page_data(url, soup):
    domain = get_domain(url)
    location = get_location(soup)
    phone_numbers = get_phone_numbers(soup)
    emails = get_emails(soup)
    title = get_title(soup)
    headers = get_headers(soup)
    description = get_description(soup)
    ip_address = get_ip_address(domain)

    data = {
        'Domain': domain,
        'URL': url,
        'Location': location,
        'Phone Numbers': phone_numbers,
        'Emails': emails,
        'Title': title,
        'Headers': headers,
        'Description': description,
        'IP Address': ip_address
    }

    save_data(data)
def extract_images(url, soup):
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_url = urljoin(url, img_tag['src'])
        save_image(img_url)
        
def is_valid_url(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc) and parsed_url.netloc == urlparse(start_url).netloc

def get_domain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return domain

def get_location(soup):
    location = "Lokasi tidak ada di halaman web"
    address_pattern = re.compile(r'[\d]{1,3}\s[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+,\s[a-zA-Z]+\s[\d]{5}')
    match = soup.find(string=address_pattern)
    if match:
        location = match.strip()
    return location

def get_phone_numbers(soup):
    phone_numbers = []
    phone_pattern = re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')
    for string in soup.stripped_strings:
        match = phone_pattern.search(string)
        if match:
            phone_numbers.append(match.group())
    if not phone_numbers:
        phone_numbers = ["Nomor Telepon tidak ada di halaman web"]
    return phone_numbers

def get_emails(soup):
    emails = []
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    for string in soup.stripped_strings:
        match = email_pattern.search(string)
        if match:
            emails.append(match.group())
    if not emails:
        emails = ["Email tidak ada di halaman web"]
    return emails

def get_title(soup):
    try:
        title = soup.title.text.strip()
    except AttributeError:
        title = "Judul Halaman tidak ada di halaman web"
    return title

def get_headers(soup):
    headers = []
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        headers.append(heading.text.strip())
    return headers

def get_description(soup):
    try:
        description = soup.find('meta', {'name': 'description'})['content']
    except TypeError:
        description = "Deskripsi Halaman tidak ada di halaman web"
    return description

def get_ip_address(url):
    domain = get_domain(url)
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        ip_address = "Tidak dapat mengambil IP (Tidak tersedia)"
    return ip_address

# Menjalankan scraping
if __name__ == "__main__":
    extract_data(start_url)
