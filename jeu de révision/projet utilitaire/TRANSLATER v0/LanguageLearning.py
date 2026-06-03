import tkinter as tk
from tkinter import messagebox, simpledialog,Menu,ttk
import csv
import random

score = 0
#========================================================================

def lire_fichier_translations():
    """ Rôle : Extraire les éléments du fichier translations.csv dans une liste de dictionnaires
        Entrées : None
        Retourne : list[dict]
    """
    fichier_csv = open("translations.csv", newline='', encoding='iso-8859-1')
    fichier = csv.reader(fichier_csv, delimiter=';')
    french_list = [] 
    english_list = []
    for ligne in fichier:
        french_list.append(ligne[0])
        english_list.append(ligne[1])
    #print("French_list = ",french_list,"\nEnglish_list = ", english_list)
    return french_list, english_list

list_fra,list_ang = lire_fichier_translations()

def random_word():
    """rôle :choisir et générer le mot à réviser parmis la liste de mot disponible
       entrée : None
       sortie : dictionnaire = str
    """
    global list_fra, list_ang, mot_corrige, mot_aleatoire
    if len(list_fra)== 0:
        messagebox.showinfo('FIN',"Tu as terminé")
        window.quit()
    else :
        i = random.randint(1,len(list_fra))
        mot_aleatoire = list_fra[i-1]
        mot_corrige = list_ang[i-1]
        list_fra.remove(mot_aleatoire)
        list_ang.remove(mot_corrige)
        print(len(list_ang),len(list_fra))
        return mot_aleatoire, mot_corrige

def nouveau_mot():
    mot_aleatoire, mot_corrige = random_word()
    mot.config(text=mot_aleatoire)
    print(mot_aleatoire,mot_corrige)

def revision():
    """ rôle : demander la traduction du monde à réviser et renvoyer si l'élève a bon
        Entrées : mot(str) : le mot à traduire , dictionnaire(dict) : les mots à réviser avec leur traduction
        sortie : boolean
    """
    '''trad = input("Quelle est la traduction en français ? (sans faute de frappe et sans accent) : ")'''
    entry_user = entry.get()
    entry_user= entry_user.lower()
    if entry_user == mot_corrige.lower():
        print('Vrai')
        entry.delete(0, tk.END)
        nouveau_mot()
        compte_score(True)
        return True
    else:
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
#========================================================================

window = tk.Tk()
window.title("Language Learning")
window.geometry("%dx%d%+d%+d" % (350, 530, (window.winfo_screenwidth() - 350) // 2, (window.winfo_screenheight() - 530) // 2))

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Quitter", command=window.quit)
menubar.add_cascade(label="Fichier", menu=file_menu)
window.config(menu=menubar)

#========================================================================

mot = tk.Label(window, text="", font=("Arial", 25))
mot.pack(side=tk.TOP, pady=30)

label = tk.Label(window, text="", font=("Calibri", 25))
label.pack(side=tk.TOP, pady=20)

score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 12))
score_label.pack(side=tk.TOP, padx=10, pady=10)

skip_button = tk.Button(window, text="Skip", command=skip, font=("Arial", 12))
skip_button.pack(side=tk.BOTTOM, pady=10)

end_button = tk.Button(window, text="Terminer", command=window.quit, font=("Arial", 12))
end_button.pack(side=tk.BOTTOM, pady=10)


bloc_entree = tk.Frame(window)
bloc_entree.pack(side=tk.BOTTOM, pady=20)

entry = tk.Entry(bloc_entree, font=("Arial", 12))
entry.pack(side=tk.LEFT)

entry_button = tk.Button(bloc_entree, text="Entrée", command=revision, font=("Arial", 12))
entry_button.pack(side=tk.LEFT, padx=10)

entry.bind("<Return>", lambda event: revision())

erreur = tk.Label(window, text="")
erreur.pack(side=tk.TOP, pady=20)
#========================================================================

nouveau_mot()
window.protocol("WM_DELETE_WINDOW", window.quit)
window.mainloop()

# on importe les bibliothèques nécessaire

def menu():
    global list_ang, list_fra
    # toutes les options de la fenêtre
    if(combobox.get() == "français vers anglais"): # si l'utilisateur demande de traduire le français en anglais
        # On lance toutes les fonctions nécessaires au fonctionnement du programme avec les listes qui correpsondent
        liste_revision = list_fra
        liste_traduction = list_ang

    if(combobox.get() == "anglais vers français"): # idem
        liste_revision = list_ang
        liste_traduction = list_fra

    else: # sinon cela veut dire que l'utilisateur quitte la fenêtre
        fenetre.destroy()

fenetre = tk.Tk()
fenetre.title("Quelle option de révision voulez vous choisir ?")
fenetre.geometry("%dx%d%+d%+d" % (250,100,(fenetre.winfo_screenwidth()-250)//2,(fenetre.winfo_screenheight()-100)//2)) # Taille et position de la fenetre
label = tk.Label(fenetre,text = "Choisir une option")
label.pack()
combobox = ttk.Combobox(fenetre, values=["Quitter", "français vers anglais", "français vers espagnol",
"anglais vers français", "anglais vers espagnol", "espagnol vers français", "espagnol vers anglais"])
combobox.current(0)
combobox.pack()
bouton_ok = tk.Button(fenetre, text='OK', command=menu)
bouton_ok.pack()

fenetre.mainloop()