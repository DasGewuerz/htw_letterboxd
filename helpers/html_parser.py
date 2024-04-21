from bs4 import BeautifulSoup
import re

# Load the HTML content
with open('html/Adam Driver_nm3485845_page.html', 'r') as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Search for the height
height_item = soup.findAll('span', {'class': 'ipc-metadata-list-item__list-content-item'})
actor_or_actress = soup.findAll('li', {'class': 'ipc-inline-list__item'})
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