from bs4 import BeautifulSoup
import re
from datetime import date
import os

def add_info(html_content,filename):
# Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # if the html is "Failed to retrieve the webpage. Status code: 404", skip it
    if "Failed to retrieve the webpage. Status code: 404" in soup.text:
        return

    # Search for the height
    height_item = soup.findAll('span', {'class': 'ipc-metadata-list-item__list-content-item'})
    actor_or_actress = soup.findAll('li', {'class': 'ipc-inline-list__item'})
    description = soup.find('script', {'type': 'application/ld+json'})
    birth_date = re.search(r'"birthDate":"[0-9]{4}-[0-9]{2}-[0-9]{2}"', description.text)
    birth_date = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}',birth_date.group(0)).group(0) if birth_date else None
    death_date = re.search(r'"deathDate":"[0-9]{4}-[0-9]{2}-[0-9]{2}"', description.text)
    death_date = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}',death_date.group(0)).group(0) if death_date else None
    places = soup.find_all('a', {'class': 'ipc-metadata-list-item__list-content-item--link'})
    birth_place = None
    death_place = None
    death_cause = None
    for place in places:
        if 'death_place' in place['href']:
            death_place = place.text
            try:
                death_cause = place.find_next_sibling('span').text.strip("()")
            except:
                death_cause = "undisclosed"
        if 'birth_place' in place['href']:
            birth_place = place.text

    # Extract the height by regexing to match "[0-9].[0-9][0-9] m"
    height = None
    for item in height_item:
        #print(item.text)
        match = re.search(r'[0-9].[0-9][0-9] m', item.text)
        if match:
            height = match.group(0)
            break

    gender = None
    for item in actor_or_actress:
        actor = re.search(r'actor', item.text, re.IGNORECASE)
        actress = re.search(r'actress', item.text, re.IGNORECASE)
        if actor:
            gender = "male"
            break
        if actress:
            gender = "female"
            break

    # add the information to the csv file by matching the nm number from the html filename
    # to the nconst number in the csv file
    # nm number can have 7 or 8 digits
    try:
        nm_number = re.search(r'_nm[0-9]{8}_', filename).group(0)
    except:
        nm_number = re.search(r'_nm[0-9]{7}_', filename).group(0)
    nm_number = nm_number[1:-1]

    with open ('imdb/actors_imdb_enriched.csv', 'r') as check_file:
        check_lines = check_file.readlines()
    for line in check_lines:
        if nm_number in line:
            return

    with open('imdb/actors_imdb.csv', 'r') as csv_file_read:
        lines = csv_file_read.readlines()
    for line in lines:
        # check if the nm number is in the line
        if nm_number in line:
            if nm_number == line.split(',')[0]:
                newline = line.strip('\n') + f',{gender},{birth_date},{death_date},"{birth_place}","{death_place}","{death_cause}",{height}'
                print(newline)
                # append the new line to the enriched csv file
                with open ('imdb/actors_imdb_enriched.csv', 'a') as file:
                    file.write(newline + '\n')
                break

# Load the HTML content
html_files = os.listdir('html')
for filename in html_files:
    if "_page" not in filename:
        continue
    with open(f'html/{filename}', 'r') as file:
        print(filename)
        html_content = file.read()
        add_info(html_content,filename)