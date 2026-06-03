# Démineur
from tkinter import *
from tkinter import ttk
import random, winsound, sys,csv
from timeit import default_timer
import random

def init_dicos():
    """ Description : Initialise les dictionnaires :
        dictionnaire de jeu : tab_j (variable gobale avec des chaines vides)
        dictionnaire des mines : tab_m (variable gobale avec des 0)
        Entrée : aucune
        Retour : aucun
    """
    #Initialisation de tab_j
    for i in range(1,nb_col+1): #Pour chaque colonne
        for j in range(1,nb_lig+1): #Pour chaque ligne
            tab_j[(i,j)] = '' #Chaîne de caractère vide
            tab_m[(i,j)] = 0 #Case à 0


def init_mines(nbmines):
    """ Description : Initialise le dictionnaire de mines de façon aléatoire :
        dictionnaire des mines : tab_m (variable gobale avec des 9 pour les mines)
        Entrée : nbmines : INT (Nombre de mines à placées)
        Retour : aucun
    """
    global tab_m

    liste_mines = list() #liste des positions des mines
    taille_lst_mines = len(liste_mines) #taille de la liste de la position des mines
    i,j = 0,0 #initialisation des variables de la position des mines

    while taille_lst_mines < nbmines: #tant qu'on a pas le bon nombre de mines
        #coordonnées aléatoire
        i = random.randint(1,nb_col)
        j = random.randint(1,nb_lig)
        #si les coordonnées ne sont pas déjà prises
        if (i,j) not in liste_mines:
            liste_mines.append((i,j)) #on ajoute
        taille_lst_mines = len(liste_mines) #mise à jour de la taille de la mine

    #ajout des mines dans la grille
    for k in liste_mines:
        tab_m[k] = 9


def affecter_adj(): #Maëva
    """ Description : Initialise le dictionnaire des mines avec le nombre de mines adjacente :
        dictionnaire des mines : tab_m (variable gobale)
        Entrée : aucune
        Retour : aucun
    """
    for n_col in range(1,nb_col+1):
        for n_lig in range(1,nb_lig+1): # prend une à une les coordonnées de toutes les cases de la grille
            if tab_m[(n_col, n_lig)] != 9: # vérifie que la case regardée ne contient pas de mine
                compteur = 0  # démarrage du compteur de mines adjacentes
                for col_verif in range(n_col-1,n_col+2):
                    for lig_verif in range(n_lig-1,n_lig+2): # prend une à une les coordonnées des cases adjacentes à celle regardée
                        if (col_verif,lig_verif) in tab_m.keys(): # vérifie que les coordonnées existent dans le dictionnaire de mines
                            if (col_verif,lig_verif) != (n_col,n_lig): # vérifie que les coordonnées sont différentes de la case regardée
                                if tab_m[(col_verif,lig_verif)] == 9:
                                    compteur += 1 # s'il y a une mine dans la case adjacente ajoute 1 au compteur
                tab_m[(n_col,n_lig)] = compteur # affecte à la case regardée le nombre de mines adjacentes


def modif_meilleur(fichier,donnees,tps,Nom,bouton_ok):
    """ Description : Modifie les meilleurs scores en ajoutant les données de la partie:
        Entrées : fichier : Nom du fichier à modifier ; STR
                  donnees : LIST (LIST) : Liste des meilleurs scores à modifier
                  tps : temps de la partie ; STR
                  Nom : nom du joueur ; STR
                  bouton_ok : objet  bouton de Tkinter pour la fonction Enre_fichier
        Retour : aucun
    """
    # Insérer les nouveaux scores dans la liste
    #for i in donnees:
        #temps_joueur = int(tps[:1])*60+int(tps[2:4])+int(tps[5:])/60
        #temps = int(i[0][:2])*60+int(i[0][3:5])+int(i[0][6:])/60
        #if temps_joueur<= temps:
            #indice = donnees.index(i)
            #donnees.insert(indice,[tps, Nom])


    # Limiter le classement à 10 éléments
    #donnees = donnees[:10]

    # Enregistre le fichier des meilleurs scores
    #Enre_fichier(fichier,donnees,bouton_ok)
    i=0
    longueur = len(donnees)
    fin=False
    if longueur != 0:
        while i<longueur and not fin:
            if tps>donnees[i][0]:
                i += 1
            else :
                fin = True
    if i == longueur:
        donnees.append([tps,Nom])
    else :
        donnees.insert(i,[tps,Nom])
    if len(donnees)>10:
        del donnees[-1]
    Enre_fichier(fichier,donnees,bouton_ok)

