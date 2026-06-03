# Créé par leou.miltgen, le 10/10/2024 en Python 3.7


def compte_score(revision,score):
    """ rôle : prendre la fonction révision et en déduire le nombre de point à enlever ou mettre selon le résultat de cette fonction
        entrer : revision = booléen
        sortie : point = int
    """

    if revision == False:   #si la réponse renvoyé est fausse
        score = score -1    #le score diminue de 1
    else:
        score = score +1    #sinon il augmente

    return score            #retourn le nouveau score apres la réponse donné

