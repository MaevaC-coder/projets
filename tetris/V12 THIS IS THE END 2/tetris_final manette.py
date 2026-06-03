import pygame
import random
import time
import copy
import csv
from tkinter import *
from tkinter import ttk
import winsound

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()

# initialisation du module joystick
pygame.joystick.init()


# Parametres
running = True
afficher_coordonnee_souris = False
music = True # Activer ou desactiver la musique
taille_carreau = 55

if music:
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)

# Parametres de delais
dernier_deplacement = time.time()  # Initialiser le dernier temps de déplacement
dernier_deplacementgd = time.time()
derniere_rotation = time.time()
delai_deplacement = 0.2  # Délai pour ralentir les rotations en secondes
delai_gauche_droite = 0.12 # Délai pour ralentir les mouvements horizontaux en secondes




# nombre de manettes connectées
nb_manettes = pygame.joystick.get_count()

# on affiche le nombre de manettes connectées pour les tests
#print("nb manettes = ",nb_manettes)

# si une manette ou plus est connectée, on initialise la première pour jouer
if nb_manettes >= 1:
    manette1 = pygame.joystick.Joystick(0)
    manette1.init()




# Dimensions de la fenêtre VERSION PETIT ECRAN
screen_x = 660
screen_y = 750

# Dimensions de la fenêtre VERSION GRAND ECRAN
#screen_x = 660
#screen_y = 1000

# Configuration de la fenêtre VERSION PETIT ECRAN
screen = pygame.display.set_mode((950, screen_y))

# Configuration de la fenêtre VERSION GRAND ECRAN
#screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("Tetris")




# Chargement des images des pièces
bouton_quitte = pygame.image.load("bouton quitte.jpg")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
rouge = pygame.image.load("rouge.png")
vert = pygame.image.load("vert.png")
bleu_fonce = pygame.image.load("bleu_fonce.png")
jaune = pygame.image.load("jaune.png")
violet = pygame.image.load("violet.png")
orange = pygame.image.load("orange.png")
bleu_clair = pygame.image.load("bleu_clair.png")
fond = pygame.image.load("background.png")
game_over = pygame.image.load("game_over.png")
rejouer = pygame.image.load("rejouer_texte.png")
rejouer = pygame.transform.scale(rejouer,(660,333))
touches = pygame.image.load("touches.png")
touches_manette = pygame.image.load("touche_manette.png")
rect_prochaine_piece = pygame.image.load("prochaine_piece.png")
fond_cote = pygame.image.load("fond_cote.png")


