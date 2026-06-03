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

    while coord1==coord2:
        lettre1=random.randint(0,9)
        chiffre1=random.randint(1,10)

        lettre2=random.randint(0,9)
        chiffre2=random.randint(1,10)

        coord1=alphabet_grille[lettre1]+str(chiffre1)
        coord2=alphabet_grille[lettre2]+str(chiffre2)

    return coord1, coord2

def proposition():
    alphabet_grille="abcdefghij"
    test = 0
    while test == 0:
        proposition = input("Entrer vos coordonnées:")
        if proposition == "":
            test = 0
        elif proposition[0] not in alphabet_grille:
            test = 0
        elif int(proposition[1:]) > 10:
            test = 0
        elif int(proposition[1:]) < 0:
            test = 0
        else:
            test = 1
    return proposition

# ---- Programme principal -----

bateau1, bateau2 = positionner()
print(bateau1, bateau2)
tentative=0
bateau_touches=""

def distance(bateau1,bateau2,proposition):
    if proposition()==bateau1:
        dist=0
    elif proposition()==bateau2:
        dist=0

    elif proposition[0]==bateau1[0] and alphabet.index(proposition[:1])==alphabet.index(bateau1[:1])+1:
        dist=1
    elif proposition[0]==bateau1[0] and alphabet.index(proposition[:1])+1==alphabet.index(bateau1[:1]):
        dist=1

    elif int(proposition[0])+1==int(bateau1[0]) and proposition[:1]==bateau1[:1]:
        dist=1
    elif int(proposition[0])==int(bateau1[0])+1 and proposition[:1]==bateau1[:1]:
        dist=1

    elif int(proposition[0])==int(bateau1[0])+1 and alphabet.index(proposition[:1])==alphabet.index(bateau1[:1])+1:
        dist=1
    elif int(proposition[0])==int(bateau1[0])+1 and alphabet.index(proposition[:1])+1==alphabet.index(bateau1[:1]):
        dist=1
    elif int(proposition[0])+1==int(bateau1[0]) and alphabet.index(proposition[:1])==alphabet.index(bateau1[:1])+1:
        dist=1
    elif int(proposition[0])+1==int(bateau1[0]) and alphabet.index(proposition[:1])+1==alphabet.index(bateau1[:1]):
        dist=1


    elif proposition[0]==bateau2[0] and alphabet.index(proposition[:1])==alphabet.index(bateau2[:1])+1:
        dist=1
    elif proposition[0]==bateau2[0] and alphabet.index(proposition[:1])+1==alphabet.index(bateau2[:1]):
        dist=1

    elif int(proposition[0])+1==int(bateau2[0]) and proposition[:1]==bateau2[:1]:
        dist=1
    elif int(proposition[0])==int(bateau2[0])+1 and proposition[:1]==bateau2[:1]:
        dist=1

    elif int(proposition[0])==int(bateau2[0])+1 and alphabet.index(proposition[:1])==alphabet.index(bateau2[:1])+1:
        dist=1
    elif int(proposition[0])==int(bateau2[0])+1 and alphabet.index(proposition[:1])+1==alphabet.index(bateau2[:1]):
        dist=1
    elif int(proposition[0])+1==int(bateau2[0]) and alphabet.index(proposition[:1])==alphabet.index(bateau2[:1])+1:
        dist=1
    elif int(proposition[0])+1==int(bateau2[0]) and alphabet.index(proposition[:1])+1==alphabet.index(bateau2[:1]):
        dist=1


    else:
        dist=2
    return dist


while len(bateau_touches) != 2:
    tentative+=1
    nb_propose=proposition()
    if distance(bateau1,bateau2,proposition)==0:
        if bateau_touches!="1":
            if nb_propose==bateau1:
                bateau_touches+="1"
                print(f"Bateau touché en {bateau1} !")
        if bateau_touches!="2":
            if nb_propose==bateau2:
                bateau_touches+="2"
                print("Bateau touché en {bateau2} !")
    if distance(bateau1,bateau2,proposition)==1:
        print("En vue !")
    if distance(bateau1,bateau2,proposition)==2:
        print("A l'eau !")

print(len(bateau_touches))
print(f"Bravo vous avez gagné en {tentative} tentatives.")