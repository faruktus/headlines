import krone, derstandard, oe24
import tkinter as tk
import webbrowser
import funct

root = tk.Tk()
                                   
def print_headlines():
    global dicti
    listb.delete(0,"end")

    # get input in all variations
    mut_eingabe = [var_eingabe.get().lower(),
                   var_eingabe.get().upper(),
                   var_eingabe.get().title()]

    # join lists from all newspapers and fill Listbox
    for x in mut_eingabe:
        col_list = krone.get_list(x) +\
                   derstandard.get_list(x) +\
                   oe24.get_list(x)
        
        for x in col_list:
            listb.insert("end", x[1])

    # create dictionary: {Number: [[url], [headline]]}
    dicti = {}
    for index, x in enumerate(col_list):
        dicti[index+1] = x

def follow_url():
    try:
        position=(listb.curselection()[0]+1)
        url = dicti[position][0]
        webbrowser.open(url)
    except:
        return

# create Entrybox
var_eingabe = tk.StringVar()
eingabe = tk.Entry(root, textvariable=var_eingabe).grid(row=1, column=1)

# create Listbox with scrollbar
listb = tk.Listbox(root, width=100, height=30)
listb.grid(row=2, column=1, columnspan=5)
funct.get_scroll(root, listb, 2, 5)

# create Buttons <headlines>, <url>
btn_headlines = tk.Button(root, text="duawos", command=print_headlines)
btn_headlines.grid(row=1, column=2)

btn_url = tk.Button(root, text="urli", command=follow_url)
btn_url.grid(row=1, column=3)

root.mainloop()
