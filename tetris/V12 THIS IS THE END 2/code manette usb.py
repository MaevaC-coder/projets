# Créé par MAEVA.CUSSONNEAU, le 15/05/2025 en Python 3.7

# déplacements pour la manette

# initialisation du module joystick
pygame.joystick.init()

# nombre de manettes connectées
nb_manettes = pygame.joystick.get_count()
# on affiche le nombre de manettes connectées pour les tests
print("nb manettes = ",nb_manettes)
# si une manette ou plus est connectée, on initialise la première pour jouer
if nb_manettes >= 1:
    manette1 = pygame.joystick.Joystick(0)
    manette1.init()


# déplacements pour la manette ( à mettre dans la boucle running)
            # récupérer les  deux axes du joystick de gauche
            axe_x = manette1.get_axis(0) # horizontal
            axe_y = manette1.get_axis(1) # vertical

            #print("axe x",axe_x,"axe y",axe_y) # vérifier que le changement de manette est détecté

            # détection des boutons
            bouton1 = manette1.get_button(0)

            # détection croix directionnelle
            croix = manette1.get_hat(0) # résultats sous forme (0,0)

            if time.time() - dernier_deplacement > delai_deplacement:

                if bouton1:
                    print("bouton 1 appuyé")
                    bouton1 = False
                    dernier_deplacement = time.time()


            bouton2 = manette1.get_button(1)

            if time.time() - dernier_deplacement > delai_deplacement:
                if bouton2:
                    print("bouton 2 appuyé")
                    bouton2 = False
                    dernier_deplacement = time.time()


            bouton3 = manette1.get_button(2)

            if time.time() - dernier_deplacement > delai_deplacement:
                if bouton3:
                    print("bouton 3 appuyé")
                    bouton3 = False
                    dernier_deplacement = time.time()


            bouton4 = manette1.get_button(3)

            if time.time() - dernier_deplacement > delai_deplacement:
                if bouton4:
                    print("bouton 4 appuyé")
                    bouton4 = False
                    dernier_deplacement = time.time()