# Classe du carré
class Carre:
    # constructeur
    def __init__(self, image, x, y, forme):
        self.image = image
        self.x = x
        self.y = y
        self.largeur, self.hauteur = image.get_size()
        self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        self.forme = forme
        self.matrice = self.generer_matrice()


    # Méthodes

    def generer_matrice(self):
        """ rôle : générer la matrice
        """
        return self.forme

    def dessiner(self, surface):
        """ rôle : dessiner la pièce sur l'écran
        """
        for ligne in range(len(self.matrice)):
            for colonne in range(len(self.matrice[ligne])): # on prend chaque ligne et colonne
                if self.matrice[ligne][colonne]: # si il y a un 1, on dessine un carré
                    surface.blit(self.image, (self.x + colonne * self.largeur, self.y + ligne * self.hauteur))

    def deplacer(self, deplacement_x, deplacement_y):
        """ rôle : déplacer la pièce en fonction du déplacement en bas et sur le côté qu'on lui applique
        """
        self.x += deplacement_x # déplacer vers le bas
        self.y += deplacement_y # déplacer à gauche ou à droite
        self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur) # recalculer la surface que prend la pièce (utile pour les collisions)

    def pivoter_droite(self, matrice_j):
        """ rôle : faire pivoter la pièce à droite"""
        if self.y <= 500:
            # Faire pivoter la matrice
            self.matrice, pivote = self.rotater_matrix(self.matrice, matrice_j)

            if pivote:  # si on a pivoté la matrice
                # Faire pivoter l'image
                self.largeur, self.hauteur = self.image.get_size()
                self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

    def pivoter_gauche(self, matrice_j):
        """ rôle : faire pivoter la pièce à  gauche """
        if self.y <= 500:
            # on sauvegarde la pièce avant rotation
            hauteur2 = self.hauteur
            largeur2 = self.largeur
            x2 = self.x
            y2 = self.y
            matrice2 = self.matrice

            # on effectue la rotation 3 fois pour avoir la rotation à gauche
            rotation = list()
            for i in range(3):
                # Faire pivoter la matrice
                self.matrice, pivote = self.rotater_matrix(self.matrice, matrice_j)

                if pivote:  # si on a pivoté la matrice
                    rotation.append(1)
                    # Faire pivoter l'image
                    self.largeur, self.hauteur = self.image.get_size()
                    self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

            # si la pièce n'a pas été pivotée trois fois
            if len(rotation) != 3:
                # c'est qu'on ne peut pas faire la rotation à gauche donc on revient à la pièce de base
                self.hauteur = hauteur2
                self.largeur = largeur2
                self.x = x2
                self.y = y2
                self.matrice = matrice2


    def rotater_matrix(self, matrix, matrice_j):
        """ rôle : pivoter la matrice si c'est possible """
        pivote = True  # on pivote la pièce

        matrice2 = copy.deepcopy(matrix)  # on copie la matrice

        # Calcul de la rotation autour du centre de la matrice
        center_x = self.x + (self.largeur * (len(matrix[0]) // 2))
        center_y = self.y + (self.hauteur * (len(matrix) // 2))

        # Rotation de la matrice autour de son centre
        self.matrice = [list(reversed(col)) for col in zip(*matrix)]

        # Nouvelles coordonnées du centre après rotation
        new_center_x = self.x + (self.largeur * (len(self.matrice[0]) // 2))
        new_center_y = self.y + (self.hauteur * (len(self.matrice) // 2))

        # Ajustement basé sur le nouveau centre
        self.x -= (new_center_x - center_x)
        self.y -= (new_center_y - center_y)

        # Vérification si la matrice est dans les limites de l'écran après rotation
        x_min = self.x
        x_max = x_min + len(self.matrice[0]) * self.largeur
        y_min = self.y
        y_max = y_min + len(self.matrice) * self.hauteur

        if x_min >= 0 and x_max <= screen_x and y_max <= screen_y:  # si la matrice après pivotation est comprise dans l'écran
            for ligne in matrice_j:
                if any(self.collision(p) for p in ligne): # si elle percute une autre piece après rotation
                    self.matrice = matrice2  # on retourne la pièce non pivotée
                    # On retourne aussi les coordonnées d'origine
                    self.x += (new_center_x - center_x)
                    self.y += (new_center_y - center_y)
                    pivote = False  # donc on n'a pas pivoté la pièce
        else:
            self.matrice = matrice2  # sinon on retourne la pièce non pivotée
            # On retourne aussi les coordonnées d'origine
            self.x += (new_center_x - center_x)
            self.y += (new_center_y - center_y)
            pivote = False  # donc on n'a pas pivoté la pièce

        return self.matrice, pivote  # on retourne la matrice et si on a tourné la pièce


    def descendre_matrix(self, piece_forme , matrice_j):
        """ rôle : descendre la matrice si c'est possible """
        global vitesse

        # coordonnées de base
        ancien_x = self.x
        ancien_y = self.y


        self.deplacer(0, vitesse + 5) # Fait chuter de +5y tout le long que l'on presse la fleche du bas

        if self.y + len(piece_forme) * self.hauteur - self.hauteur >= 640 - vitesse:
            # On retourne aussi les coordonnées d'origine
            self.x = ancien_x
            self.y = ancien_y
            self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

        for ligne in matrice_j:
            if any(self.collision(p) for p in ligne): # si elle percute une autre piece après rotation
                # On retourne aussi les coordonnées d'origine
                self.x = ancien_x
                self.y = ancien_y
                self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)


    def changer_matrice(self):
        """ rôle : retourner la matrice
        """
        return self.matrice

    def collision(self, autre):
        """ rôle : vérifier si la pièce actuelle percute une autre
        """
        if autre != 0:
            # calculer la surface que prend la pièce
            for ligne in range(len(self.matrice)):
                for colonne in range(len(self.matrice[ligne])):
                    if self.matrice[ligne][colonne]:
                        self_rectangle = pygame.Rect(
                            self.x + colonne * self.largeur,
                            self.y + ligne * self.hauteur,
                            self.largeur, self.hauteur)

                        # on prend chaque autre pièce posée et on calcule la surface que celle ci
                        for ligne_autre in range(len(autre.matrice)):
                            for colonne_autre in range(len(autre.matrice[ligne_autre])):
                                if autre.matrice[ligne_autre][colonne_autre]:
                                    autre_rectangle = pygame.Rect(
                                        autre.x + colonne_autre * autre.largeur,
                                        autre.y + ligne_autre * autre.hauteur,
                                        autre.largeur, autre.hauteur)

                                    # si les deux rectangles se percutent il y a une collision
                                    if self_rectangle.colliderect(autre_rectangle):
                                        return True  # il y a collision
        return False

# afficher les coordonnées de la souris
def coordonnee_souris():
    """ rôle : afficher les coordonnées de la souris
        Entrées : None
        Sortie : None
    """
    co = pygame.mouse.get_pos()
    return co

def longueur_matrice(matrice): # determine le nombre de pixel que fait la forme donnée
    """ rôle : determiner le nombre de pixel que fait la forme donnée
        Entrées : matrice(matrice)
        Sortie : int
    """
    longueur_max = 0
    for ligne in matrice:
        longueur_max = max(longueur_max, len(ligne)) # on prend la longueur maximum
    return longueur_max

# Fonction qui créé la matrice du jeu
def creer_matrice_jeu(hauteur_fenetre, largeur_fenetre, taille_carreau):
    """ rôle : créer la matrice du jeu entier en fonction des carreaux posés
        Entrées : hauteur_fenetre (int), largeur_fenetre (int), taille_carreau (int)
        Sortie : matrice (list de list)
    """
    hauteur_grille = hauteur_fenetre // taille_carreau
    largeur_grille = largeur_fenetre // taille_carreau
    matrice_jeu = [[0] * largeur_grille for _ in range(hauteur_grille)] # on remplit la grille de 0

    return matrice_jeu

# Fonction qui ajoute une pièce à la matrice du jeu
def ajout_piece(piece,taille_c,matrice_j):
    """ rôle : ajouter une pièce à la matrice du jeu
        Entrées : piece (Carre), taille_c (int), matrice_j (matrice)
        Sortie : None
    """
    for y in range(len(piece.matrice)): # on prend chaque colonne de la matrice
        for x in range(len(piece.matrice[y])): # on prend chaque ligne de la matrice

            if piece.matrice[y][x]:  # Si la matrice a un carré ici
                grille_x = (piece.x // taille_c) + x # on calcule sa position en x dans la matrice
                grille_y = (piece.y // taille_c) + y # on calcule sa position en y dans la matrice

                x_car = piece.x + x*taille_c # on calcule la coordonnée en x du carré sur l'écran
                y_car = piece.y + y*taille_c # on calcule la coordonnée en y du carré sur l'écran

                matrice_j[grille_y][grille_x] = Carre(piece.image, x_car , y_car, [[1]]) # on ajoute à la matrice le carré correspondant

# Fonction qui supprime une ligne lorsqu'elle est pleine
def supprimer_ligne(matrice_j,taille_c):
    global score, nb_lignes, nb_20lignes, vitesse, vitesse_max, acceleration, police_tetris, chrono
    """ rôle : supprimer une ligne de la matrice du jeu si elle est pleine
        Entrées : matrice_j (list de list)
        Sortie : None
    """
    # vérifier si une ligne est pleine
    index = list()
    nbr_ligne_effectuees = 0
    for ligne in matrice_j:
        pleine = True
        for p in ligne :
            if p == 0 : # on vérifie si il y a un 0 dans la ligne (si elle n'est pas pleine)
                pleine = False # dans ce cas la ligne n'est pas pleine
        if pleine :
            index.append(matrice_j.index(ligne)) # si elle est pleine on ajoute l'index de la ligne
            nbr_ligne_effectuees += 1
            nb_lignes += 1

    if nbr_ligne_effectuees ==1: # une ligne vaut 40 points
        score += 40

        # m = pygame.mixer.Sound("lignes.mp3")
        # m.play()

    if nbr_ligne_effectuees ==2: # deux lignes 100 points
        score += 100

        # m = pygame.mixer.Sound("lignes.mp3")
        # m.play()

    if nbr_ligne_effectuees ==3: # trois lignes 300 points
        score += 300

        # m = pygame.mixer.Sound("lignes.mp3")
        # m.play()

    if nbr_ligne_effectuees >= 4: # un tetris vaut 1200 points
        score += 1200

        # m = pygame.mixer.Sound("tetris.mp3")
        # m.play()

        # on affiche le texte tetris !
        tetris_affichage = police_tetris.render(f'Tetris !', 1, (255,255,255) )
        screen.blit(tetris_affichage,(250, 300))
        pygame.display.flip()

        pygame.time.delay(1000) # petit délai pour lire le tetris

    # toutes les 4 lignes on accélère la vitesse tant qu'on a pas atteint la vitesse max
    if nb_lignes >= (nb_20lignes+1) * 4:
        if vitesse < vitesse_max :
            vitesse += 1
            nb_20lignes += 1
            acceleration = True

    acceleration_affichage = police_tetris.render(f'accélération', 1, (255,255,255) )

    chrono = time.time()
    if acceleration:
        if time.time() - chrono < 2:
            screen.blit(acceleration_affichage,(200, 300))
        else:
            acceleration = False

    pygame.display.flip()



    for i in index: # pour chaque ligne pleine
        del matrice_j[i] # on supprime la ligne
        matrice_j.insert(0, [0] * len(matrice_j[0])) # on insère une ligne de 0
        for ligneb in range(i+1): # pour chaque ligne au dessus de celle qu'on vient de supprimer
            for p2 in matrice_j[ligneb]: # si on a une pièce
                if p2  != 0: # on la fait descendre d'une ligne
                    p2.y = p2.y + taille_c
    refresh() # rafraichit la page avec la nouvelle matrice du jeu

# Fonction pour afficher les éléments
def refresh():
    """ rôle : afficher les éléments
        Entrées : None
        Sortie : None
    """
    global fond, matrice_jeu, fond_cote, police, bouton_quitte, rect_prochaine_piece
    global piece_sauv, prochaine_piece, piece_actuelle, screen, acceleration, chrono

    screen.blit(fond, (0, 0)) # on affiche le fond
    for ligne in matrice_jeu: # puis toutes les pièces
        for carre in ligne:
            if carre != 0:
                carre.dessiner(screen)

    # on affiche le score VERSION GRAND ECRAN
    # score_affichage = police.render(f'Score : {score}', 1, (255,255,255) )
    # screen.blit(score_affichage,(10, 725))

    # on affiche le score et le nombre de lignes complétées avec le bouton quitter VERSION PETIT ECRAN
    screen.blit(fond_cote,(660, 0)) # on doit superposer un rectangle noir sur le côté pour ne plus voir les infos précédentes
    score_affichage = police.render(f'Score : {score}', 1, (255,255,255) )
    screen.blit(score_affichage,(680, 95))

    lignes_affichage = police.render(f'Lignes : {nb_lignes}', 1, (255,255,255) )
    screen.blit(lignes_affichage,(680, 145))

    niveau_affichage = police.render(f'Niveau : {vitesse}', 1, (255,255,255) )
    screen.blit(niveau_affichage,(680, 195))

    screen.blit(bouton_quitte, (screen_x+90, 0))

    # on affiche le cadre et texte pour la prochaine pièce VERSION GRAND ECRAN
    # next_affichage = police.render(f'NEXT', 1, (255,255,255) )
    # screen.blit(next_affichage,(10, 775))
    # screen.blit(rect_prochaine_piece, (10, 820))

    # on affiche le cadre et texte pour la prochaine pièce VERSION PETIT ECRAN
    next_affichage = police.render(f'NEXT', 1, (255,255,255) )
    screen.blit(next_affichage,(680, 245))
    screen.blit(rect_prochaine_piece, (680, 290))

    # on affiche le cadre et texte pour la pièce sauvegardée VERSION PETIT ECRAN
    sauv_affichage = police.render(f'SAUV', 1, (255,255,255) )
    screen.blit(sauv_affichage,(680, 450))
    screen.blit(rect_prochaine_piece, (680, 495))

    if piece_sauv is not None:
        piece_sauv.dessiner(screen)


    piece_actuelle.dessiner(screen) # on affiche la prochaine pièce et la pièce actuelle
    prochaine_piece.dessiner(screen)

    acceleration_affichage = police_tetris.render(f'accélération', 1, (255,255,255) )
    if acceleration:
        if time.time() - chrono < 2:
            screen.blit(acceleration_affichage,(200, 300))
        else:
            acceleration = False

    pygame.display.flip()


# mettre le jeu en pause
def affichage_pause():
    """ rôle : mettre le jeu en pause
        Entrées : None
        Sortie : None
    """
    global manette1, bouton_pause, dernier_deplacement,delai_deplacement, nb_manettes

    pause_affichage1 = police.render(f'Appuyer sur le bouton 10', 1, (255,0,0) )
    pause_affichage2 = police.render(f'pour continuer à jouer', 1, (255,0,0) )
    screen.blit(pause_affichage1,(14, 250))
    screen.blit(pause_affichage2,(14, 330))
    pygame.display.flip()

    dernier_deplacement = time.time()
    pause = True
    while pause:
        if time.time() - dernier_deplacement > delai_deplacement:
            for event in pygame.event.get():

                # si le joueur a cliqué sur l'écran
                if event.type == pygame.MOUSEBUTTONDOWN:
                    co = coordonnee_souris()

                    # si il a cliqué sur le bouton quitter
                    if screen_x + 90 <= co[0] <= screen_x + 290 and 0 <= co[1] <= 70:
                        pygame.quit()
                        exit()

                if nb_manettes >= 1:
                    # si le joueur a cliqué sur un bouton de manette
                    if event.type == pygame.JOYBUTTONDOWN:

                        bouton_pause = manette1.get_button(9)
                        bouton_quit = manette1.get_button(8)

                        if bouton_quit:
                            pygame.quit()
                            exit()

                        if bouton_pause:
                            pause = False

                else:
                    # Vérification des touches enfoncées
                    keys = pygame.key.get_pressed()

                    # si on met le jeu en pause
                    if keys[pygame.K_p]:
                        pause = False
                        dernier_deplacement = time.time()

    refresh()

# relancer le jeu
def reset():
    """ rôle : relancer le jeu
        Entrées : None
        Sortie : None
    """
    global matrice_jeu, score, vitesse, nb_20lignes, nb_lignes, couleur_piece_sauv, piece_sauv_forme, piece_sauv

    matrice_jeu = creer_matrice_jeu(screen_y, screen_x, taille_carreau) # on créé une matrice vide

    score = 0 # le score est remis à 0
    vitesse =  1
    nb_lignes = 0
    nb_20lignes = 0

    couleur_piece_sauv = None
    piece_sauv_forme = None
    piece_sauv = None

    refresh()


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

def modif_meilleur(fichier,donnees,score,Nom,bouton_ok):
    """ Description : Modifie les meilleurs scores en ajoutant les données de la partie:
        Entrées : fichier : Nom du fichier à modifier ; STR
                  donnees : LIST (LIST) : Liste des meilleurs scores à modifier
                  score : score de la partie ; STR
                  Nom : nom du joueur ; STR
                  bouton_ok : objet  bouton de Tkinter pour la fonction Enre_fichier
        Retour : aucun
    """
    # Insérer les nouveaux scores dans la liste
    i=0
    longueur = len(donnees)
    fin=False
    if longueur != 0:
        while i<longueur and not fin:
            if score<int(donnees[i][0]):
                i += 1
            else :
                fin = True
    if i == longueur:
        donnees.append([str(score),Nom])
    else :
        donnees.insert(i,[str(score),Nom])
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


def classement():
    global tableau, score

    fichier='Meilleur.csv'

    classement=lecture_fichier(fichier)

    fen2=Tk()
    fen2.title("Meilleurs Score")
    fen2.geometry("%dx%d%+d%+d" % (600,400,(fen2.winfo_screenwidth()-600)//2,(fen2.winfo_screenheight()-400)//2)) # Taille et position de la fenetre
    fen2.config(background='#41B77F')


    # Style du tableau
    style = ttk.Style()
    style.theme_use("clam")
    style.map("Treeview")

    #tableau
    tableau = ttk.Treeview(fen2)
    tableau["columns"]=("Score","Pseudo")
    tableau.column("#0", width=100, minwidth=30, stretch=NO)
    tableau.column("Score", width=100, minwidth=30, stretch=NO)
    tableau.column("Pseudo", width=250, minwidth=30, stretch=NO)

    tableau.heading('#0', text='Classement')
    tableau.heading('Score', text='Score')
    tableau.heading('Pseudo', text='Nom')
    texteTitre = Label(fen2, text = '*** MEILLEURS SCORES ***',font=("arial", 18),bg='#41B77F')
    texteTitre.place(height=30, width=350, x=120, y =5)

    tableau.delete(*tableau.get_children())
    for i in range (len(classement)):
        tableau.insert("", "end", i, text=i+1, values=(classement[i][0],classement[i][1]))
    tableau.place(height=240, width=580, x=10, y =105)
    if len(classement)==0:
        meilleur = True
    elif score>= int(classement[-1][0]) or len(classement)<10:
        meilleur = True
    else :
        meilleur = False

    if meilleur: # A remplacer par meilleur si groupe de trois

        texteLabel = Label(fen2, text = 'Entrez votre nom :',font=("arial", 12),bg='#41B77F')
        texteLabel.place(height=20, width=150, x=10, y =70)

        Texte1 = StringVar(master=fen2)
        Texte1.set(str(score))
        texteLabel2 = Label(fen2, textvariable = Texte1,font=("arial", 12),bg='white')
        texteLabel2.place(height=20, width=100, x=150, y =40)

        tempsLabel = Label(fen2, text = 'Votre score :',font=("arial", 12),bg='#41B77F')
        tempsLabel.place(height=20, width=100, x=20, y =40)

        monTexte=Entry(fen2)
        monTexte.place(height=25, width=250, x=150, y =70)

        bouton_ok = Button(fen2, text='VALIDER', command=lambda: modif_meilleur(fichier,classement,score,monTexte.get(),bouton_ok))
        bouton_ok.place(height=30, width=120, x=450, y =70)

    bouton_quitter = Button(fen2, text='QUITTER',command=fen2.destroy)
    bouton_quitter.place(height=30, width=150, x=220, y =365)


    fen2.mainloop()

# Initialisation des variables
delai = 100
pieces = [rouge, vert, bleu_fonce, violet, orange, bleu_clair, jaune]
matrice = {
    "I": [[1, 1, 1, 1]],            # Grande barre
    "J": [[1, 0, 0], [1, 1, 1]],    # L mirroir
    "L": [[0, 0, 1], [1, 1, 1]],    # L
    "O": [[1, 1], [1, 1]],          # Carré
    "S": [[0, 1, 1], [1, 1, 0]],    # Z mirroir
    "T": [[0, 1, 0], [1, 1, 1]],    # T
    "Z": [[1, 1, 0], [0, 1, 1]],    # Z
}


# initialisation des variables
score = 0
nb_lignes = 0
nb_20lignes = 0
vitesse_max = 7
vitesse = 1
police = pygame.font.SysFont("Arial" ,30)
police_tetris = pygame.font.SysFont("Arial" ,60)



# création de la matrice
matrice_jeu = creer_matrice_jeu(screen_y, screen_x, taille_carreau)

screen.blit(fond, (0, 0)) # on affiche le fond
if nb_manettes >= 1:
    screen.blit(touches_manette,(0,0))
else :
    screen.blit(touches, (0, 0)) # on affiche les commandes des touches
screen.blit(bouton_quitte, (screen_x+90, 0)) # on affiche le bouton quitter
pygame.display.flip()
pygame.time.delay(5000) # petit délai pour lire les commandes

acceleration = False
chrono = time.time()

# on tire au sort la prochaine pièce
couleur_prochaine_piece = random.choice(pieces)
prochaine_piece_forme = random.choice(list(matrice.values()))

couleur_piece_sauv = None
piece_sauv_forme = None
piece_sauv = None
sauv = False
nb_sauv = 0



# Boucle principale du jeu
while running:
    play = True
    perdu = False

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    if play:
        if sauv :
            if piece_sauv is not None:

                # Initialisation de la pièce au début du jeu
                couleur_piece_actuelle = couleur_piece_sauv
                piece_actuelle_forme = piece_sauv_forme
                piece_actuelle = piece_sauv

            else:
                # Initialisation de la pièce au début du jeu et de la prochaine pièce
                couleur_piece_actuelle = couleur_prochaine_piece
                piece_actuelle_forme = prochaine_piece_forme

                couleur_prochaine_piece = random.choice(pieces)
                prochaine_piece_forme = random.choice(list(matrice.values()))

                hauteur_proch_piece = len(prochaine_piece_forme)-1
                # on calcule la hauteur pour placer les pièces au bon niveau dans le rectangle VERSION PETIT ECRAN
                prochaine_piece = Carre(couleur_prochaine_piece, 700, 238-55*hauteur_proch_piece+125, prochaine_piece_forme)

            # on sauvegarde l'ancienne pièce
            couleur_piece_sauv = couleur_ancien
            piece_sauv_forme = forme_ancien

            hauteur_piece_sauv = len(piece_sauv_forme)-1
            # on calcule la hauteur pour placer les pièces au bon niveau dans le rectangle VERSION PETIT ECRAN
            piece_sauv = Carre(couleur_piece_sauv, 700, 238-55*hauteur_piece_sauv+330, piece_sauv_forme)

            sauv = False
            # on vérifie que le joueur ne fait pas qu'échanger les pièces
            nb_sauv = 1


        else :

            # Initialisation de la pièce au début du jeu et de la prochaine pièce
            couleur_piece_actuelle = couleur_prochaine_piece
            piece_actuelle_forme = prochaine_piece_forme

            couleur_prochaine_piece = random.choice(pieces)
            prochaine_piece_forme = random.choice(list(matrice.values()))

            hauteur_proch_piece = len(prochaine_piece_forme)-1

            # on calcule la hauteur pour placer les pièces au bon niveau dans le rectangle VERSION PETIT ECRAN
            prochaine_piece = Carre(couleur_prochaine_piece, 700, 238-55*hauteur_proch_piece+125, prochaine_piece_forme)
            # le joueur n'a pas fait qu'échanger les pièces
            nb_sauv = 0


        couleur_ancien = couleur_piece_actuelle
        forme_ancien = piece_actuelle_forme
        dernier_deplacement = time.time()

        #Créé l'objet piece_actuelle avec sa couleur, son x de base, son y de base, sa matrice faisant sa forme
        piece_actuelle = Carre(couleur_piece_actuelle, screen_x // 2, -75, piece_actuelle_forme)

        # on calcule la hauteur pour placer les pièces au bon niveau dans le rectangle VERSION GRAND ECRAN
        # prochaine_piece = Carre(couleur_prochaine_piece, 30, 893-55*hauteur_proch_piece, prochaine_piece_forme)

        refresh()# place les elements

        score += 1




        while play and not perdu:

            # play = nouvelle piece
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # si le joueur a cliqué sur l'écran
                if event.type == pygame.MOUSEBUTTONDOWN:
                    co = coordonnee_souris()

                    # si il a cliqué sur le bouton quitter
                    if screen_x + 90 <= co[0] <= screen_x + 290 and 0 <= co[1] <= 70:
                        pygame.quit()
                        exit()


                if nb_manettes >= 1:
                    # si le joueur quitte le jeu avec la manette
                    if event.type == pygame.JOYBUTTONDOWN:

                        # détection du bouton quitter
                        bouton_quit = manette1.get_button(8)
                        bouton_pause = manette1.get_button(9)

                        if bouton_quit:
                            pygame.quit()
                            exit()

                        # si on met le jeu en pause
                        if bouton_pause:
                            affichage_pause()

            # s'il y a au moins une manette de connectée
            if nb_manettes >= 1 :

                # déplacements pour la manette

                # Délai pour mouvements gauche/droite
                if time.time() - dernier_deplacementgd > delai_gauche_droite:

                    # si on appuie sur la croix directionnelle
                    if event.type == pygame.JOYHATMOTION:

                        # détection croix directionnelle
                        croix = manette1.get_hat(0)


                        # si on appuie sur la fleche de gauche et que la piece n'est pas au bord gauche
                        if croix[0] < 0 and piece_actuelle.x - piece_actuelle.largeur >= 0:
                            piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                            piece_actuelle.deplacer(0, vitesse)
                            for ligne in matrice_jeu :
                                if any(piece_actuelle.collision(piece) for piece in ligne):
                                    piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                            dernier_deplacementgd = time.time()


                        # si on appuie sur la fleche de droite et que la piece n'est pas au bord droit
                        if croix[0] > 0 and piece_actuelle.x + (longueur_matrice(piece_actuelle_forme)+1) * piece_actuelle.largeur <= screen_x:
                            piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                            piece_actuelle.deplacer(0, vitesse)
                            for ligne in matrice_jeu :
                                if any(piece_actuelle.collision(piece) for piece in ligne):
                                    piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                            dernier_deplacementgd = time.time()


                    # si on bouge un joystick
                    if event.type == pygame.JOYAXISMOTION:

                        # détection joystick gauche
                        # récupérer les  deux axes du joystick de gauche
                        axe_x = manette1.get_axis(0) # horizontal
                        axe_y = manette1.get_axis(1) # vertical


                        # si on bouge le joystick gauche vers la gauche et que la piece n'est pas au bord gauche
                        if axe_x <= -0.5 and piece_actuelle.x - piece_actuelle.largeur >= 0:
                            piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                            piece_actuelle.deplacer(0, vitesse)
                            for ligne in matrice_jeu :
                                if any(piece_actuelle.collision(piece) for piece in ligne):
                                    piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                            dernier_deplacementgd = time.time()


                        # si on bouge le joystick gauche vers la droite et que la piece n'est pas au bord droit
                        if axe_x >= 0.5  and piece_actuelle.x + (longueur_matrice(piece_actuelle_forme)+1) * piece_actuelle.largeur <= screen_x:
                            piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                            piece_actuelle.deplacer(0, vitesse)
                            for ligne in matrice_jeu :
                                if any(piece_actuelle.collision(piece) for piece in ligne):
                                    piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                            dernier_deplacementgd = time.time()


                # délai pour les mouvements haut et sauvegarder
                if time.time() - dernier_deplacement > delai_deplacement:

                    # si on appuie sur un bouton
                    if event.type == pygame.JOYBUTTONDOWN:

                        # détection des boutons
                        bouton_s = manette1.get_button(5)

                        if bouton_s:

                            if nb_sauv != 1:

                                sauv = True
                                play = False

                    # si on appuie sur la croix directionnelle
                    if event.type == pygame.JOYHATMOTION:

                        # détection croix directionnelle
                        croix = manette1.get_hat(0)

                        # si on appuie sur la fleche du bas
                        if croix[1] < 0 and piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur + 6 <= 638:
                            # si possible on descend la pièce
                            piece_actuelle.descendre_matrix(piece_actuelle_forme,matrice_jeu)


                    # si on bouge un joystick
                    if event.type == pygame.JOYAXISMOTION:

                        # détection joystick gauche
                        # récupérer les  deux axes du joystick de gauche
                        axe_x = manette1.get_axis(0) # horizontal
                        axe_y = manette1.get_axis(1) # vertical

                        # si on bouge le joystick gauche vers le bas
                        if axe_y >= 0.5 and piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur + 6 <= 638:
                            # si possible on descend la pièce
                            piece_actuelle.descendre_matrix(piece_actuelle_forme,matrice_jeu)



                # délai pour les rotations
                if time.time() - derniere_rotation > delai_deplacement:


                    # si on appuie sur un bouton
                    if event.type == pygame.JOYBUTTONDOWN:

                        # détection des boutons
                        bouton_g = manette1.get_button(0)
                        bouton_d = manette1.get_button(2)

                        # si on appuie sur le bouton 1 on tourne à gauche
                        if bouton_g:
                            piece_actuelle.pivoter_gauche(matrice_jeu)
                            derniere_rotation = time.time()
                            piece_actuelle_forme = piece_actuelle.changer_matrice()

                        # si on appuie sur le bouton 3 on tourne à droite
                        if bouton_d:
                            piece_actuelle.pivoter_droite(matrice_jeu)
                            derniere_rotation = time.time()
                            piece_actuelle_forme = piece_actuelle.changer_matrice()






            # s'il n'y a pas de manette de détectée
            else:

                    # Vérification des touches enfoncées
                    keys = pygame.key.get_pressed()

                    # si on met le jeu en pause
                    if time.time() - dernier_deplacement > delai_deplacement:
                        if keys[pygame.K_p]:
                            affichage_pause()

                        # si on sauvegarde une piece et que le joueur ne fait pas qu'échanger les pièces
                        if keys[pygame.K_s]:

                            if nb_sauv != 1:

                                sauv = True
                                play = False


                    # Délai pour mouvements gauche/droite
                    if time.time() - dernier_deplacementgd > delai_gauche_droite:

                        # si cette touche est la fleche de gauche et que la piece n'est pas au bord gauche
                        if keys[pygame.K_LEFT] and piece_actuelle.x - piece_actuelle.largeur >= 0:
                            piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                            piece_actuelle.deplacer(0, vitesse)
                            for ligne in matrice_jeu :
                                if any(piece_actuelle.collision(piece) for piece in ligne):
                                    piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                            dernier_deplacementgd = time.time()


                        # si cette touche est la fleche de droite et que la piece n'est pas au bord droit
                        if keys[pygame.K_RIGHT] and piece_actuelle.x + (longueur_matrice(piece_actuelle_forme)+1) * piece_actuelle.largeur <= screen_x:
                            piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                            piece_actuelle.deplacer(0, vitesse)
                            for ligne in matrice_jeu :
                                if any(piece_actuelle.collision(piece) for piece in ligne):
                                    piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                            dernier_deplacementgd = time.time()



                    # délai pour les rotations
                    if time.time() - derniere_rotation > delai_deplacement:

                        # si cette touche est la barre espace on tourne à gauche
                        if keys[pygame.K_SPACE]:
                            piece_actuelle.pivoter_gauche(matrice_jeu)
                            derniere_rotation = time.time()
                            piece_actuelle_forme = piece_actuelle.changer_matrice()


                        # si cette touche est la fleche du haut on tourne à droite
                        if keys[pygame.K_UP]:
                            piece_actuelle.pivoter_droite(matrice_jeu)
                            derniere_rotation = time.time()
                            piece_actuelle_forme = piece_actuelle.changer_matrice()


                    # Délai pour mouvements haut
                    if time.time() - dernier_deplacement > delai_deplacement:

                        # si cette touche est la fleche du bas
                        if keys[pygame.K_DOWN] and piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur + 6 <= 638:
                            # si possible on descend la pièce
                            piece_actuelle.descendre_matrix(piece_actuelle_forme,matrice_jeu)



            #on fait descendre la pièce vers le bas
            piece_actuelle.deplacer(0, vitesse)

            # si il y a une collision avec un pièce, on la fige et on passe à la pièce suivante
            for ligne in matrice_jeu :
                if any(piece_actuelle.collision(piece) for piece in ligne):
                    piece_actuelle.deplacer(0, -vitesse)
                    while (piece_actuelle.y+20) % taille_carreau != 0:
                        piece_actuelle.deplacer(0, 1)


                    # on ajoute la pièce dans la matrice du jeu
                    ajout_piece(piece_actuelle,taille_carreau,matrice_jeu)
                    play = False
                    # on vérifie si on complète une ligne et si oui, on la supprime
                    supprimer_ligne(matrice_jeu,taille_carreau)

                    # Si les coordonnées de la piece sont supérieures à la ligne du haut alors on a un game over
                    if piece_actuelle.y < 0:
                        perdu = True
                        play = False

            refresh()

            # Si les coordonnées de la piece tombe sous 638 alors on la fait descendre doucement jusqu'a la barre et on passe a la piece suivante
            if piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur >= 640 - (vitesse+1):
                while piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur != 640:
                    piece_actuelle.deplacer(0, 1)# On ajoute 1 au coordonées y de la pièce pour la faire tomber

                # ajouter la nouvelle pièce dans la matrice du jeu
                ajout_piece(piece_actuelle,taille_carreau,matrice_jeu)

                play = False
                # on vérifie si on complète une ligne et si oui, on la supprime
                supprimer_ligne(matrice_jeu,taille_carreau)

            if afficher_coordonnee_souris: # On affiche les coordonnées de la souris pour les tests
                print(coordonnee_souris())





    if perdu:# si on a perdu
        dernier_deplacement = time.time()
        # on affiche tout + le game over pendant 4 sec avec tous les autres éléments du jeu
        screen.blit(fond, (0, 0))
        for ligne in matrice_jeu:
            for piece in ligne:
                if piece != 0 :
                    piece.dessiner(screen)
        piece_actuelle.dessiner(screen)

        screen.blit(game_over, (14, 250))

        #l = pygame.mixer.Sound("intro game over.wav")
        #l.play(1)
        if music:
            pygame.mixer.music.load("intro game over.mp3")
            pygame.mixer.music.play(1)

        # affichage du texte pour rejouer et le score de la défaite VERSION GRAND ECRAN
        # screen.blit(rejouer, (0, 726))
        # score_affichage_defaite = police.render(f'Score : {score}', 1, (255,0,0) )
        # screen.blit(score_affichage_defaite,(10, 725))

        # affichage du texte pour rejouer, des lignes et du score de la défaite VERSION PETIT ECRAN
        screen.blit(rejouer, (0, 500))
        screen.blit(fond_cote,(660, 0)) # on doit superposer un rectangle noir sur le côté pour ne plus voir les infos précédentes
        screen.blit(bouton_quitte, (screen_x+90, 0))
        score_affichage_defaite = police.render(f'Score : {score}', 1, (255,0,0) )
        screen.blit(score_affichage_defaite,(680, 120))

        lignes_affichage = police.render(f'Lignes : {nb_lignes}', 1, (255,0,0) )
        screen.blit(lignes_affichage,(680, 170))


        # si on appuie sur une touche on relance le jeu
        pygame.display.flip()

        pygame.time.delay(2000) # petit délai pour lire le texte pour rejouer

        classement()

        attente_de_touche = True
        while attente_de_touche:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit() #Quitte
                    running = False
                    exit()

                # si le joueur a cliqué sur l'écran
                if event.type == pygame.MOUSEBUTTONDOWN:
                    co = coordonnee_souris()

                    # si il a cliqué sur le bouton quitter
                    if screen_x + 90 <= co[0] <= screen_x + 290 and 0 <= co[1] <= 70:
                        pygame.quit()
                        exit()

                if time.time() - dernier_deplacement > delai_deplacement:

                    if nb_manettes >= 1:

                        # si le joueur quitte le jeu avec la manette
                        if event.type == pygame.JOYBUTTONDOWN:

                            # détection du bouton quitter
                            bouton_quit = manette1.get_button(8)
                            print(bouton_quit)

                            if bouton_quit:
                                pygame.quit()
                                exit()

                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.JOYBUTTONDOWN :
                        attente_de_touche = False
                        if music:
                            pygame.mixer.music.load("music.mp3")
                            pygame.mixer.music.play(-1)
        reset()
        play = True

pygame.quit() #Quitte
