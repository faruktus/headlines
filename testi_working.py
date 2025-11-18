import tkinter as tk

root = tk.Tk()

#frame = tk.Frame(root)

list_box = tk.Listbox(root)
list_box.grid(row=0, column=0)

for x in [x for x in range(30)]:
    list_box.insert('end', x)

sb = tk.Scrollbar(root, orient=tk.VERTICAL)

sb.grid(row=0, column=1, sticky=tk.NS)

list_box.config(yscrollcommand=sb.set)
sb.config(command=list_box.yview)

root.mainloop()

