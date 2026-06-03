import pygame
import random

# Initialisation de Pygame
pygame.init()
running = True


# Dimensions de la fenêtre
screen_x = 660
screen_y = 600

# Configuration de la fenêtre
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Tetris")




# Chargement des images des pièces
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
carre = pygame.image.load("Carre.png")
escalier = pygame.image.load("Escalier.png")
escalier_mirroir = pygame.image.load("Escalier_mirroir.png")
barre = pygame.image.load("Barre.png")
L = pygame.image.load("L.png")
L_mirroir = pygame.image.load("L_mirroir.png")
T = pygame.image.load("T.png")




# Initialisation des variables
rotation = 0 # defini la rotation de base
delai = 50 # defini le nombre d'images par seconde
largeur, hauteur = T.get_size()
print('largeur = ',largeur)
carreau = largeur / 3 # defini la largeur d'un carreau
print(carreau)
pieces = [carre, escalier, escalier_mirroir, L, L_mirroir, T, barre]
noms_pieces = ["carre", "escalier", "escalier_mirroir", "L", "L_mirroir", "T", "barre"]
# Verification des pieces :

for i in range(len(pieces)):
    largeur, hauteur = pieces[i].get_size()
    print('piece = ',noms_pieces[i])
    print('largeur = ',largeur)
    print('hauteur = ',hauteur)
    print("\n")

# Fonction pour afficher les éléments
def refresh():
    screen.fill((0, 0, 0))
    screen.blit(piece, (x_piece, coordonnee_y_piece))
    pygame.display.flip()




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
        piece = random.choice(pieces) # choisi au hasard une piece dans la liste pieces[]
        coordonnee_y_piece = 0 # La piece commence a tomber a partir de y = 0
        largeur, hauteur = piece.get_size() # get les dimensions de la piece
        x_piece = 0 # Met la piece au mimlieu de l'ecran (je retire la moitié de la piece car sinon le millieu est dans le coin de la piece)
        refresh() # place la piece


        while play:
            # play = nouvelle piece
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.VIDEORESIZE:
                    screen_x, screen_y = event.size
                    screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN: # Si on presse une touche
                    if event.key == pygame.K_LEFT and x_piece - carreau >= 0: # si cette touche est la fleche de gauche et que la piece n'est pas au bord gauche
                        x_piece -= carreau
                    elif event.key == pygame.K_RIGHT and x_piece + carreau + largeur <= screen_x: # si cette touche est la fleche de droite et que la piece n'est pas au bord droit
                        x_piece += carreau
                    elif event.key == pygame.K_UP: # si cette touche est la fleche du haut
                        rotation = (rotation + 90) % 360
                        piece = pygame.transform.rotate(piece, 90)

            # Vérification des touches enfoncées pour accélérer la chute
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                coordonnee_y_piece += 6 # Fait chuter de +6y tout le long que l'on presse la fleche du bas

            # Affiche les éléments
            coordonnee_y_piece += 1    # On ajoute 1 au coordonées y de la pièce pour la faire tomber
            refresh()
            pygame.time.delay(delai)

            # Si les coordonnées de la piece tombe sous 0 alors on passe a la piece suivante
            if coordonnee_y_piece + hauteur >= screen_y:
                play = False

pygame.quit() #Quitte
