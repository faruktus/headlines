from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import tkinter as tk

def get_beauty(url):
    req = Request(url, headers={"User-Agent":"Mozilla/5.0"})
    html = urlopen(req).read()
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj

def get_scroll(mnt, target, ro, col):
    sb = tk.Scrollbar(mnt, orient=tk.VERTICAL)
    sb.grid(row=ro, column=col+1, sticky=tk.NS)

    target.config(yscrollcommand=sb.set)
    sb.config(command=target.yview)
 
