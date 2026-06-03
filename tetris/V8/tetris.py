import pygame
import random
import time
import copy
# Initialisation de Pygame
pygame.init()

# Parametres
running = True
afficher_coordonnee_souris = True
music = False # Activer ou desactiver la musique
taille_carreau = 55

if music:
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

# Parametres de delais
dernier_deplacement = time.time()  # Initialiser le dernier temps de déplacement
delai_deplacement = 0.2  # Délai pour ralentir les mouvements horizontaux et les rotations en secondes

# Dimensions de la fenêtre
screen_x = 660
screen_y = 1000

score = 0
police = pygame.font.SysFont("Arial" ,30)

# Configuration de la fenêtre
screen = pygame.display.set_mode((1300, screen_y))
pygame.display.set_caption("Tetris")

# Chargement des images des pièces
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
rect_prochaine_piece = pygame.image.load("prochaine_piece.png")


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

    def pivoter(self, matrice_j):
        """ rôle : faire pivoter la pièce """
        if self.y <= 500:
            # Faire pivoter la matrice
            self.matrice, pivote = self.rotater_matrix(self.matrice, matrice_j)

            if pivote:  # si on a pivoté la matrice
                # Faire pivoter l'image
                self.largeur, self.hauteur = self.image.get_size()
                self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

    def rotater_matrix(self, matrix, matrice_j):
        """ rôle : pivoter la matrice si c'est possible """
        pivote = True  # on pivote la pièce

        matrice2 = copy.deepcopy(matrix)  # on copie la matrice
        n = len(matrix)

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
    global score
    """ rôle : supprimer une ligne de la matrice du jeu si elle est pleine
        Entrées : matrice_j (list de list)
        Sortie : None
    """
    # vérifier si une ligne est pleine
    index = list()
    for ligne in matrice_j:
        pleine = True
        for p in ligne :
            if p == 0 : # on vérifie si il y a un 0 dans la ligne (si elle n'est pas pleine)
                pleine = False # dans ce cas la ligne n'est pas pleine
        if pleine :
            index.append(matrice_j.index(ligne)) # si elle est pleine on ajoute l'index de la ligne
            score += 10


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
    screen.blit(fond, (0, 0))
    for ligne in matrice_jeu:
        for carre in ligne:
            if carre != 0:
                carre.dessiner(screen)

    score_affichage = police.render(f'Score : {score}', 1, (255,255,255) )
    screen.blit(score_affichage,(680, 20))

    next_affichage = police.render(f'NEXT', 1, (255,255,255) )
    screen.blit(next_affichage,(10, 775))
    screen.blit(rect_prochaine_piece, (10, 820))

    piece_actuelle.dessiner(screen)
    prochaine_piece.dessiner(screen)
    pygame.display.flip()

# relancer le jeu
def reset():
    """ rôle : relancer le jeu
        Entrées : None
        Sortie : None
    """
    global matrice_jeu
    matrice_jeu = creer_matrice_jeu(screen_y, screen_x, taille_carreau) # on créé une matrice vide
    refresh()

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

# création de la matrice
matrice_jeu = creer_matrice_jeu(screen_y, screen_x, taille_carreau)

screen.blit(fond, (0, 0))
screen.blit(touches, (0, 0))
pygame.display.flip()
pygame.time.delay(5000)

couleur_prochaine_piece = random.choice(pieces)
prochaine_piece_forme = random.choice(list(matrice.values()))

