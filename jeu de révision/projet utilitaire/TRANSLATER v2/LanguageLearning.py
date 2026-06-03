import tkinter as tk
from tkinter import messagebox, Menu, ttk, simpledialog
import csv
import random
import webbrowser

#====================VARIABLES=========================
score = 0

#====================FONCTIONS=========================
def lire_fichier_translations():
    """ Rôle : Extraire les éléments du fichier translations.csv dans une liste de dictionnaires
        Entrées : None
        Retourne : list[dict]
    """
    fichier_csv = open("translation.csv", newline='', encoding='utf-8-sig')
    fichier = csv.reader(fichier_csv, delimiter=';')
    french_list = [] 
    english_list = []
    spanish_list = []
    german_list = []

    for ligne in fichier:
        french_list.append(ligne[0])
        english_list.append(ligne[1])
        spanish_list.append(ligne[2])
        german_list.append(ligne[3])

    return french_list, english_list, spanish_list, german_list
list_fra,list_ang,list_esp,list_all = lire_fichier_translations()

def random_word():
    """rôle : choisir et générer le mot à réviser parmi la liste de mots disponible
       entrée : None
       sortie : dictionnaire = str
    """
    global liste_revision, liste_traduction, mot_corrige, mot_aleatoire

    if len(liste_revision) == 0:
        messagebox.showinfo('FIN', "Tu as terminé")
        fenetre_principale.quit()
    else:
        i = random.randint(1, len(liste_revision))
        mot_aleatoire = liste_revision[i-1]
        mot_corrige = liste_traduction[i-1]
        liste_revision.remove(mot_aleatoire)
        liste_traduction.remove(mot_corrige)
        print(len(liste_traduction), len(liste_revision))
        return mot_aleatoire, mot_corrige

def nouveau_mot():
    erreur.config(text='')
    mot_aleatoire, mot_corrige = random_word()
    mot.config(text=mot_aleatoire)
    print(mot_aleatoire, mot_corrige)

def revision():
    """ rôle : demander la traduction du mot à réviser et renvoyer si l'élève a bon
        Entrées : mot(str) : le mot à traduire , dictionnaire(dict) : les mots à réviser avec leur traduction
        sortie : boolean
    """
    entry_user = entry.get()
    entry_user = entry_user.lower()
    if entry_user == mot_corrige.lower(): # si la traduction est bonne on renvoie vrai
        print('Vrai')
        entry.delete(0, tk.END)
        nouveau_mot()
        compte_score(True)
        return True
    else: # sinon on renvoie faux
        print('Faux')
        erreur.config(text=f"-1 ⚠\n '{entry.get()}' n'est pas la traduction de '{mot_aleatoire}' ", fg="red")
        compte_score(False)
        return False

def compte_score(revision):
    """ rôle : prendre la fonction révision et en déduire le nombre de point à enlever ou mettre selon le résultat de cette fonction
        entrer : revision = booléen
        sortie : point = int
    """
    global score
    if revision == False:
        score = score -1
    else:
        score = score +1
    score_label.config(text=f"Score: {score}")
    return score

def skip():
    nouveau_mot()
    compte_score(False)

def menu():
    """ rôle : lancer le programme de traduction de mot en fonction des langues choisies
        Entrées : None
        sortie : None
    """
    global list_ang, list_fra, list_esp, list_ger, root, liste_revision, liste_traduction,langue_revision,langue_traduction
    langue_revision = combobox_rev.get()
    langue_traduction = combobox_trad.get()
    options.destroy()
    fenetre_principale.deiconify() # Faire apparaitre la fenetre
    if langue_revision == langue_traduction:
        fenetre_principale.destroy()
    else:
        if langue_revision == "français":
            liste_revision = list_fra
        elif langue_revision == "anglais":
            liste_revision = list_ang
        elif langue_revision == "espagnol":
            liste_revision = list_esp
        elif langue_revision == "allemand":
            liste_revision = list_all

        if langue_traduction == "français":
            liste_traduction = list_fra
        elif langue_traduction == "anglais":
            liste_traduction = list_ang
        elif langue_traduction == "espagnol":
            liste_traduction = list_esp
        elif langue_traduction == "allemand":
            liste_traduction = list_all    
        print("succes", langue_revision, langue_traduction)
        nouveau_mot()

def modes_revision():
    """ rôle : lancer les fonctions qui correspondent au mode de révision choisi
        Entrées : None
        sortie : None
    """
    # toutes les options de la fenêtre
    if mode_de_jeu.get() == "traduction de mots": # si l'utilisateur veut traduire des mots (cartes)
        # On lance toutes les fonctions nécessaires au fonctionnement d'un mode de jeu, ici on lance la fonction menu pour le choix des langues
        mode.destroy()
        options.deiconify()# afficher la fenetre
    elif mode_de_jeu.get() == "quiz": # Si l'utilisateur veut faire un quiz on lance les fonctions nécessaires à son fonctionnement
        webbrowser.open_new_tab("http://127.0.0.1:3000/Quiz/Quiz.html")
        mode.destroy()
    else: # sinon cela veut dire que l'utilisateur quitte la fenêtre
        mode.destroy()

def fin():
    global score,prenom
    prenom = simpledialog.askstring(" ", "Entrez votre prénom :")
    if prenom:
        fenetre_principale.destroy()
        afficher_score()

