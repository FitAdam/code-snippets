import requests
from bs4 import BeautifulSoup
import os

base_url = "https://tvn24.pl/polska/"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

selected_lines = soup.select("p")


"""for elem in selected_lines:
    print(elem.text)"""

list_with_text = []

for elem in selected_lines:
    list_with_text.append(elem.text)

list_with_text = str(list_with_text)

# Name the list of orders
file_with_text = "file_to_save.txt"
if not os.path.exists(file_with_text):
    print("\nFile file_to_save.txt does not exist!")
    with open(file_with_text, "w"):
        pass
    print("\nCreated a file in this directory named file_to_save.txt...")

# Open the file_to_save.txt file in write mode and read the lines
file_with_text = open(file_with_text, "r+")
file_with_text = file_with_text.read()
if len(file_with_text) == 0:
    print("\nThe file is empty!")

with open("file_to_save.txt", "a", encoding="utf-8") as open_file:
    for elem in selected_lines:
        open_file.write(list_with_text)

if len(file_with_text) == 0:
    print("\nThe text has been saved into the file txt in the same directory!")

