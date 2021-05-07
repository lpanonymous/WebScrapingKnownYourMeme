import urllib.request
datos = urllib.request.urlopen('https://knowyourmeme.com/memes/success-kid-i-hate-sandcastles').read().decode()

from bs4 import BeautifulSoup
soup =  BeautifulSoup(datos, "html.parser")
details = soup.find("div", {"class":"entry-section"})
print(details.get_text())






