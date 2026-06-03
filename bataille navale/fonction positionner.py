# Créé par maeva.cussonneau, le 01/12/2023 en Python 3.7

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

bateau1, bateau2 = positionner()

print(bateau1,bateau2)
