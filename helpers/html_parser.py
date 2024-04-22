from bs4 import BeautifulSoup
import re
from datetime import date

# Load the HTML content
with open(r'html/Aaron Stielstra_nm0993783_page.html', 'r') as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

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
        death_cause = place.find_next_sibling('span').text.strip("()")
    if 'birth_place' in place['href']:
        birth_place = place.text
print(birth_date)
print(death_date)
print(birth_place)
print(death_place)
print(death_cause)

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

print(height)
print(gender)