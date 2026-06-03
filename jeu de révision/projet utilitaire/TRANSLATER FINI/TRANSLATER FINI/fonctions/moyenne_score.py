# Créé par leou.miltgen, le 07/11/2024 en Python 3.7
score = 36
def moyenne_progression(liste_traduction):
    """rôle : enregistrer dans un dossier csv le score et un nom pour l'utilisateur
        entrer : globale_score = int
        sortie : none
    """

    moy = 252 - len(liste_traduction)                                   #calcule le nombre de question répondu
    moyenne = (((score*10)/moy)*2)                                      #défini le score sur 20 de la personne
    donnees = list()
    name = str(input("entrer un nom d'utilisateur"))               #demande un nom pour reconnaitre à qui appartient le score
    donnees.append([moyenne,name])
##    print(donnees)
    Enre_fichier(fichier,donnees,bouton_ok) # ou Enre_fichier(fichier,donnees[:10],bouton_ok)

##Ouverture du fichier csv en mode lecture
def lecture_fichier(nomfichier):
    tab=[]
    fichier=open(nomfichier,"tableau_score")
    contenu=csv.reader(fichier,delimiter=";")
    for row in contenu:
        print(row)
        tab.append(row)
    fichier.close()
    return tab

##Ouverture du fichier csv en mode écriture
def Enre_fichier(nomfichier,donnees,bouton):
    global tableau

    # ouverture du fichier
    fichier=open(nomfichier,"w",newline='')
    spamwriter = csv.writer(fichier, delimiter=';')
    # Préparation des nouveaux meilleurs
    tableau.delete(*tableau.get_children())
    for i in range(len(donnees)):
        tableau.insert("", "end", i, text=i+1, values=(donnees[i][0],donnees[i][1]))
        spamwriter.writerow(donnees[i]) # Ecriture dans le fichier
    fichier.close()
    # Affichage des nouveaux meilleurs
    tableau.place(height=240, width=580, x=10, y =105)
    bouton.config(state=DISABLED,bg='SystemButtonFace',disabledforeground='grey')
    return


moyenne_progression()