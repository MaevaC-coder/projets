# Créé par maeva.cussonneau, le 07/10/2024 en Python 3.7

# Fonction qui créé un dictionnaire de mots : la clé est le mot en français et la valeur associée est la traduction en anglais
def dictionnaire_langue(fra,ang):
    """ rôle : créer  un dictionnaire de mots français-anglais pour réviser
        Entrées : fra(list(str)) : la liste des mots en français
                  ang(list(str)) : la liste des mots en anglais
        Sortie : dict
    """
    # on crée le dictionnaire
    dictionnaire = {}
    # pour chaque mot français on associe sa traduction anglaise : le mot français est la clé et le mot anglais la valeur
    for i in range(len(fra)):
        dictionnaire[fra[i]] = ang[i]
    return dictionnaire # on retourne le dictionnaire