##Ouverture du fichier csv en mode lecture
def lecture_fichier(nomfichier):
    tab=[]
    fichier=open(nomfichier,"r")
    contenu=csv.reader(fichier,delimiter=";")
    for row in contenu:
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


# Dessine la grille de jeu
def grille(nb_col, nb_lignes, dim, origine):
    # Initialisation des cases
    y = 0
    while y < nb_lignes:
        x = 1
        y += 1
        while x <= nb_col:
            can.create_rectangle((x-1)*dim+gap,(y-1)*dim+gap,
                                 x*dim+gap,y*dim+gap,width=0, fill="#C6C6C6")
            x += 1
    x1= origine
    y1= origine
    # Détermine la largeur de la grille
    y2 = y1 + (dim*nb_lignes)
    # Détermine la hauteur de la grille
    x2 = x1 + (dim*nb_col)
    colonne = 0
    while colonne <= nb_col:
        colonne=colonne+1
        # Création de la ligne verticale
        can.create_line(x1,y1,x1,y2,width=1, fill="grey")
        # Décalage de la ligne vers la droite
        x1 = x1 + dim
    x1 = origine
    ligne = 0
    while ligne <= nb_lignes:
        ligne=ligne+1
        # Création de la ligne horizontale
        can.create_line(x1,y1,x2,y1,width=1, fill="black")
        # Décalage de la ligne vers le bas
        y1 = y1 + dim

# Initialise le niveau de jeu
def init_niveau():
    global nb_col, nb_lig, nb_mines
    niveau = choix.get()
    # niveau débutant
    if niveau == 1:
        nb_col, nb_lig, nb_mines = 10, 10, 12
    # niveau normal
    elif niveau == 2:
        nb_col, nb_lig, nb_mines = 15, 15, 30
    # niveau avancé
    elif niveau == 3:
        nb_col, nb_lig, nb_mines = 20, 20, 80
    # niveau expert
    else:
        nb_col, nb_lig, nb_mines = 25, 25, 120
    # taille du canevas pour chaque niveau
    can.configure(width=(nb_col*dim)+gap , height=(nb_lig*dim)+gap)
    init_jeu()

# Initialistion des paramètres du jeu
def init_jeu():
    global nb_mines_cachees, nb_cases_vues, on_joue,start
    # Initialisation des variables
    on_joue = True
    nb_cases_vues = 0
    can.delete(ALL)
    nb_mines_cachees = nb_mines
    affiche_compteurs()
    stopchrono=True
    start=0
    text_clock.configure(text='0:00:00')
    texte_fin.configure(text='')

    # Initialisation des 2 dictionnaires
    init_dicos()

    # Dessine la grille
    grille(nb_col, nb_lig, dim, gap)
    # place les mines aléatoirement dans la grille de jeu
    init_mines(nb_mines)
    # On indique le nombre de mines adjacentes dans la grille de jeu
    affecter_adj()


# calcule le nombre de mines qu'il reste à trouver
def affiche_compteurs():
    decompte_mines.configure(text=str(nb_mines_cachees))
    # Décompte des case à traiter pour la fonction gagné
    decompte_cases.configure(text=str((nb_col*nb_lig)-nb_cases_vues))

