
# Optimized Scraper for Cigar Aficionado Data
# This script uses requests and BeautifulSoup to extract cigar data with optimizations for efficiency.

import time
import json
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Using a requests session for persistent connections
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
})

# Define base URL
base_url = 'https://www.cigaraficionado.com/ratings/1000'

# Function to get page content with error handling and retry logic
def get_page_content(url, retries=3, delay=1):
    for i in range(retries):
        try:
            response = session.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Retrying {i + 1}/{retries}...")
            time.sleep(delay)
    return None  # Returns None if all retries fail

# Function to parse cigar data from a single page
def parse_cigar_data(soup):
    data = {}
    # Parse name, score, length, gauge, strength, etc.
    data['name'] = soup.find('div', class_='col-9 col-md-10 ml-auto order-1 cigar-detail_title').h1.text if soup.find('div', class_='col-9 col-md-10 ml-auto order-1 cigar-detail_title') else None
    data['score'] = soup.find('div', class_='attributes-item_score').text if soup.find('div', class_='attributes-item_score') else None
    data['length'] = soup.find('div', class_='attributes-item pr-lg-24 pr-xl-49').strong.text if soup.find('div', class_='attributes-item pr-lg-24 pr-xl-49') else None
    data['gauge'] = soup.find('div', id='attributeRingGauge').strong.text if soup.find('div', id='attributeRingGauge') else None
    data['strength'] = soup.find('div', class_="attributes-item_strength").text if soup.find('div', class_="attributes-item_strength") else None
    return data

# Main scraping function for all cigars on the page
def scrape_cigars(base_url):
    content = get_page_content(base_url)
    if not content:
        print("Failed to retrieve main page content.")
        return pd.DataFrame()
    
    soup = BeautifulSoup(content, 'html.parser')
    cigars = []
    
    # Loop through cigar detail links
    for cigar_link in soup.select('a[href*="top25cigar"]'):
        cigar_url = cigar_link.get('href')
        cigar_content = get_page_content(cigar_url)
        if cigar_content:
            cigar_soup = BeautifulSoup(cigar_content, 'html.parser')
            cigars.append(parse_cigar_data(cigar_soup))
        time.sleep(1)  # Rate limiting
    
    # Convert list of dictionaries to DataFrame
    return pd.DataFrame(cigars)

# Run scraper and save to CSV
if __name__ == "__main__":
    cigars_df = scrape_cigars(base_url)

    # Get the current date in yyyy-mm-dd format
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f'data/cigar_data_{current_date}.csv'
    cigars_df.to_csv('cigar_data.csv', index=False)
    
    # Save the DataFrame with the date-stamped filename
    cigars_df.to_csv(filename, index=False)
    print(f"Scraping complete. Data saved to {filename}.")
