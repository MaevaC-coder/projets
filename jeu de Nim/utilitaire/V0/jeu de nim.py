import pygame
import random
import time
import copy
# Initialisation de Pygame
pygame.init()

# Parametres
running = True
afficher_coordonnee_souris = False
music = False # Activer ou desactiver la musique
taille_carreau = 55

if music:
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

# Dimensions de la fenêtre
screen_x = 1150
screen_y = 720

# Configuration de la fenêtre
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("Jeu de Nim")

# Chargement des images des pièces
fond = pygame.image.load("fond_table.jpg")
fond = pygame.transform.scale(fond,(1150,720))
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
mikado1 = pygame.image.load("mikado1.png")
mikado2 = pygame.image.load("mikado2.png")
mikado3 = pygame.image.load("mikado3.png")
mikado4 = pygame.image.load("mikado4.png")
mikado5 = pygame.image.load("mikado5.png")
mikado6 = pygame.image.load("mikado6.png")


#configuration de la personne qui débute le tour
def debut():
    tour = random.randint(1,2)              # créer une variable qui prend aléatoirement 1 ou 2
    if tour == 1:                           # si la variable est égal à 1 alors c'est l'humain qui commence sinon c'est la machine
        premier_humain = True
        premier_machine = False
    else:
        premier_humain = False
        premier_machine = True


# afficher les coordonnées de la souris
def coordonnee_souris():
    """ rôle : afficher les coordonnées de la souris
        Entrées : None
        Sortie : None
    """
    co = pygame.mouse.get_pos()


# Fonction pour afficher les éléments
def refresh():
    """ rôle : afficher les éléments
        Entrées : None
        Sortie : None
    """
    screen.blit(fond, (0, 0)) # on affiche le fond

    pygame.display.flip()

# relancer le jeu
def reset():
    """ rôle : relancer le jeu
        Entrées : None
        Sortie : None
    """
    refresh()

screen.blit(fond, (0, 0)) # on affiche le fond
pygame.display.flip()



# Boucle principale du jeu
while running:
    play = True
    perdu = False

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if play:

        while play and not perdu:
            # play = nouvelle piece
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            refresh()

            if afficher_coordonnee_souris: # On affiche les coordonnées de la souris pour les tests
                coordonnee_souris()


    if perdu:# si on a perdu
        # on affiche tout + le game over pendant 4 sec avec tous les autres éléments du jeu
        screen.blit(fond, (0, 0))

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
