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

# police d'écriture du texte affiché
police = pygame.font.SysFont("Arial" ,80)

# Dimensions de la fenêtre
screen_x = 1150
screen_y = 680


# configuration de la musique
if music:
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()


# Configuration de la fenêtre
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("Jeu de Nim")

# Chargement des images du jeu
fond = pygame.image.load("fond_table.jpg")
fond = pygame.transform.scale(fond,(1150,720))

bouton_nombre = pygame.image.load("bouton nombre.png")
bouton_regles = pygame.image.load("bouton règle.jpg")
bouton_fermer = pygame.image.load("bouton fermer.jpg")
bouton_quitte = pygame.image.load("bouton quitte.jpg")

bouton_nombre = pygame.transform.scale(bouton_nombre,(800,222))

regles = pygame.image.load("règles.png")

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


# configuration de la liste de mikados
def creer_liste_mikados(dict):
    """ rôle = créer la liste avec le nombre de mikados avec lesquels on joue et le chiffre de l'image qui correspond
        entrées : dict(img,[int,int]) : le dictionnaire contenant les images des mikados et leur dimension
        sortie : list
    """
    batons = list() # on créé une liste pour savoir le nombre de mikados qu'il reste en jeu

    for chiffre in range(nb_mikados): # on numérote les mikados restants de 1 à 6 dans l'ordre croissant
        numero_baton = (chiffre+1)%6
        if numero_baton == 0:
            numero_baton = 6
        batons.append(numero_baton)

    return batons

