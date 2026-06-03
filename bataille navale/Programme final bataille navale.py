# Créé par nathan.alain, le 01/12/2023 en Python 3.7

import random
# ----- Fonction qui renvoie deux coordonnées distinctes comprises dans
# ----- l'intervalle a1 ... a10 ... j1 ... j10
def positionner():
    """ rôle : renvoyer deux coordonnées distinctes comprises dans l'intervalle
        a1 ... a10 ... j1 ... j10
        Entrée : none
        Retourne : str, str
    """
    alphabet_grille="abcdefghij"

    lettre1=random.randint(0,9)
    chiffre1=random.randint(1,10)

    lettre2=random.randint(0,9)
    chiffre2=random.randint(1,10)

    coord1=alphabet_grille[lettre1]+str(chiffre1)
    coord2=alphabet_grille[lettre2]+str(chiffre2)

    return coord1, coord2

# ----- fonction qui renvoie la plus petite distance entre un bateau et
# ----- une proposition
def distance(bateau1,bateau2,nb_prop):
    """ rôle: renvoie la plus petite distance entre un bateau et une proposition
        entrée : bateau1(str), bateau2(str), nb_prop(str)
        sortie : int
    """
    alphabet_grille="abcdefghij"

    x1=abs(alphabet_grille.index(bateau1[0])-alphabet_grille.index(nb_prop[0]))

    y1=abs(int(bateau1[1:])-int(nb_prop[1:]))

    x2=abs(alphabet_grille.index(bateau2[0])-alphabet_grille.index(nb_prop[0]))

    y2=abs(int(bateau2[1:])-int(nb_prop[1:]))

    if x1==0 and y1==0:

        dist=0

    elif x2==0 and y2==0:

        dist=0

    elif x1==0 and y1==1:

        dist=1

    elif x1==1 and y1==0:

        dist=1

    elif x1==1 and y1==1:

        dist=1

    elif x2==0 and y2==1:

        dist=1

    elif x2==1 and y2==0:

        dist=1

    elif x2==1 and y2==1:

        dist=1

    else:

        dist=2

    return dist
# ----- fonction qui demande une proposition à l'utilisateur et vérifie si
# ----- la proposition est dans l'intervalle de la grille
def proposition():
    """rôle : demande une proposition à l'utilisateur et vérifie si la proposition est dans l'intervalle de la  grille
       entrée : none
       sortie : str
    """
    alphabet_grille="abcdefghij"
    test = 0
    while test == 0:
        proposition = input("Entrer vos coordonnées:")
        if proposition == "":
            test = 0
            print("Les coordonnées ne sont pas bonnes.")
        elif proposition[0] not in alphabet_grille:
            test = 0
            print("Les coordonnées ne sont pas bonnes.")
        elif proposition[1:]!="1":
            if proposition[1:]=="2":
                test=1
            else:
                if proposition[1:]=="3":
                    test=1
                else:
                    if proposition[1:]=="4":
                        test=1
                    else:
                        if proposition[1:]=="5":
                            test=1
                        else:
                            if proposition[1:]=="6":
                                test=1
                            else:
                                if proposition[1:]=="7":
                                    test=1
                                else:
                                    if proposition[1:]=="8":
                                        test=1
                                    else:
                                        if proposition[1:]=="9":
                                            test=1
                                        else:
                                            if proposition[1:]=="10":
                                                test=1
                                            else:
                                                test = 0
                                                print("Les coordonnées ne sont pas bonnes.")

        else:
            test = 1
    return proposition

bateau1, bateau2 = positionner()
coule = ""
compteur = 0
while len(coule) <2:
    nb_prop=proposition()
    compteur = compteur + 1
    if distance(bateau1,bateau2,nb_prop) == 0:
        if nb_prop == bateau1:
            if coule!="1":
                print(f"Bateau coulé en {bateau1}")
                coule = coule + "1"
            else:
                print(f"Bateau déjà coulé")
        if nb_prop == bateau2:
            if coule!="2":
                print(f"Bateau coulé en {bateau2}")
                coule = coule + "2"
            else:
                print(f"Bateau déjà coulé")
    elif distance(bateau1,bateau2,nb_prop) == 1:
        print("En vue")
    else:
        print("A l'eau")
print(f"Bravo vous êtes super fort vous avez gagné en {compteur} tentatives !")





