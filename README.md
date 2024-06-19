# WScrapy

WScrapy is a web scraping tool designed to extract data from websites and save it in various formats. This project is designed for scraping information from websites and saving the data to a CSV file. It includes functionalities to scrape various types of data such as text content, images, and more from specified URLs.


## Features

- **Scraping Data**: Scrapes information such as domain, title, headers, description, IP address, location, phone numbers, emails, etc., from specified URLs.
- **Saving Data**: Saves scraped data into a CSV file (`data.csv`) located in the `output` directory.
- **Downloading Images**: Downloads images from URLs found during scraping and stores them in the `output/images` directory.
- **Error Handling**: Logs errors encountered during scraping or image downloading to the console.


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/themufid/WScrapy.git
    cd WScrapy
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```

3. Install the required dependencies:

    ```bash
    python -m pip install -r requirements.txt
    ```

## Configuration

Modify the `config.py` file to set the OUTPUT_PATH and adjust any other parameters as needed.

## Usage

Run the application:

```bash
python run.py
```

The script will initiate the scraping process and save the data to `./output/data.csv`. Images from the scraped URLs will be downloaded to `./output/images`.