# supprimer des mikados
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
    screen.blit(bouton_quitte, (screen_x-200, 0)) # on affiche le bouton pour quitter le jeu
    screen.blit(bouton_regles, (screen_x-200, screen_y-70)) # on affiche le bouton pour les regles

    # on affiche tous les mikados qu'il reste à afficher
    longueur = 349
    for chiffre in range(len(batons_restants)):
        image = dict_mikados[batons_restants[chiffre]][0]
        hauteur = (screen_y - dict_mikados[batons_restants[chiffre]][1][1]) // 2
        screen.blit(image,(longueur + chiffre * 20 , hauteur))
        longueur += dict_mikados[batons_restants[chiffre]][1][0]

    # si c'est au joueur de jouer, on affiche les boutons pour pouvoir supprimer des mikados
    if tour_joueur:
        screen.blit(bouton_nombre,((screen_x-800)//2, 460))

    pygame.display.flip()

# Fonction pour créer les gobelets de l'IA
def gobelets():
    """ rôle : créer les gobelets de l'IA
        Entrées : None
        Sortie : dict(list) : les gobelets
    """
    global nb_mikados

    # pour chaque nombre possible de mikados restants on associe la liste du nombre de mikados pouvant être supprimés
    gobelets = {}
    for mikado in range(2,nb_mikados):
        gobelets[mikado+1] = [1,2,3]

    # quand il ne reste que 1 mikado on peut ne supprimer que 1 mikado
    gobelets[1] = [1]
    # quand il ne reste que 2 mikados on peut ne supprimer que 1 ou 2 mikados
    gobelets[2] = [1,2]

    return gobelets


# Procédure pour afficher à qui est le tour
def affiche_tour(police_tour):
    """ rôle : afficher le message de début de tour
        Entrées : police_tour(font) : la police
        Sortie : None
    """

    global tour_joueur

    # si c'est au joueur de jouer
    if tour_joueur == True:
        affichage_tour = police_tour.render(f'à ton tour !', 1, (255,255,255) )
        screen.blit(affichage_tour,(455, 30))
        pygame.display.flip()
        pygame.time.delay(1300) # petit délai pour lire le texte

    # si c'est à la machine de jouer
    else:
        affichage_tour1 = police_tour.render(f"ce n'est pas", 1, (255,255,255) )
        affichage_tour2 = police_tour.render(f'encore ton tour...', 1, (255,255,255) )
        screen.blit(affichage_tour1,(455, 20))
        screen.blit(affichage_tour2,(455, 80))
        pygame.display.flip()
        pygame.time.delay(2000) # petit délai pour lire le texte

    # on réaffiche tout
    refresh()

# relancer le jeu
def reset():
    """ rôle : relancer le jeu
        Entrées : None
        Sortie : None
    """
    global batons_restants, tour_joueur, dernier_coup, abandonner, play

    # on réinitalise tout
    batons_restants = creer_liste_mikados(dict_mikados)
    tour_joueur = True
    dernier_coup = 0
    abandonner = False
    play = True

    # on réaffiche tout
    refresh()





# Programme principal


# on affiche le fond
screen.blit(fond, (0, 0))
pygame.display.flip()

# on créé la liste des mikados
batons_restants = creer_liste_mikados(dict_mikados)

# c'est toujours au joueur de commencer
tour_joueur = True

# on créé les gobelets pour l'IA
gobelets = gobelets()

# variables
dernier_coup = 0
abandonner = False
manches_gagnees = 0
nb_manches_jouees = 0


# Boucle principale du jeu
while running:
    play = True
    jeu_termine = False

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # play = nouveau tour
    if play:

        # si il reste encore des mikados
        if len(batons_restants) != 0:
            refresh()
            # on affiche le message du tour
            affiche_tour(police)

        while play and not jeu_termine:

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # si il ne reste plus de mikados la partie s'arrête
            if len(batons_restants) == 0:
                jeu_termine = True

                # si c'est le joueur qui a joué le dernier tour il a gagné
                if not tour_joueur:
                    gagne = True

                # sinon c'est la machine qui a gagné
                else:
                    gagne = False

            # Délai pour chaque action
            elif time.time() - dernière_action > delai:

                # si le joueur a cliqué sur l'écran
                if event.type == pygame.MOUSEBUTTONDOWN:
                    co = coordonnee_souris()

                    # si il a cliqué sur le bouton quitter
                    if screen_x - 200 <= co[0] <= screen_x and 0 <= co[1] <= 70:
                        pygame.quit()
                        exit()

                    # s'il a cliqué sur le bouton de règles
                    if screen_x - 200 <= co[0] <= screen_x and screen_y-70 <= co[1] <= screen_y:
                        dernier_deplacement = time.time()
                        # on affiche les regles et le bouton pour les fermer
                        screen.blit(bouton_fermer,(screen_x-200, screen_y-70))
                        screen.blit(regles,(0, 0))
                        pygame.display.flip()

                        # tant que l'utilisateur lit les règles
                        lecture_regles = True
                        while lecture_regles:
                            for event in pygame.event.get():

                                # si le joueur a cliqué sur l'écran
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    co = coordonnee_souris()

                                    # si il a cliqué sur le bouton quitter
                                    if screen_x - 200 <= co[0] <= screen_x and 0 <= co[1] <= 70:
                                        pygame.quit()
                                        exit()

                                    # si il a cliqué sur le bouton fermer on ferme la page de règles
                                    if screen_x - 200 <= co[0] <= screen_x and screen_y-70 <= co[1] <= screen_y:
                                        lecture_regles = False

                        refresh()

                # si c'est au joueur de jouer
                if tour_joueur == True :

                    # si le joueur a cliqué sur l'écran
                    if event.type == pygame.MOUSEBUTTONDOWN and not jeu_termine:

                        co = coordonnee_souris()

                        # si il a cliqué sur le bouton 1
                        if 252 <= co[0] <= 407 and 530 <= co[1] <= 700:
                            batons_restants = supprimer_mikado(batons_restants,1)

                            # on passe au tour suivant
                            play = False
                            tour_joueur = False
                            refresh()

                        # si il a cliqué sur le bouton 2
                        if 479 <= co[0] <= 635 and 530 <= co[1] <= 700:
                            batons_restants = supprimer_mikado(batons_restants,2)

                            # on passe au tour suivant
                            play = False
                            tour_joueur = False
                            refresh()

                        # si il a cliqué sur le bouton 3
                        if 722 <= co[0] <= 878 and 530 <= co[1] <= 700:
                            batons_restants = supprimer_mikado(batons_restants,3)

                            # on passe au tour suivant
                            play = False
                            tour_joueur = False
                            refresh()

                        dernière_action = time.time()

                # si c'est à la machine de jouer
                else:

                    # si le gobelet dans lequel pioche machine n'est pas vide
                    if len(gobelets[len(batons_restants)]) != 0:

                        # elle prend tout les jetons du gobelet
                        choix = len(gobelets[len(batons_restants)])

                        # elle tire au sort le jeton qu'elle prend
                        indice_choix = random.randint(0,choix-1)
                        nb_supprimes = gobelets[len(batons_restants)][indice_choix]

                        # elle garde en mémoire son dernier coup
                        dernier_coup = [len(batons_restants),nb_supprimes]

                        # on affiche combien de mikados elle supprime
                        affichage_machine1 = police.render(f"La machine", 1, (17,98,216) )
                        if nb_supprimes>1:
                            affichage_machine2 = police.render(f'supprime {nb_supprimes} bâtons', 1, (17,98,216) )
                        else:
                            affichage_machine2 = police.render(f'supprime {nb_supprimes} bâton', 1, (17,98,216) )

                        screen.blit(affichage_machine1,(455, 20))
                        screen.blit(affichage_machine2,(455, 80))

                        pygame.display.flip()
                        pygame.time.delay(2500) # petit délai pour lire le texte

                        # elle suprime autant de mikados qu'indiqué sur le jeton
                        batons_restants = supprimer_mikado(batons_restants,nb_supprimes)

                        # on passe au tour suivant
                        play = False
                        tour_joueur = True
                        refresh()

                    # sinon s'il n'y a plus de jetons dans le gobelet qu'elle prend
                    else:

                        # on affiche le message d'abandon
                        affichage_machine1 = police.render(f"La machine a", 1, (255,255,255) )
                        affichage_machine2 = police.render(f"choisi d'abandonner", 1, (255,255,255) )

                        screen.blit(affichage_machine1,(455, 20))
                        screen.blit(affichage_machine2,(455, 80))
                        pygame.display.flip()
                        pygame.time.delay(1000) # petit délai pour lire le texte

                        # la machine abandonne la partie
                        abandonner = True
                        jeu_termine = True



            refresh()

            if afficher_coordonnee_souris: # On affiche les coordonnées de la souris pour les tests
                print(coordonnee_souris())


    if jeu_termine:# si le jeu est fini
        # on affiche le fond et les boutons
        screen.blit(fond, (0, 0))
        screen.blit(bouton_quitte, (screen_x-200, 0))
        screen.blit(bouton_regles, (screen_x-200, screen_y-70))
        nb_manches_jouees += 1

        # si le joeur a gagné ou que la machine a abandonné
        if gagne or abandonner:
            # une manche gagnée par le joueur
            manches_gagnees += 1
            # on affiche le message de victoire
            affichage_gagne = police.render(f'Bravo tu as gagné la manche!!', 1, (255,255,255) )
            # on retire le dernier coup de la machine des gobelets
            gobelets[dernier_coup[0]].remove(dernier_coup[1])
        else :
            # sinon on affiche le message de défaite
            affichage_gagne = police.render(f'Tu as perdu, retente ta chance !!', 1, (255,255,255) )

        # on remet les coups à 0
        dernier_coup = 0
        # on affiche le nombre de manches gagnées par le joeur sur le nombre de manches totales
        affichage_manche = police.render(f"manches gagnées : {manches_gagnees}/{nb_manches_jouees}", 1, (255,255,255) )
        # on affiche le message pour rejouer
        affichage_rejouer1 = police.render(f"Pour rejouer, appuyez sur une", 1, (255,255,255) )
        affichage_rejouer2 = police.render(f"touche ou cliquez sur l'écran", 1, (255,255,255) )

        # si le joueur a gagné la manche mais que la partie n'est pas finie
        if gagne and nb_manches_jouees!=15 and manches_gagnees != 8:
            screen.blit(affichage_gagne,(150, 150))
        # si le joueur n'a pas gagné la manche mais que la partie n'est pas finie
        elif nb_manches_jouees!=15 and manches_gagnees != 8:
            screen.blit(affichage_gagne,(130, 150))
        # si le joueur a gagné la partie
        elif (nb_manches_jouees == 15 and manches_gagnees == 8) or manches_gagnees == 8:
            partie_gagnee = police.render(f"Bravo tu as gagné la partie !", 1, (255,255,255) )
            screen.blit(partie_gagnee,(150, 150))
            # on relance une nouvelle partie
            nb_manches_jouees = 0
            manches_gagnees = 0
        # si le joueur n'a pas gagné la partie
        elif nb_manches_jouees == 15 or nb_manches_jouees-manches_gagnees == 8 :
            partie_gagnee = police.render(f"Tu as perdu la partie !", 1, (255,255,255) )
            screen.blit(partie_gagnee,(220, 150))
            # on relance une nouvelle partie
            nb_manches_jouees = 0
            manches_gagnees = 0

        screen.blit(affichage_manche,(210, 300))
        screen.blit(affichage_rejouer1,(130, 400))
        screen.blit(affichage_rejouer2,(150, 480))
        pygame.display.flip()

        # si on appuie sur une touche on relance le jeu
        attente_de_touche = True
        while attente_de_touche:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    attente_de_touche = False
                    dernière_action = time.time()

                    co = coordonnee_souris()
                    # si il a cliqué sur le bouton quitter
                    if screen_x - 200 <= co[0] <= screen_x and 0 <= co[1] <= 70:
                        pygame.quit()
                        exit()

                if event.type == pygame.QUIT:
                    pygame.quit() #Quitte
                    running = False
                    exit()
        reset()

pygame.quit() #Quitte
