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
nb_mikados = 8

# Parametres de delais
dernière_action = time.time()  # Initialiser le dernier temps d'action du joueur
delai = 0.2  # Délai pour supprimer des mikados lorsque c'est au joueur de jouer

police = pygame.font.SysFont("Arial" ,30)

# Dimensions de la fenêtre
screen_x = 1150
screen_y = 720


# configuration de la musique
if music:
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()


# Configuration de la fenêtre
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("Jeu de Nim")

# Chargement des images des pièces
fond = pygame.image.load("fond_table.jpg")
fond = pygame.transform.scale(fond,(1150,720))
bouton_nombre = pygame.image.load("bouton nombre.png")
bouton_quitte = pygame.image.load("bouton quitte.jpg")
bouton_nombre = pygame.transform.scale(bouton_nombre,(800,222))
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

dict_mikados = {} # le dictionnaire qui contient toutes les images de mikados
mikado1 = pygame.image.load("mikado1.png")
dict_mikados[1] = [mikado1,[20,268]]
mikado2 = pygame.image.load("mikado2.png")
dict_mikados[2] = [mikado2,[27,252]]
mikado3 = pygame.image.load("mikado3.png")
dict_mikados[3] = [mikado3,[37,268]]
mikado4 = pygame.image.load("mikado4.png")
dict_mikados[4] = [mikado4,[19,328]]
mikado5 = pygame.image.load("mikado5.png")
dict_mikados[5] = [mikado5,[28,276]]
mikado6 = pygame.image.load("mikado6.png")
dict_mikados[6] = [mikado6,[18,500]]

#configuration de la personne qui débute le tour
def debut():
    tour = random.randint(1,2)              # créer une variable qui prend aléatoirement 1 ou 2
    if tour == 1:                           # si la variable est égal à 1 alors c'est l'humain qui commence sinon c'est la machine
        premier_humain = True
        premier_machine = False
    else:
        premier_humain = False
        premier_machine = True


# configuration de la liste de mikados
def creer_liste_mikados(dict):
    """ rôle = créer la liste avec le nombre de mikados avec lesquels on joue et l'image qui correspond
        entrées : dict(img,[int,int]) : le dictionnaire contenant les images des mikados et leur dimension
        sortie : list
    """
    batons = list() # on créé une liste pour savoir le nombre de mikados qu'il reste en jeu
    for chiffre in range(nb_mikados):
        numero_baton = (chiffre+1)%6
        if numero_baton == 0:
            numero_baton = 6
        batons.append(numero_baton)
    return batons

# configuration de la liste de mikados
def creer_liste_mikados(dict):
    """ rôle = créer la liste avec le nombre de mikados avec lesquels on joue et l'image qui correspond
        entrées : dict(img,[int,int]) : le dictionnaire contenant les images des mikados et leur dimension
        sortie : list
    """
    batons = list() # on créé une liste pour savoir le nombre de mikados qu'il reste en jeu
    for chiffre in range(nb_mikados):
        numero_baton = (chiffre+1)%6
        if numero_baton == 0:
            numero_baton = 6
        batons.append(numero_baton)
    return batons

# configuration de la liste de mikados
def supprimer_mikado(list,int):
    """ rôle = supprimer des mikados
        entrées : list : la liste de mikados restants en jeu , int : le nombre de mikados à supprimer
        sortie : list
    """
    longueur = len(list)
    return list[:longueur-int]

# afficher les coordonnées de la souris
def coordonnee_souris():
    """ rôle : afficher les coordonnées de la souris
        Entrées : None
        Sortie : None
    """
    co = pygame.mouse.get_pos()
    return co


# Fonction pour afficher les éléments
def refresh():
    """ rôle : afficher les éléments
        Entrées : None
        Sortie : None
    """
    screen.blit(fond, (0, 0)) # on affiche le fond
    screen.blit(bouton_quitte, (screen_x-200, screen_y-70)) # on affiche le bouton pour quitter le jeu

    longueur = 349
    # on affiche tous les mikados qu'il reste à afficher
    for chiffre in range(len(batons_restants)):
        image = dict_mikados[batons_restants[chiffre]][0]
        hauteur = (screen_y - dict_mikados[batons_restants[chiffre]][1][1]) // 2
        screen.blit(image,(longueur + chiffre * 20 , hauteur))
        longueur += dict_mikados[batons_restants[chiffre]][1][0]
    if tour_joueur:
        screen.blit(bouton_nombre,((screen_x-800)//2, 500))

    pygame.display.flip()

# Fonction pour afficher les éléments nécessaires au tour du joueur
def affichage_joueur():

    gg

# Fonction pour dire à qui est le tour
def affiche_tour(police_tour):

    global tour_joueur
    if tour_joueur == True:
        affichage_tour = police_tour.render(f'à ton tour !', 1, (255,255,255) )
        screen.blit(affichage_tour,(715, 500))
        pygame.display.flip()
        pygame.time.delay(1000) # petit délai pour lire le tetris
    if tour_joueur == False:
        affichage_tour = police_tour.render(f'ce n est pas encore ton tour...', 1, (255,255,255) )
        screen.blit(affichage_tour,(715, 500))
        pygame.display.flip()
        pygame.time.delay(1000) # petit délai pour lire le tetris


# relancer le jeu
def reset():
    """ rôle : relancer le jeu
        Entrées : None
        Sortie : None
    """
    global batons_restants
    batons_restants = creer_liste_mikados(dict_mikados)
    refresh()


screen.blit(fond, (0, 0)) # on affiche le fond
pygame.display.flip()


batons_restants = creer_liste_mikados(dict_mikados)
tour_joueur = True


# Boucle principale du jeu
while running:
    play = True
    jeu_termine = False

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if play:
        affiche_tour(police)
        while play and not jeu_termine:
            # play = nouveau tour
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if tour_joueur == True : # si c'est au joueur de jouer

                # Délai pour supprimer des mikados
                if time.time() - dernière_action > delai:

                    # si le joueur a cliqué sur l'écran
                    if event.type == pygame.MOUSEBUTTONDOWN and not jeu_termine:

                        co = coordonnee_souris()

                        # si il a cliqué sur le bouton 1
                        if 252 <= co[0] <= 407 and 530 <= co[1] <= 700:
                            batons_restants = supprimer_mikado(batons_restants,1)

                        # si il a cliqué sur le bouton 2
                        if 479 <= co[0] <= 635 and 530 <= co[1] <= 700:
                            batons_restants = supprimer_mikado(batons_restants,2)

                        # si il a cliqué sur le bouton 3
                        if 722 <= co[0] <= 878 and 530 <= co[1] <= 700:
                            batons_restants = supprimer_mikado(batons_restants,3)

                        print(batons_restants)
                        refresh()
                        dernière_action = time.time()
                        play = False
                        tour_joueur = False

            if len(batons_restants) == 0:
                jeu_termine = True

            refresh()

            if afficher_coordonnee_souris: # On affiche les coordonnées de la souris pour les tests
                print(coordonnee_souris())


    if jeu_termine:# si le jeu est fini
        # on affiche tout
        screen.blit(fond, (0, 0))
        screen.blit(bouton_quitte, (screen_x-200, screen_y-70))

        # si on appuie sur une touche on relance le jeu
        pygame.display.flip()
        attente_de_touche = True
        while attente_de_touche:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    attente_de_touche = False
                    dernière_action = time.time()
                if event.type == pygame.QUIT:
                    pygame.quit() #Quitte
                    running = False
                    exit()
        reset()
        play = True

pygame.quit() #Quitte
