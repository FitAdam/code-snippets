
"""Exercise 17 
Use the BeautifulSoup and requests Python packages to
 print out a list of all the article titles on the New York Times homepage."""

import requests
from bs4 import BeautifulSoup

r_html = requests.get('https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html')
r_html = r_html.text
soup = BeautifulSoup(r_html, "html.parser")
#print(soup.prettify())

for link in soup.find_all("a"):

    if len(link.text) > 50:
        print(link.text)

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.head)