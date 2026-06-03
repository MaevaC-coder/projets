# Créé par maeva.cussonneau, le 07/11/2024 en Python 3.7
import matplotlib.pyplot as plt
from math import*
import csv

# Fonction d'extraction des scores et du nombre de questions répondues
def lire_fichier_score_csv():
    """ Rôle : Extraire les éléments du fichier tableau_score.csv dans une liste de dictionnaires
        Entrées : None
        Retourne : list[dict]
    """
    resultat = list()

    fichier_csv = open("tableau_score.csv", newline='', encoding='iso-8859-1')  # on ouvre le fichier "url"
    fichier = csv.reader(fichier_csv, delimiter=';')            # on lit le fichier csv
    for ligne in fichier:
        resultat = list()                                       # on crée une liste vide
        resultat.append(ligne[2])                               # on ajoute la moyenne de points sur 20 à la liste
    resultat.pop(0)                                             # on supprime le 1er élément de la liste : les entêtes

    return resultat

# Fonction qui inverse le contenu d'une liste passée en paramètre
def inverse(l):
    """ rôle : inverser le contenu d"une liste passée en paramètre
        Entrées : l(list)
        sortie : list
    """
    j = len(l)
    if j <= 1:
        return l
    else:
        return [l[-1]] + autre_inverse(l[1:-1]) + [l[0]]

moyennes_score = lire_fichier_score_csv()   # on prend toutes les moyennes du fichier csv

if len(moyennes_score) <= 20: # si il y a 20 moyennes enregistrées ou moins
    moyennes_recentes = moyennes_recentes[:] # on prend toutes les moyennes
else: # sinon
    moyennes_recentes = moyennes_score[len(moyennes_score)-20:]  # on prend les 20 moyennes les plus récentes (les dernières enregistrées) car on n'affiche que les 20 moyennes les plus récentes

moyennes_recentes = inverse(moyennes_recentes)  # on inverse le contenu de la liste pour afficher du plus au moins récent

x = [n+1 for n in range(20)] # les valeurs des abscisses
y = [m for m in moyennes_recentes]  # les valeurs des ordonnées

# affichage du graphique de points
plt.scatter(x,y)
plt.show()
