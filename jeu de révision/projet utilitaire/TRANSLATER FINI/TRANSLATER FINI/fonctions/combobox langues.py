# Créé par maeva.cussonneau, le 10/10/2024 en Python 3.7

# on importe les bibliothèques nécessaire
import tkinter as tk
from tkinter import ttk

# Fonction qui lance la fenêtre pour choisir les modes de révision
def menu():
    """ rôle : lancer le programme de traduction de mot en fonction des langues choisies
        Entrées : None
        sortie : None
    """
    # toutes les options de la fenêtre
    if(combobox.get() == "français vers anglais"): # si l'utilisateur demande de traduire le français en anglais
        # On lance toutes les fonctions nécessaires au fonctionnement du programme avec les listes qui correspondent
        liste_revision = liste_fra
        liste_traduction = liste_ang

    if(combobox.get() == "français vers espagnol"): # idem
        liste_revision = liste_fra
        liste_traduction = liste_esp

    if(combobox.get() == "anglais vers français"): # idem
        liste_revision = liste_ang
        liste_traduction = liste_fra

    if(combobox.get() == "anglais vers espagnol"): # idem
        liste_revision = liste_ang
        liste_traduction = liste_esp

    if(combobox.get() == "espagnol vers français"): # idem
        liste_revision = liste_esp
        liste_traduction = liste_fra

    if(combobox.get() == "espagnol vers anglais"): # idem
        liste_revision = liste_esp
        liste_traduction = liste_ang

    else: # sinon cela veut dire que l'utilisateur quitte la fenêtre
        fenetre.destroy()

# Tous les paramètres dont la fonction modes_jeux() a besoin pour s'afficher via une fenêtre
fenetre = tk.Tk()
fenetre.title("Quelle option de révision voulez vous choisir ?") # titre de la fenêtre
fenetre.geometry("%dx%d%+d%+d" % (250,100,(fenetre.winfo_screenwidth()-250)//2,(fenetre.winfo_screenheight()-100)//2)) # Taille et position de la fenetre
label = tk.Label(fenetre,text = "Choisir une option") # indique à l'utilisateur ce qu'il peut choisir (ici une option de langues à réviser)
label.pack()
combobox = ttk.Combobox(fenetre, values=["Quitter", "français vers anglais", "français vers espagnol",
"anglais vers français", "anglais vers espagnol", "espagnol vers français", "espagnol vers anglais"]) # Nom des options
combobox.current(0)
combobox.pack()
bouton_ok = tk.Button(fenetre, text='OK', command=menu) # le bouton ok pour valider un choix
bouton_ok.pack()

fenetre.mainloop()
