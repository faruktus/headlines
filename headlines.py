import krone, derstandard, oe24

eingabe = input("Suchbegriff: ")

deimuada = krone.get_list(eingabe) +\
           derstandard.get_list(eingabe) +\
           oe24.get_list(eingabe)

dicti = {}

for index, x in enumerate(deimuada):
    dicti[index+1] = x
