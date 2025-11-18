from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def get_list(term):
    html = urlopen("https://www.oe24.at/sitemap-news.xml")
    bsObj = BeautifulSoup(html, "html.parser")
    headlines = bsObj.findAll("n:title")
    head_url = bsObj.findAll("loc")

    mo = re.compile(f"(?i){term}")
    liste=[]
    for url, head in zip(head_url, headlines):
        matches = mo.search(head.get_text())
        if matches:
            liste.append([url.get_text(), "Oe24 - " + head.get_text()])
    
    liste2=[]
    for x in liste:
        if x not in liste2:
            liste2.append(x)

    return liste2
