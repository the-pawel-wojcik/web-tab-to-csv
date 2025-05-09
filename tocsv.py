""" Download a table from a website and convert it to a csv. """
import argparse
import csv
import requests
from urllib.parse import urlparse

from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('website')
    args = parser.parse_args()
    url = args.website

	# Send a GET request to the website
    response = requests.get(url)

	# Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

	# Find the table on the webpage
    table = soup.find('table')

	# Extract the table data
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        row_data = [col.text.strip() for col in cols]
        data.append(row_data)

    try:
        domain = urlparse(url).netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        filename = domain + '.csv'
    except:
        filename = 'web-table.csv'

	# Write the data to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    main()
