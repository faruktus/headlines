from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def get_beauty(url):
    req = Request(url, headers={"User-Agent":"Mozilla/5.0"})
    html = urlopen(req).read()
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj



