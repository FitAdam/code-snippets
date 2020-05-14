import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

selected_lines = soup.select("p")


for elem in selected_lines:
    print(elem.text)
