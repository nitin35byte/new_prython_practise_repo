import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL
base_url = "https://www.carpages.ca"

# Initial URL for the first page
url = base_url + "/used-cars/search/"

# List to store all scraped data
data = {'Link': [], 'Name': [], 'Price': [], 'Color': [], 'Car_Description': [], 'Drived': []}

# Set to track visited URLs
visited_links = set()

# Loop to scrape multiple pages
counter = 0
while counter < 25:  # Limiting to scrape 10 pages (you can adjust as needed)
    # Send a GET request to the current page URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all car postings on the current page
    postings = soup.find_all('div', class_='t-flex t-gap-6 t-items-start t-p-6')

    # Loop through each car posting to extract data
    for post in postings:
        link = post.find('a', class_='t-flex t-items-start t-w-[130px] t-shrink-0')['href']
        full_link = urljoin(base_url, link)

        # Check if the URL has already been visited (to avoid duplicates)
        if full_link not in visited_links:
            name = post.find('h4', class_='hN').text.strip()
            price = post.find('span', class_='t-font-bold').text.strip()
            color = post.find('span', class_='t-text-sm').text.strip()
            car_description = post.find('h5', class_='hN').text.strip()
            drived_km = post.find('div', class_='t-text-gray-500').text.strip()

            # Append extracted data to the data dictionary
            data['Link'].append(full_link)
            data['Name'].append(name)
            data['Price'].append(price)
            data['Color'].append(color)
            data['Car_Description'].append(car_description)
            data['Drived'].append(drived_km)

            # Add the URL to the visited set
            visited_links.add(full_link)

    # Find the link to the next page (if available) and construct the absolute URL
    next_page = soup.find('a', class_='nextprev')
    if next_page:
        next_page_url = urljoin(base_url, next_page['href'])
        url = next_page_url
    else:
        break  # Break the loop if no next page link is found

    counter += 1  # Increment the counter to track the number of pages scraped

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
output_file = 'car_listing4.csv'
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} unique car listings to {output_file}")