def afficher_score():
    global prenom, score, langue_revision, langue_traduction
    with open("score.txt", "a", encoding='utf-8') as fichier:
        fichier.write(f"Nom : {prenom}, Score : {score}, Langue de révision : {langue_revision}, Langue de traduction : {langue_traduction}\n")
    afficher_score_tkinter()

def afficher_score_tkinter():
    global prenom, score, langue_revision, langue_traduction

    fenetre_score = tk.Tk()
    fenetre_score.title("Scores")
    fenetre_score.geometry("%dx%d%+d%+d" % (600, 600, (fenetre_score.winfo_screenwidth()-600
                                                       )//2, (fenetre_score.winfo_screenheight()-600)//2))

    with open("score.txt", "r", encoding='utf-8') as fichier:
        scores = fichier.readlines()
    
    label_scores_precedents = tk.Label(fenetre_score, text="Scores précédents:\n")
    label_scores_precedents.pack()

    for score in scores:
        label_score_precedent = tk.Label(fenetre_score, text=score.strip())
        label_score_precedent.pack()

    fenetre_score.mainloop()



  
#===============CREATION DES FENETRES MODES, OPTIONS, FENETRE PRINCIPALE=====================

mode = tk.Tk()
mode.title("mode de révision ?") # titre de la fenêtre
mode.geometry("%dx%d%+d%+d" % (250, 100, (mode.winfo_screenwidth()-250)//2, (mode.winfo_screenheight()-100)//2)) # Taille et position de la mode

options = tk.Tk()
options.title("Options de révision")
options.geometry("%dx%d%+d%+d" % (280, 120, (options.winfo_screenwidth()-280)//2, (options.winfo_screenheight()-120)//2)) # Taille et position de la options

fenetre_principale = tk.Tk()
fenetre_principale.title("Language Learning")
fenetre_principale.geometry("%dx%d%+d%+d" % (350, 530, (fenetre_principale.winfo_screenwidth() - 350) // 2, (fenetre_principale.winfo_screenheight() - 530) // 2)) # Taille et position de la options

options.withdraw()# Cacher la fenetre
fenetre_principale.withdraw()# Cacher la fenetre

#----------------CREATION DE L'AFFICHAGE DE LA FENETRE MODE---------------

label = tk.Label(mode, text="Choisir un mode de révision") # indique à l'utilisateur ce qu'il peut choisir (ici un mode de jeu)
label.pack()
 
mode_de_jeu = ttk.Combobox(mode, values=["traduction de mots", "quiz"]) # Nom des options
mode_de_jeu.current(0)
mode_de_jeu.pack()
 
bouton_ok = tk.Button(mode, text='OK', command=modes_revision) # le bouton ok pour valider un choix
bouton_ok.pack()

#----------------CREATION DE L'AFFICHAGE DE LA FENETRE OPTION---------------

label_rev = tk.Label(options, text="Choisir une option")
label_rev.pack()

# Menu déroulant pour la langue de revision
combobox_rev = ttk.Combobox(options, values=["français", "anglais", "espagnol", "allemand"])
combobox_rev.current(0)
combobox_rev.pack()

vers = tk.Label(options, text="vers")
vers.pack()

# Menu déroulant pour la langue de traduction
combobox_trad = ttk.Combobox(options, values=["anglais","français" , "espagnol", "allemand"])
combobox_trad.current(0)
combobox_trad.pack()

combobox_traduction = combobox_trad.get()
combobox_revision = combobox_rev.get()

bouton_ok = tk.Button(options, text='OK', command=menu)
bouton_ok.pack()

#----------------CREATION DE L'AFFICHAGE DE LA FENETRE PRINCIPALE---------------

mot = tk.Label(fenetre_principale, text="", font=("Arial", 25))
mot.pack(side=tk.TOP, pady=30)

label = tk.Label(fenetre_principale, text="", font=("Calibri", 25))
label.pack(side=tk.TOP, pady=20)

score_label = tk.Label(fenetre_principale, text=f"Score: {score}", font=("Arial", 12))
score_label.pack(side=tk.TOP, padx=10, pady=10)

skip_button = tk.Button(fenetre_principale, text="Skip", command=skip, font=("Arial", 12))
skip_button.pack(side=tk.BOTTOM, pady=10)

end_button = tk.Button(fenetre_principale, text="Terminer", command=fin, font=("Arial", 12))
end_button.pack(side=tk.BOTTOM, pady=10)

bloc_entree = tk.Frame(fenetre_principale)
bloc_entree.pack(side=tk.BOTTOM, pady=20)

entry = tk.Entry(bloc_entree, font=("Arial", 12))
entry.pack(side=tk.LEFT)

entry_button = tk.Button(bloc_entree, text="Entrée", command=revision, font=("Arial", 12))
entry_button.pack(side=tk.LEFT, padx=10)

entry.bind("<Return>", lambda event: revision())

erreur = tk.Label(fenetre_principale, text="")
erreur.pack(side=tk.TOP, pady=20)

fenetre_principale.protocol("WM_DELETE_WINDOW", fenetre_principale.quit)

#======================================================================================

fenetre_principale.mainloop()
options.mainloop()
mode.mainloop()