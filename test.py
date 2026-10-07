from tkinter import Tk, Label
root = Tk() # Création de la fenêtre racine
label = Label(root, text="Hello", foreground="#892222",
              background="#FFAAAA", padx="10", pady="4")
label.grid()
root.mainloop() # Lancement de la boucle principale