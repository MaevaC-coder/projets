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

# Configuration de la fenêtre
screen = pygame.display.set_mode((screen_x, screen_y))
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

# Classe du carré
class Carre:
    def __init__(self, image, x, y, forme):
        self.image = image
        self.x = x
        self.y = y
        self.largeur, self.hauteur = image.get_size()
        self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        self.forme = forme
        self.matrice = self.generer_matrice()

    def generer_matrice(self):
        return self.forme

    def dessiner(self, surface):
        for ligne in range(len(self.matrice)):
            for colonne in range(len(self.matrice[ligne])):
                if self.matrice[ligne][colonne]:
                    surface.blit(self.image, (self.x + colonne * self.largeur, self.y + ligne * self.hauteur))

    def deplacer(self, deplacement_x, deplacement_y):
        self.x += deplacement_x
        self.y += deplacement_y
        self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

    def pivoter(self, p_placees):
        if self.y<= 500:
            # Faire pivoter l'image
            self.image = pygame.transform.rotate(self.image, 90)
            self.largeur, self.hauteur = self.image.get_size()
            self.rectangle = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

            # Faire pivoter la matrice
            self.matrice = self.rotater_matrix(self.matrice, p_placees)

    def rotater_matrix(self, matrix, p_placees):
        matrice2 = copy.deepcopy(self.matrice) # on copie la matrice
        self.matrice = [list(reversed(col)) for col in zip(*matrix)] # on fait pivoter la matrice originale
        largeur_m = self.x + (longueur_matrice(self.matrice)+1) * self.largeur # on calcule la longueur de la matrice originale après pivotation

        if largeur_m <= screen_x and largeur_m >= 0: # si la matrice après pivotation est comprise dans l'écran
            if any(self.collision(p) for p in p_placees): # si elle percute une autre piece après rotation
                self.matrice = matrice2 # on retourne la pièce non pivotée

        else :
            self.matrice = matrice2 # sinon on retourne la pièce non pivotée
        return self.matrice # on retourne la matrice

    def changer_matrice(self):
        return self.matrice

    def collision(self, autre):
        for ligne in range(len(self.matrice)):
            for colonne in range(len(self.matrice[ligne])):
                if self.matrice[ligne][colonne]:
                    self_rectangle = pygame.Rect(
                        self.x + colonne * self.largeur,
                        self.y + ligne * self.hauteur,
                        self.largeur, self.hauteur)
                    for ligne_autre in range(len(autre.matrice)):
                        for colonne_autre in range(len(autre.matrice[ligne_autre])):
                            if autre.matrice[ligne_autre][colonne_autre]:
                                autre_rectangle = pygame.Rect(
                                    autre.x + colonne_autre * autre.largeur,
                                    autre.y + ligne_autre * autre.hauteur,
                                    autre.largeur, autre.hauteur)
                                if self_rectangle.colliderect(autre_rectangle):
                                    return True  # il y a collision
        return False

# Liste pour stocker les pièces placées
pieces_placees = []

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

# Fonction pour afficher les éléments
def refresh():
    screen.blit(fond, (0, 0))
    for piece in pieces_placees:
        piece.dessiner(screen)
    piece_actuelle.dessiner(screen)
    pygame.display.flip()
    print(piece_actuelle.x)

def coordonnee_souris():
    co = pygame.mouse.get_pos()
    print(co)

def longueur_matrice(matrice): # determine le nombre de pixel que fait la forme donnée
    longueur_max = 0
    for ligne in matrice:
        longueur_max = max(longueur_max, len(ligne))
    return longueur_max

def reset():
    global pieces_placees
    pieces_placees = []
    refresh()


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
        couleur_piece_actuelle = random.choice(pieces)
        piece_actuelle_forme = random.choice(list(matrice.values()))

        #Créé l'objet piece_actuelle avec sa couleur, son x de base, son y de base, sa matrice faisant sa forme
        piece_actuelle = Carre(couleur_piece_actuelle, screen_x // 2, -55, piece_actuelle_forme)

        refresh()# place les elements

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
                    if any(piece_actuelle.collision(piece) for piece in pieces_placees):
                        piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                    dernier_deplacement = time.time()

                # si cette touche est la fleche de droite et que la piece n'est pas au bord droit
                if keys[pygame.K_RIGHT] and piece_actuelle.x + (longueur_matrice(piece_actuelle_forme)+1) * piece_actuelle.largeur <= screen_x:
                    print(piece_actuelle_forme)
                    piece_actuelle.deplacer(piece_actuelle.largeur, 0)
                    piece_actuelle.deplacer(0, 1)
                    if any(piece_actuelle.collision(piece) for piece in pieces_placees):
                        piece_actuelle.deplacer(-piece_actuelle.largeur, 0)
                    dernier_deplacement = time.time()

                # si cette touche est la fleche du haut
                if keys[pygame.K_UP]:
                    piece_actuelle.pivoter(pieces_placees)
                    dernier_deplacement = time.time()
                    piece_actuelle_forme = piece_actuelle.changer_matrice()

            # si cette touche est la fleche du bas
            if keys[pygame.K_DOWN] and piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur + 6 <= 638:
                piece_actuelle.deplacer(0, 6) # Fait chuter de +6y tout le long que l'on presse la fleche du bas
                if any(piece_actuelle.collision(piece) for piece in pieces_placees):
                    piece_actuelle.deplacer(0, -6)


            piece_actuelle.deplacer(0, 1)
            if any(piece_actuelle.collision(piece) for piece in pieces_placees):
                piece_actuelle.deplacer(0, -1)
                pieces_placees.append(piece_actuelle)

                # Si les coordonnées de la piece sont supérieures à la ligne du haut alors on a un game over
                if piece_actuelle.y < 0:
                    perdu = True
                    play = False
                play = False

            refresh()

            # Si les coordonnées de la piece tombe sous 638 alors on la fait descendre doucement jusqu'a la barre et on passe a la piece suivante
            if piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur >= 638:
                while piece_actuelle.y + len(piece_actuelle_forme) * piece_actuelle.hauteur - piece_actuelle.hauteur != 640:
                    piece_actuelle.deplacer(0, 1)# On ajoute 1 au coordonées y de la pièce pour la faire tomber
                pieces_placees.append(piece_actuelle)
                print(len(piece_actuelle.matrice) * piece_actuelle.hauteur)

            if afficher_coordonnee_souris: # On affiche les coordonnées de la souris pour les tests
                coordonnee_souris()


    if perdu:# si on a perdu
        # on affiche tout + le game over pendant 4 sec
        screen.blit(fond, (0, 0))
        for piece in pieces_placees:
            piece.dessiner(screen)
        piece_actuelle.dessiner(screen)
        screen.blit(game_over, (14, screen_y // 4))
        screen.blit(rejouer, (0, 726))

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
