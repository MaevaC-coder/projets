# Créé par leou.miltgen, le 10/10/2024 en Python 3.7
# Made by Léou
def QCM(generation_mot, liste_traduction,liste_revision):
    """ röle : générer un QCM de manière aléatoire
        entrer : generation_mot = str , liste_traduction = list() , liste_revision = list()
        retourne : QCM = list()
    """
    QCM = list()                            #créer la liste QCM
    QCM.append(generation_mot)              #l'on ajoute le mot générer dans le QCM
    mot = generation_mot                    #l'on "duplique" le mot générer

    if mot in liste_revision:               #ensuite si le mot générer est bien dans la liste (bien que se soit sur normalement)
        co = liste_revision.index(mot)      #l'on créer une variable avec l'index du mot

    reponse = liste_traduction(co)          #depuis l'index récupérer du mot l'on prend son équivalent traduit
    QCM.append(reponse)                     #l'on ajoute le mot traduit à QCM

    return QCM                              #on renvoie QCM