# affiche le nombre de mines restantes
def affiche_nb_mines (nb_mines_voisines, col, lig):
    global nb_mines_cachees,nb_cases_vues
    # si la case est vide
    if tab_j[col, lig] == "":
        nb_cases_vues = nb_cases_vues + 1
        # S'il y a un drapeau : modification du compteur de mines
        if (tab_j[col, lig] == "d"):
            # Ajout d'une mine
            nb_mines_cachees = nb_mines_cachees + 1
            # le drapeau est considéré comme une case vue
            nb_cases_vues = nb_cases_vues - 1
            affiche_compteurs()
        tab_j[col, lig] = nb_mines_voisines
        # Dessine un carré "blanc"
        can.create_rectangle((col-1)*dim+gap+2,(lig-1)*dim+gap+2,
                             col*dim+gap-1,lig*dim+gap-1,width=0, fill="white")
        # Affichage du nombre de mines avec les couleurs corespondantes
        coul = ['blue','orange','red','green','purple','skyblue','pink']
        can.create_text(col*dim-dim//2+gap, lig*dim-dim//2+gap,
                        text=str(nb_mines_voisines),
                        fill=coul[nb_mines_voisines-1],font=('Times', '23', 'bold'))



# Affiche toutes les cases zéro adjacentes et leur bordure
def vide_plage_zero(col, ligne):
    global nb_mines_cachees, nb_cases_vues
    # si on a déjà la cellule n'est pas vide
    if tab_j[col, ligne] != 0:
        # S'l y a un drapeau on modifie le compteur de mines et de cases traitées
        if (tab_j[col, ligne] == "d"):
            nb_mines_cachees = nb_mines_cachees + 1
            nb_cases_vues = nb_cases_vues - 1
        # Affichage du fond
        can.create_rectangle((col-1)*dim+gap+2, (ligne-1)*dim+gap+2,
                             col*dim+gap-2, ligne*dim+gap-2,
                             width=0, fill="white")
        # Stockage des 0 dans le tableau de jeu
        tab_j[col, ligne] = 0
        nb_cases_vues = nb_cases_vues + 1
        # Vérifie les cases voisines en croix
        if col > 1:
            nb_mines_voisines = tab_m[col-1, ligne]
            if nb_mines_voisines == 0:
                vide_plage_zero(col-1, ligne)
            else:
                affiche_nb_mines(nb_mines_voisines, col-1, ligne)
        if col < nb_col:
            nb_mines_voisines = tab_m[col+1, ligne]
            if nb_mines_voisines == 0:
                vide_plage_zero(col+1, ligne)
            else:
                affiche_nb_mines(nb_mines_voisines, col+1, ligne)
        if ligne > 1:
            nb_mines_voisines = tab_m[col, ligne-1]
            if nb_mines_voisines == 0:
                vide_plage_zero(col, ligne-1)
            else:
                affiche_nb_mines(nb_mines_voisines, col, ligne-1)
        if ligne < nb_lig:
            nb_mines_voisines = tab_m[col, ligne+1]
            if nb_mines_voisines == 0:
                vide_plage_zero(col, ligne+1)
            else:
                affiche_nb_mines (nb_mines_voisines, col, ligne+1)
        # Vérification des diagonales pour afficher les bords de la plage zéro
        if col > 1 and ligne > 1:
            nb_mines_voisines = tab_m[col-1, ligne-1]
            if nb_mines_voisines == 0:
                vide_plage_zero(col-1, ligne-1)
            else:
                affiche_nb_mines(nb_mines_voisines, col-1, ligne-1)
        if col > 1 and ligne < nb_lig:
            nb_mines_voisines = tab_m[col-1, ligne+1]
            if nb_mines_voisines == 0:
                vide_plage_zero(col-1, ligne+1)
            else:
                affiche_nb_mines(nb_mines_voisines, col-1, ligne+1)
        if col < nb_col and ligne > 1:
            nb_mines_voisines = tab_m[col+1, ligne-1]
            if nb_mines_voisines == 0:
                vide_plage_zero(col+1, ligne-1)
            else:
                affiche_nb_mines (nb_mines_voisines, col+1, ligne-1)
        if col < nb_col and ligne < nb_lig:
            nb_mines_voisines = tab_m[col+1, ligne+1]
            if nb_mines_voisines == 0:
                vide_plage_zero(col+1, ligne+1)
            else:
                affiche_nb_mines(nb_mines_voisines, col+1, ligne+1)
        affiche_compteurs()