# Boucle principale du jeu
while running:
    play = True
    perdu = False

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if play:
        # Initialisation de la pièce au début du jeu
        couleur_piece_actuelle = couleur_prochaine_piece
        piece_actuelle_forme = prochaine_piece_forme
        couleur_prochaine_piece = random.choice(pieces)
        prochaine_piece_forme = random.choice(list(matrice.values()))

        #Créé l'objet piece_actuelle avec sa couleur, son x de base, son y de base, sa matrice faisant sa forme
        piece_actuelle = Carre(couleur_piece_actuelle, screen_x // 2, -75, piece_actuelle_forme)
        hauteur_proch_piece = len(prochaine_piece_forme)-1
        prochaine_piece = Carre(couleur_prochaine_piece, 30, 893-55*hauteur_proch_piece, prochaine_piece_forme)

        refresh()# place les elements

        score += 1

        while play and not perdu:
            # play = nouvelle piece
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Vérification des touches enfoncées
            keys = pygame.key.get_pressed()

            # Délai pour mouvements gauche/droite/haut
            if time.time() - dernier_deplacement > delai_deplacement:

                # si cette touche est la fleche de gauche et que la piece n'est pas au bord gauche
                if keys[pygame.K_LEFT] and piece_actuelle.x - piece_actuelle.largeur >= 0:
                    piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                    piece_actuelle.deplacer(0, 1)
                    for ligne in matrice_jeu :
                        if any(piece_actuelle.collision(piece) for piece in ligne):
                            piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                    dernier_deplacement = time.time()

                # si cette touche est la fleche de droite et que la piece n'est pas au bord droit
                if keys[pygame.K_RIGHT] and piece_actuelle.x + (longueur_matrice(piece_actuelle_forme)+1) * piece_actuelle.largeur <= screen_x:
                    piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                    piece_actuelle.deplacer(0, 1)
                    for ligne in matrice_jeu :
                        if any(piece_actuelle.collision(piece) for piece in ligne):
                            piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                    dernier_deplacement = time.time()

                # si cette touche est la fleche du haut
                if keys[pygame.K_UP]:
                    piece_actuelle.pivoter(matrice_jeu)
                    dernier_deplacement = time.time()
                    piece_actuelle_forme = piece_actuelle.changer_matrice()

            # si cette touche est la fleche du bas
            if keys[pygame.K_DOWN] and piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur + 6 <= 638:
                piece_actuelle.deplacer(0, 6) # Fait chuter de +6y tout le long que l'on presse la fleche du bas
                for ligne in matrice_jeu :
                        if any(piece_actuelle.collision(piece) for piece in ligne):
                            piece_actuelle.deplacer(0, -6)


            piece_actuelle.deplacer(0, 1)

            # si il y a une collision avec un pièce, on la fige et on passe à la pièce suivante
            for ligne in matrice_jeu :
                if any(piece_actuelle.collision(piece) for piece in ligne):
                    piece_actuelle.deplacer(0, -1)
                    while piece_actuelle.y % 5 != 0:
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
            if piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur >= 638:
                while piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur != 640:
                    piece_actuelle.deplacer(0, 1)# On ajoute 1 au coordonées y de la pièce pour la faire tomber

                # ajouter la nouvelle pièce dans la matrice du jeu
                ajout_piece(piece_actuelle,taille_carreau,matrice_jeu)

                play = False
                # on vérifie si on complète une ligne et si oui, on la supprime
                supprimer_ligne(matrice_jeu,taille_carreau)

            if afficher_coordonnee_souris: # On affiche les coordonnées de la souris pour les tests
                coordonnee_souris()


    if perdu:# si on a perdu
        # on affiche tout + le game over pendant 4 sec
        screen.blit(fond, (0, 0))
        for ligne in matrice_jeu:
            for piece in ligne:
                if piece != 0 :
                    piece.dessiner(screen)
        piece_actuelle.dessiner(screen)

        next_affichage = police.render(f'NEXT', 1, (255,255,255) )
        screen.blit(next_affichage,(10, 775))
        screen.blit(rect_prochaine_piece, (10, 820))
        prochaine_piece.dessiner(screen)

        screen.blit(game_over, (14, screen_y // 4))
        screen.blit(rejouer, (0, 726))
        score_affichage_defaite = police.render(f'Score : {score}', 1, (255,0,0) )
        screen.blit(score_affichage_defaite,(10, 725))

        score = 0


        # si on appuie sur une touche on relance le jeu
        pygame.display.flip()
        attente_de_touche = True
        while attente_de_touche:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    attente_de_touche = False
                if event.type == pygame.QUIT:
                    pygame.quit() #Quitte
                    running = False
                    exit()
        reset()
        play = True

pygame.quit() #Quitte
