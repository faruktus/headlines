from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import tkinter as tk
import sys
import krone, derstandard, oe24, kurier, diepresse

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
 
def get_checkbuttons(mnt, ro, col):
    global derstandard_var
    global std
    derstandard_var = tk.BooleanVar()
    std = tk.Checkbutton(mnt, text="derStandard", variable=derstandard_var,
                         font=('console', 14))
    std.grid(row=ro, column=col)
    
    global krone_var
    global krn
    krone_var = tk.BooleanVar()
    krn = tk.Checkbutton(mnt, text="Krone", variable=krone_var,
                         font=('console',14))
    krn.grid(row=ro, column=col+1)
    
    global oe24_var
    global oesterreich
    oe24_var = tk.BooleanVar()
    oesterreich = tk.Checkbutton(mnt, text="Oe24", variable=oe24_var,
                                 font=('console',14))
    oesterreich.grid(row=ro, column=col+2)

    global kurier_var
    global kuri
    kurier_var = tk.BooleanVar()
    kuri = tk.Checkbutton(mnt, text="Kurier", variable=kurier_var,
                          font=('console', 14))
    kuri.grid(row=ro, column=col+3)

    global diepresse_var
    global press
    diepresse_var = tk.BooleanVar()
    press = tk.Checkbutton(mnt, text="diePresse", variable=diepresse_var,
                           font=('console', 14))
    press.grid(row=ro, column=col+4)

    oe24_var.set(True)
    krone_var.set(True)
    derstandard_var.set(True)
    kurier_var.set(True)
    diepresse_var.set(True)

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def get_cum_list(*args, eingabe):
    liste=[]
    for x in args: 
        curr_module = str_to_class(x)
        curr_list = curr_module.get_list(eingabe)
        liste += curr_list
    return liste

def get_active_checkboxes():
    var_dict = {"krone": krone_var,
                "derstandard": derstandard_var,
                "oe24": oe24_var,
                "kurier": kurier_var,
                "diepresse": diepresse_var}

    liste=[]
    for k,v in var_dict.items():
        if v.get() == True:
            liste.append(k)
    
    return liste
