# Créé par maeva.cussonneau, le 10/10/2024 en Python 3.7

#Fonction qui demande la traduction et renvoie si l'élève a bon
def revision(mot,dictionnaire):
    """ rôle : demander la traduction du monde à réviser et renvoyer si l'élève a bon
        Entrées : mot(str) : le mot à traduire , dictionnaire(dict) : les mots à réviser avec leur traduction
        sortie : boolean
    """
    # demande la traduction et enregistre la réponse de l'utilisateur
    trad = input("Quelle est la traduction en français ? (sans faute de frappe et sans accent)")
    if trad == dictionnaire[mot]: # si la traduction est bonne on renvoie vrai
        return True
    else: # sinon on renvoie faux
        return False

