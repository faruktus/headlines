import tkinter as tk

def get_scroll(mnt, target, ro, col):
    sb = tk.Scrollbar(mnt, orient=tk.VERTICAL)
    sb.grid(row=ro, column=col+1, sticky=tk.NS)

    target.config(yscrollcommand=sb.set)
    sb.config(command=target.yview)
