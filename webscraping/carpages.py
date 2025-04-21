import pandas as pd
import requests
from bs4 import BeautifulSoup

# Initialize the main URL and set up initial empty data dictionary
url = "https://www.carpages.ca/used-cars/search/"
data = {'Link': [], 'Name': [], 'Price': [], 'Color': [], 'Car_Description': [], 'Drived': []}

# Initialize counter to limit the number of pages to scrape
counter = 0
while counter <10:  # Limiting to scrape 10 pages (you can adjust as needed)
    # Send a GET request to the current page URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all car postings on the current page
    postings = soup.find_all('div', class_='t-flex t-gap-6 t-items-start t-p-6')

    # Loop through each car posting to extract data
    for post in postings:
        link = post.find('a', class_='t-flex t-items-start t-w-[130px] t-shrink-0')['href']
        full_link = 'https://www.carpages.ca/' + link
        name = post.find('h4', class_='hN').text.strip()
        price = post.find('span', class_='t-font-bold').text.strip()
        color = post.find('span', class_='t-text-sm').text.strip()
        car_description = post.find('h5', class_='hN').text.strip()
        drived_km = post.find('div', class_='t-text-gray-500').text.strip()

        # Append extracted data to the corresponding lists in the data dictionary
        data['Link'].append(full_link)
        data['Name'].append(name)
        data['Price'].append(price)
        data['Color'].append(color)
        data['Car_Description'].append(car_description)
        data['Drived'].append(drived_km)
        next_page = soup.find('a', class_='nextprev').get('href')
        print(next_page)

        response = requests.get(next_page)
        soup = BeautifulSoup(response.text, 'html.parser')
        counter += 1

    # Find the link to the next page (if available)
   ## next_page = soup.find('a', class_='nextprev')
    ##if next_page:
      ##  url = 'https://www.carpages.ca/' + next_page.get('href')  # Update the URL to the next page
    ##else:
      ##  break  # Break the loop if no next page link is found

    ##counter += 1  # Increment the counter to track the number of pages scraped

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save the DataFrame to a single CSV file
output_file = 'car_listings_2.csv'
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} car listings to {output_file}")
