from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import funct

def get_list(term):
    bsObj = funct.get_beauty("https://kurier.at/sitemaps_google_news.xml")
    headlines = bsObj.findAll("news:title")
    head_url = bsObj.findAll("loc")

    mo = re.compile(f"(?i){term}")
    liste=[]
    for url, head in zip(head_url, headlines):
        matches = mo.search(head.get_text())
        if matches:
            liste.append([url.get_text(), "Kurier - " + head.get_text()])

    liste2=[]
    for x in liste:
        if x not in liste2:
            liste2.append(x)

    return liste2
