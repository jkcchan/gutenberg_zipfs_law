from BeautifulSoup import BeautifulSoup
import urllib2
import random

LANGUAGES = ["zh", "da", "nl", "en", "eo", "fi", "fr", "de", "el", "hu", "it", "la", "pt", "es", "sv", "tl"]

lan_to_id = {}

for language in LANGUAGES:
    html_page = urllib2.urlopen("""https://www.gutenberg.org/browse/languages/""" + language)
    soup = BeautifulSoup(html_page)
    links = soup.findAll('li')
    print(str(len(links)) + " books in language " + language)
    lan_to_id[language] = []
    for link in links:
        id = link.a.get('href')[link.a.get('href').rfind('/') + 1:]
        lan_to_id[language].append(id)

for lang, ids in lan_to_id.items():
    random.shuffle(ids)
    with open(lang, 'w') as file:
        for id in lan_to_id[lang]:
            file.write(id + '\n')
