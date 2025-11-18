import tkinter as tk

def get_checkbuttons(mnt, ro, col):
    global derStandard
    derStandard = tk.BooleanVar()
    std = tk.Checkbutton(mnt, text="derStandard", variable=derStandard)
    std.grid(row=ro, column=col)
    
    global Krone
    Krone = tk.BooleanVar()
    krn = tk.Checkbutton(mnt, text="Krone", variable=Krone)
    krn.grid(row=ro, column=col+1)
    
    global Oe24
    Oe24 = tk.BooleanVar()
    oe24 = tk.Checkbutton(mnt, text="Oe24", variable=Oe24)
    oe24.grid(row=ro, column=col+2)

    Oe24.set(True)
    Krone.set(True)
    derStandard.set(True)