def perdu():
    global on_joue,stopchrono
    stopchrono=True
    on_joue  = False
    # Parcours du tableau pour afficher toutes les mines
    nLig = 0
    while nLig < nb_lig:
        nCol = 1
        nLig = nLig +1
        while nCol <= nb_col:
            # affichage de grille exacte
            if tab_m[nCol, nLig] == 9:
                if tab_j[nCol, nLig] == "?":
                    can.create_image(nCol*dim-dim//2+gap,
                                     nLig*dim-dim//2+gap, image = im_mine)
                elif tab_j[nCol, nLig] == "":
                    can.create_image(nCol*dim-dim//2+gap,
                                     nLig*dim-dim//2+gap, image = im_mine)
            else :
                if tab_j[nCol, nLig] == "d":
                    can.create_image(nCol*dim-dim//2+gap,
                                     nLig*dim-dim//2+gap, image = im_erreur)
            nCol = nCol+1
    texte_fin.configure(text='Perdu !')
    fen.update_idletasks() # rafraichit la fenêtre avant le bruitage
    winsound.PlaySound('explosion.wav', winsound.SND_FILENAME)


def gagne():
    global stopchrono,tableau
    stopchrono=True
    texte_fin.configure(text='Bravo !')
    fen.update_idletasks()
    winsound.PlaySound('gagne.wav', winsound.SND_FILENAME)
    niveau = choix.get()
    # niveau débutant
    if niveau == 1:
        fichier='MeilleurD.csv'
    # niveau normal
    elif niveau == 2:
        fichier='MeilleurN.csv'
    # niveau avancé
    elif niveau == 3:
        fichier='MeilleurA.csv'
    # niveau expert
    else:
        fichier ='MeilleurE.csv'
    classement=lecture_fichier(fichier)
    temps= str(text_clock.cget("text"))

    fen2=Tk()
    fen2.title("Meilleurs Temps")
    fen2.geometry("%dx%d%+d%+d" % (600,400,(fen2.winfo_screenwidth()-600)//2,(fen2.winfo_screenheight()-400)//2)) # Taille et position de la fenetre
    fen2.config(background='#41B77F')


    # Style du tableau
    style = ttk.Style()
    style.theme_use("clam")
    style.map("Treeview")

    #tableau
    tableau = ttk.Treeview(fen2)
    tableau["columns"]=("Temps","Pseudo")
    tableau.column("#0", width=100, minwidth=30, stretch=NO)
    tableau.column("Temps", width=100, minwidth=30, stretch=NO)
    tableau.column("Pseudo", width=250, minwidth=30, stretch=NO)

    tableau.heading('#0', text='Classement')
    tableau.heading('Temps', text='Temps')
    tableau.heading('Pseudo', text='Nom')
    texteTitre = Label(fen2, text = '*** MEILLEURS TEMPS ***',font=("arial", 18),bg='#41B77F')
    texteTitre.place(height=30, width=350, x=120, y =5)

    tableau.delete(*tableau.get_children())
    for i in range (len(classement)):
        tableau.insert("", "end", i, text=i+1, values=(classement[i][0],classement[i][1]))
    tableau.place(height=240, width=580, x=10, y =105)
    if len(classement)==0:
        meilleur = True
    elif temps<=classement[-1][0] or len(classement)<10:
        meilleur = True
    else :
        meilleur = False

    if meilleur: # A remplacer par meilleur si groupe de trois

        texteLabel = Label(fen2, text = 'Entrer votre nom :',font=("arial", 12),bg='#41B77F')
        texteLabel.place(height=20, width=150, x=10, y =70)

        Texte1 = StringVar(master=fen2)
        Texte1.set(temps)
        texteLabel2 = Label(fen2, textvariable = Texte1,font=("arial", 12),bg='white')
        texteLabel2.place(height=20, width=100, x=150, y =40)

        tempsLabel = Label(fen2, text = 'Votre temps :',font=("arial", 12),bg='#41B77F')
        tempsLabel.place(height=20, width=100, x=20, y =40)

        monTexte=Entry(fen2)
        monTexte.place(height=25, width=250, x=150, y =70)

        bouton_ok = Button(fen2, text='VALIDER', command=lambda: modif_meilleur(fichier,classement,temps,monTexte.get(),bouton_ok))
        bouton_ok.place(height=30, width=120, x=450, y =70)

    bouton_quitter = Button(fen2, text='QUITTER',command=fen2.destroy)
    bouton_quitter.place(height=30, width=150, x=220, y =365)


    fen2.mainloop()




# gère le clic gauche de la souris
def pointeurG(event):
    global nb_cases_vues,start,stopchrono,on_joue
    if start==0:
        stopchrono=False
        start = default_timer()
        updateTime()
    # si la partie n'est pas en cours (quand on a perdu), blocage du jeu
    if on_joue :
        nCol = (event.x - gap) // dim +1
        nLig = (event.y - gap) // dim +1
        if nb_col >= nCol and nb_lig >= nLig:
            # si la cellule est vide
            if tab_j[nCol, nLig] == "":
                # Vérifie si on est bien dans le tableau
                if nCol>=1 and nCol<=nb_col and nLig>=1 and nLig<=nb_lig:
                    # Vérifie si la cellule contient une mine
                    if tab_m[nCol, nLig] == 9:
                        perdu()
                    else:
                        if tab_m[nCol, nLig]  >= 1:
                            affiche_nb_mines(tab_m[nCol, nLig], nCol, nLig )
                            affiche_compteurs()
                        else: # Traitement des cases vides
                            vide_plage_zero(nCol, nLig)
                # Vérification des compteurs
                if (nb_col*nb_lig) == nb_cases_vues and nb_mines_cachees == 0:
                    on_joue  = False
                    gagne()



# gère le clic droit de la souris
def pointeurD(event):
    global nb_mines_cachees, nb_cases_vues,start,on_joue
    # si la partie n'est pas en cours (quand on a perdu), blocage du jeu
    if start==0:
        start = default_timer()
        updateTime()
    if on_joue :
        nCol = (event.x - gap)// dim+1
        nLig = (event.y - gap) // dim+1
        if nb_col >= nCol and nb_lig >= nLig:
            # si la cellule est vide
            if tab_j[nCol, nLig]=="":
                # Affiche le drapeau
                can.create_image(nCol*dim-dim//2+gap, nLig*dim-dim//2+gap,
                                 image = im_flag)
                tab_j[nCol, nLig]="d"
                nb_cases_vues = nb_cases_vues + 1
                nb_mines_cachees = nb_mines_cachees - 1
            # si la cellule contient  un drapeau
            elif tab_j[nCol, nLig] == "d":
                # Remise à  blanc
                can.create_rectangle((nCol-1)*dim+gap+3,(nLig-1)*dim+gap+3,
                                     nCol*dim+gap-3,nLig*dim+gap-3,width=0, fill="grey")
                # Affiche le ?
                can.create_text(nCol*dim-dim//2+gap, nLig*dim-dim//2+gap,
                                text="?", fill='black',font='Arial 20')
                tab_j[nCol, nLig] = "?"
                # le ? n'est pas considéré comme une case traitée
                nb_cases_vues = nb_cases_vues - 1
                # Ajoute une mine car le ? ne désigne pas une mine
                nb_mines_cachees = nb_mines_cachees + 1
            # si la cellule contient un ?
            elif tab_j[nCol, nLig] == "?":
                # Remise à  blanc
                can.create_rectangle((nCol-1)*dim+gap+3,(nLig-1)*dim+gap+3,
                                     nCol*dim+gap-3,nLig*dim+gap-3,
                                     width=0, fill="#C6C6C6")
                # Stocke du vide dans le tableau de jeu
                tab_j[nCol, nLig] = ""
        affiche_compteurs()
        # Vérification des compteurs
        if ((nb_col*nb_lig) == nb_cases_vues and nb_mines_cachees == 0):
            on_joue  = False
            gagne()



# ----------------------------------------------------------------------------------------
# Début du programme
# ----------------------------------------------------------------------------------------

stopchrono=False
start=0
# Déclarations des variables lorsqu'on ouvre la fenêtre principale
# (niveau débutant par défaut)
nb_col, nb_lig, nb_mines = 0,0,0
dim, gap, nb_cases_vues = 30, 3, 0
on_joue = True

fen=Tk()
fen.title("Démineur")
fen.resizable(width=False, height=False)


# Chargement des images
im_mine = PhotoImage(file = "mine.png")
im_erreur = PhotoImage(file = "erreur.png")
im_flag = PhotoImage(file = "drapeau.png")
tab_m = {} # dictionnaire des mines
tab_j = {} # dictionnaire des cases modifiées par le joueur

can=Canvas(fen, width=(nb_col*dim)+gap, height=(nb_lig*dim)+gap, bg="grey")
can.bind("<Button-1>",pointeurG)
can.bind("<Button-3>",pointeurD)
can.pack(side=RIGHT)

# Frame à gauche de la grille de jeu pour disposer les boutons radios
f2 = Frame(fen)
# Création de cases à cocher pour le niveau
choix=IntVar()
choix.set(1)
case1=Radiobutton(f2)
case1.configure(text='Débutant', command=init_niveau, variable=choix,value=1)
case1.pack(anchor= NW ,padx=30)
case2=Radiobutton(f2)
case2.configure(text='Normal', padx=3, command=init_niveau, variable=choix,value=2)
case2.pack(anchor= NW, padx=30)
case2=Radiobutton(f2)
case2.configure(text='Avancé', padx=3, command=init_niveau, variable=choix,value=3)
case2.pack(anchor= NW, padx=30)
case3=Radiobutton(f2)
case3.configure(text='Expert', padx=3, command=init_niveau, variable=choix,value=4)
case3.pack(anchor= NW ,padx=30)
f2.pack()

# Frame à gauche de la grille de jeu pour les compteurs
f3 = Frame(fen)
# Champ pour l'affichage du décompte des mines
texte_mines = Label (f3, text = "Mines restantes :")
decompte_mines = Label (f3, text = "100")
texte_mines.grid(row=4,column=1,sticky='NW')
decompte_mines.grid(row=4,column=2,sticky='NE')
# Champ pour l'affichage du décompte des cases
texte_cases = Label (f3, text = "Cases à traiter :")
decompte_cases = Label (f3, text = "10")
texte_cases.grid(row=5,column=1,sticky='NW')
decompte_cases.grid(row=5,column=2,sticky='NE')

f3.pack()

# Frame à gauche de la grille de jeu pour disposer les boutons
f1 = Frame(fen)
bou1 = Button(f1, width=14, text="Nouvelle partie", font="Arial 10", command=lambda: init_jeu())
bou1.pack(side=BOTTOM, padx=5, pady=5)
f1.pack(side=BOTTOM)

# Frame à gauche de la grille de jeu pour afficher l'image
f4 = Frame(fen)

# Gestion du temps
def updateTime():
    if not stopchrono:
        now = default_timer() - start
        minutes, seconds = divmod(now, 60)
        hours, minutes = divmod(minutes, 60)
        str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
        text_clock.configure(text=str_time)
        fen.update_idletasks()
        fen.after(1000, updateTime)

text_clock = Label(f4,text='',font=("arial", 14))
text_clock.pack(side=BOTTOM)

texte_fin = Label (f4, text = "",font=("Arial", "20","bold"))
texte_fin.pack(side=BOTTOM)
photo=PhotoImage(file="demineur.png")
labl = Label(f4, image=photo)
labl.pack(side=TOP)
f4.pack()

init_niveau()
fen.mainloop()
