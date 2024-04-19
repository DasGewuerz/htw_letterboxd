import requests
from bs4 import BeautifulSoup
import random
import pandas as pd



user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

# get 1000 random actors from unique actor names in letterboxd/actors.csv
# for each actor, get the nconst from imdb/actors_imdb.csv
# for each nconst, scrape the imdb page and bio for the actor
# save each html page with the actor name as the filename in the folder imdb/actor_pages/

# Function to scrape the IMDB page
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
# example url "https://www.imdb.com/name/nm0000375/" where nm0000375 is the nconst

# Get the nconst from the actors_imdb.csv file
actors_imdb = pd.read_csv('imdb/actors_imdb.csv')

# Get the unique actor names from the actors.csv file
actors = pd.read_csv('letterboxd/actors.csv')
actors = actors['name'].unique()

# Get 1000 random actors
actors = random.sample(list(actors), 10)

# Loop through the actors and scrape the IMDB page

for actor in actors:
    # Get the nconst for the actor
    nconst = actors_imdb[actors_imdb['primaryName'] == actor]['nconst'].values[0]
    
    # Construct the URL
    url = f"https://www.imdb.com/name/{nconst}/"
    bio_url = f"https://www.imdb.com/name/{nconst}/bio"

    # Scrape the IMDB page
    soup = scrape_imdb(url)
    bio_soup = scrape_imdb(bio_url)
    
    # Save the HTML content
    with open(f'imdb/actor_pages/{actor}_page.html', 'w') as file:
        file.write(str(soup))

    with open(f'imdb/actor_pages/{actor}_bio.html', 'w') as file:
        file.write(str(bio_soup))

