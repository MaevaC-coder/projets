# Créé par leou.miltgen, le 14/10/2024 en Python 3.7
import random

def QCM_Reponse(QCM,liste_traduction):
    """ rôle :créer les réponses du QCM
        entrer : QCM = la bonne réponse et le mot à trouver ,liste_traduction = liste avec tout les mots
        sortie : liste_reponse = list()
    """

    liste_reponse = ["1","2","3","4"]                               #liste d'une longueur égale au nombre de réponse possible
    r = random.randint(0, 3)                                        #la position de la bonne réponse créer aléatoirement

    for i in liste_reponse:                                         #une boucle avec i qui parcours la liste_reponse
        if i == r:                                                  #si i est égale à la position de la bonne réponse
            liste_reponse.insert(r,QCM[1])                          #on ajoute la bonne réponse dans la position
        else:                                                       #dans le cas ou la position n'est pas celle de la bonne réponse
            mauvais = generation_mot(liste_traduction)              #génère une mauvais réponse
            while mauvais == QCM[1]:                                #tant que par mal chance le mot générer est le même que la bonne réponse
                mauvais = generation_mot(liste_traduction)          #regénère une mauvaise réponse
            liste_reponse.insert(i,mauvais)                         #on ajoute la mauvaise réponse à la valeur i, donc à la position actuel d'où l'on parcours la liste

    return liste_reponse
