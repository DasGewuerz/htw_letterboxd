import requests
from bs4 import BeautifulSoup
import random

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

def scrape_imdb(url):
    # Send a request to the URL
    response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Save BeautifulSoup object
        
        return soup
    else:
        return "Failed to retrieve the webpage. Status code: " + str(response.status_code)

# URL of the IMDB page to be scraped
url = "https://www.imdb.com/name/nm0000375/"
soup_content = scrape_imdb(url)
actor_name = soup_content.find('span', class_='hero__primary-text').text
actor_height = soup_content.find('span', class_='ipc-metadata-list-item__list-content-item').text
print(actor_name)
#print(actor_height)
# save the content with the actor name
