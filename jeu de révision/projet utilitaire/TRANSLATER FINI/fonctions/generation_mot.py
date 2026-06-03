# Créé par leou.miltgen, le 07/10/2024 en Python 3.7
import random

def generation_mot(dictionnaire):
    """rôle :choisir et générer le mot à réviser parmis la liste de mot disponible
       entrer : dicitonnaire = list()
       sortie : dictionnaire = str
    """

    i = random.randint(0, 251)      #génére un nombre aléatoire entre 0 et 251
    return dictionnaire[i]          #renvoie un mot grace à la valeur donné par i





