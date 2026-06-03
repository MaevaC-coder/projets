# Créé par MAEVA.CUSSONNEAU, le 07/12/2023 en Python 3.7
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

def proposition(nb_prop):
    alphabet_grille="abcdefghij"
    test = 0
    while test == 0:
        if nb_prop == "":
            test = 0
        elif nb_prop[0] not in alphabet_grille:
            test = 0
        elif int(nb_prop[1:]) > 10:
            test = 0
        elif int(nb_prop[1:]) < 0:
            test = 0
        else:
            test = 1
    return nb_prop

def distance(bateau1,bateau2,nb_prop):
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


bateau1, bateau2 = positionner()
print(bateau1, bateau2)
tentative=0
touches=0
n_bateau_touches=""

while len(n_bateau_touches)<2:
    tentative+=1
    nb_prop=input("Entrez vos coordonées :")
    if distance(bateau1,bateau2,nb_prop)==0:
        if nb_prop==bateau1:
            if n_bateau_touches!="1":
                print(f"Bateau touché en {nb_prop} !")
                n_bateau_touches=n_bateau_touches+"1"
            else:
                print("Déjà coulé !")
        if nb_prop==bateau2:
            if n_bateau_touches!="2":
                print(f"Bateau touché en {nb_prop} !")
                n_bateau_touches=n_bateau_touches+"2"
            else:
                print("Dgfghéjà coulé !")
    if distance(bateau1,bateau2,nb_prop)==1:
        print("En vue.")
    if distance(bateau1,bateau2,nb_prop)==2:
        print("A l'eau.")

print(f"Bravo vous avez gagné en {tentative} tentatives.")