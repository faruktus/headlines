import krone, derstandard, oe24, diepresse, kurier
import tkinter as tk
import webbrowser
import funct

root = tk.Tk()
root.title('')
                                   
# create Checkbuttons
funct.get_checkbuttons(root, 2, 1)

def print_headlines():
    global dicti
    listb.delete(0,"end")
    
    # get searchterm/active checkboxes  
    # fill Listbox with active checkboxes
    eingabe = var_eingabe.get()
    status_list = funct.get_active_checkboxes()
    col_list = funct.get_cum_list(*status_list, eingabe=eingabe)

    for x in col_list:
        listb.insert("end", x[1])

    # create dictionary: {Number: [[url], [headline]]}
    dicti = {}
    for index, x in enumerate(col_list):
        dicti[index+1] = x

def follow_url(event):
    try:
        position=(listb.curselection()[0]+1)
        url = dicti[position][0]
        webbrowser.open(url)
    except:
        return

# create Entrybox
var_eingabe = tk.StringVar()
eingabe = tk.Entry(root, width=40, textvariable=var_eingabe, 
                   justify='center', font=('console', 14, 'bold'))                   
eingabe.grid(row=1, column=2, columnspan=2)


# create Listbox with scrollbar
listb = tk.Listbox(root, width=100, height=30,
                   fg='#400E00', bg='#FFFEE7', font=('console', 18))
listb.bind('<Double-1>', follow_url)
listb.grid(row=3, column=1, columnspan=5)
funct.get_scroll(root, listb, 3, 5)

# create Button <headlines>
btn_headlines = tk.Button(root, text="SUCHEN", command=print_headlines, 
                          font=('console', 14, 'bold'), fg='#400E00')
btn_headlines.grid(row=1, column=4, sticky='w')

root.mainloop()
