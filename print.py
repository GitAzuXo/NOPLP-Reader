import tkinter as tk
from random import seed, choice, randint

seed(42)

def Printtext(text, seeable):
    s = text
    if seeable == True:
        color = 'black'
    else:
        color = 'orange'
    l.config(text=s, fg=color)

root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())


globalline = 0

l = tk.Label(text='', font=("Helvetica", 60))
l.pack(expand=True)

def Screeninit(nom_fichier):
    root.bind("<space>", lambda event: readlyrics(nom_fichier, globalline))
    root.mainloop()

def readlyrics(nom_fichier, ligne):
    global globalline
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()
            fullstr = ""
            for line in lignes:
                fullstr = fullstr + line.strip() + " "
            nbmots = len(fullstr.split(" "))
            print(nbmots)
            random = randint(10, nbmots)
            if ligne < len(lignes):
                Printtext(lignes[ligne], True)
                globalline += 1
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")