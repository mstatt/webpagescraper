# Import libraries
import requests
import uuid
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = '<URL>'
articletext = ''
# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

article_news = soup.find_all('p')

#Combine all of the paragraph tag text into a single var with a newline seperator.
for p in article_news:
	articletext = articletext + p.get_text() + '\n'
# Assign a uuid to the output text file
userUuid = uuid.uuid4()
#Output the text to a file in the scrapes folder.
with open("scrapes/"+str(userUuid)+".txt", "w") as text_file:
    text_file.write(articletext)