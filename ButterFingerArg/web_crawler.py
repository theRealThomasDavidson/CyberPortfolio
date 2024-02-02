"""
This is a webcrawler that will check for links to pages with links in a page that are in the same domain, will not repeat any looks at webpages, and will record any text information that is shown in any html element.

that information is then written with a new line separated format into the OUT_FILE.
"""

import requests
from bs4 import BeautifulSoup
from unicodedata import normalize

BASE_URL = 'https://www.butterfinger.com'
FIRST_PAGE = "/"
OUT_FILE = "./phrases.txt"

base_url = BASE_URL
to_see_urls = set((FIRST_PAGE,))
seen_urls= set()
set_of_strings = set()          #if these pop up twice I don't want to count or process them twice, 
while to_see_urls:
    folder = to_see_urls.pop()
    seen_urls.add(folder)
    r = requests.get(base_url + folder)
    soup = BeautifulSoup(r.text, 'lxml')

    b = soup.find('body')
    for s in b.stripped_strings:
        set_of_strings.add(s)
    for link in soup.find_all('a'):
        link = link.get('href')
        if not (isinstance(link, (str,)) and link):
            continue
        if link[0] == "/" and link not in seen_urls:
            to_see_urls.add(link)
with open(OUT_FILE, "w+") as out_file:
    for phrase in set_of_strings:
        phrase = normalize('NFKD', phrase).encode('ascii','ignore').decode()
        out_file.write(phrase.lower() + "\n")