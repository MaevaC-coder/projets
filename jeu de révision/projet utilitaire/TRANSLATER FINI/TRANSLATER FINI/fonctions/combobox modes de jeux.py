# Créé par maeva.cussonneau, le 10/10/2024 en Python 3.7

# on importe les bibliothèques nécessaire
import tkinter as tk
from tkinter import ttk

# Fonction qui lance la fenêtre pour choisir les modes de révision
def modes_revision():
    """ rôle : lancer les fonctions qui correspondent au mode de révision choisi
        Entrées : None
        sortie : None
    """
    # toutes les options de la fenêtre
    if(combobox.get() == "traduction de mots"): # si l'utilisateur veut traduire des mots (cartes)
        # On lance toutes les fonctions nécessaires au fonctionnement d'un mode de jeu, ici on lance la fonction menu pour le choix des langues
        menu()
        fenetre.destroy()

    if(combobox.get() == "quiz"): # Si l'utilisateur veut faire un quiz on lance les fonctions nécessaires à son fonctionnement
        # remplacer ce commentaire par les fonctions

        fenetre.destroy()

    else: # sinon cela veut dire que l'utilisateur quitte la fenêtre
        fenetre.destroy()

# Tous les paramètres dont la fonction modes_jeux() a besoin pour s'afficher via une fenêtre
fenetre = tk.Tk()
fenetre.title("mode de révision ?") # titre de la fenêtre
fenetre.geometry("%dx%d%+d%+d" % (250,100,(fenetre.winfo_screenwidth()-250)//2,(fenetre.winfo_screenheight()-100)//2)) # Taille et position de la fenetre
label = tk.Label(fenetre,text = "Choisir un mode de révision") # indique à l'utilisateur ce qu'il peut choisir (ici un mode de jeu)
label.pack()
combobox = ttk.Combobox(fenetre, values=["Quitter", "traduction de mots", "quiz"]) # Nom des options
combobox.current(0)
combobox.pack()
bouton_ok = tk.Button(fenetre, text='OK', command=modes_revision) # le bouton ok pour valider un choix
bouton_ok.pack()

fenetre.mainloop()



