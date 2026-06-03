# Créé par maeva.cussonneau, le 17/12/2024 en Python 3.7
import pygame
import random

# Initialisation de Pygame
pygame.init()
running = True

music = False
if music:
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

# Dimensions de la fenêtre
info_ecran = pygame.display.Info()
screen_x = info_ecran.current_w
screen_y = info_ecran.current_h

fond = pygame.image.load("background.png")
fond_x, fond_y = fond.get_size()

# Configuration de la fenêtre
screen = pygame.display.set_mode((fond_x, fond_y))
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

# Enregistrement des pieces, Liste pour stocker les pièces placées
pieces_placees = []

# Initialisation des variables
rotation = 0 # defini la rotation de base
delai = 10 # defini le nombre d'images par seconde
largeur, hauteur = bleu_clair.get_size()
print('largeur = ',largeur)
carreau = largeur # defini la largeur d'un carreau
print(carreau)
pieces = [rouge, vert, bleu_fonce, violet, orange, bleu_clair, jaune]
noms_pieces = ["rouge", "vert", "bleu_fonce", "violet", "orange", "bleu_clair", "jaune"]

for i in range(len(pieces)):
    largeur, hauteur = pieces[i].get_size()
    print('piece = ',noms_pieces[i])
    print('largeur = ',largeur)
    print('hauteur = ',hauteur)
    print("\n")

# Classe du carré
class Carre:
    """
    Role:
        Boite qui peut contenir une certaine quantité de produits alimentaires et étre ouvertes
    Constructeur:
        Boite(_nom(str): le nom de l'objet,
            _ouverte (bool): True si la boite est ouverte,
            _capacite(int): sa capacité en cl,
            _quantite(int) sa quantité en cl)

        Méthodes: ouvrir()-> bool: _ ouverte <- True
            fermer() -> bool: Louverte <- False
            est_vide() -> bool: renvoie True si quantite == 0 est_pleine()-> bool: renvoie True si quantité == capacité
            ajouter (valeur) -> bool: quantité <- quantité + valeur si quantité + valeur <= ca
            retirer(valeur) -> bool: quantité <- quantité valeur si valeur <= quantité
    """
    # déclaration du constructeur
    def __init__(self, x, y, largeur):
        self.__x = x
        self.__y = y
        self.__rect=pygame.Rect(self.x-self.largeur,self.y-self.largeur,largeur*2,largeur*2)

# Fonction pour afficher les éléments
def refresh():
    screen.blit(fond, (0,0))
    for piece, x, y in pieces_placees:
        screen.blit(piece, (x, y))
    screen.blit(current_piece, (x_piece, y_piece))
    pygame.display.flip()

# fonction de la classe carre pour les collisions
def collision(self,autres_carres):
    """ rôle : gérer les collisions entre carres
        entrées : self(carre) : le carré qu'on regarde pour voir s'il entre en collision,
                autres_carres(list(carre)) : la liste tous les autres carrés posés avec leurs informations, dont les coordonnées
        sortie : none
    """
    global play

    # il n'y a pas encore de collision
    collide=False

    # on prend chaque carré dans toute la liste de carrés déjà posés
    for carre2 in autres_carres:
        # si leur coordonnées se superposent (si elles se touchent)
        if self.rectangle.colliderect(carre2.rectangle) == 1:
            # il y a collision

            collide=True

    # si il y a collision
    if collide:
            play = False



# Boucle principale du jeu
while running:

    play = True
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_x, screen_y = event.size
            screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
    if play:
        # Initialisation de la pièce au début du jeu
        current_piece = random.choice(pieces) # choisi au hasard une piece dans la liste pieces[]
        y_piece = 0 # La piece commence a tomber a partir de y = 0
        largeur, hauteur = current_piece.get_size() # get les dimensions de la piece
        x_piece = screen_x//2 # Met la piece au mimlieu de l'ecran (je retire la moitié de la piece car sinon le millieu est dans le coin de la piece)
        refresh() # place la piece

        while play:
            # play = nouvelle piece
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Vérification des touches enfoncées
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and x_piece - carreau >= 0:  # si cette touche est la fleche de gauche et que la piece n'est pas au bord gauche
                x_piece -= carreau
                if keys[pygame.K_DOWN] and y_piece + 6 <= 640:
                    y_piece += 6 # Fait chuter de +6y tout le long que l'on presse la fleche du bas

                pygame.time.delay(delai+ 100)

            if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and x_piece + carreau + largeur <= screen_x: # si cette touche est la fleche de droite et que la piece n'est pas au bord droit
                x_piece += carreau
                if keys[pygame.K_DOWN] and y_piece + 6 <= 640:
                    y_piece += 6 # Fait chuter de +6y tout le long que l'on presse la fleche du bas

                pygame.time.delay(delai+ 100)


            if keys[pygame.K_UP]: # si cette touche est la fleche du haut
                rotation = (rotation + 90) % 360
                current_piece = pygame.transform.rotate(current_piece, 90)
                pygame.time.delay(delai)

            if keys[pygame.K_DOWN] and y_piece + 6 <= 640:
                            y_piece += 6 # Fait chuter de +6y tout le long que l'on presse la fleche du bas

            pygame.time.delay(delai)

            y_piece += 1    # On ajoute 1 au coordonées y de la pièce pour la faire tomber
            refresh()
            # Si les coordonnées de la piece tombe sous 0 alors on passe a la piece suivante
            if y_piece >= fond_y - carreau:
                # On ajoute 1 au coordonées y de la pièce pour la faire tomber
                pieces_placees.append((current_piece, x_piece, y_piece))
                play = False

pygame.quit() #Quitte
