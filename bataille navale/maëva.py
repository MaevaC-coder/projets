# Import des bibliothèques
import math

# Définition des variables globales
pi = math.pi

# ----- Procédure permettant d'afficher x à la puissance y -----
def procédure1(x, y):
    """ rôle : afficher x à la puissance y
        Entrées : x(float), y(float)
        Retourne : string
    """
    exp = math.pow(x,y)
    result = str(x) + " exposant "+ str(y) + " = " + str(exp)
    return result

# ----- Fonction permettant de retourner l'arrondi de x * pi -----
def fonction1(x):
    """ rôle : retourner l'arrondi de x * pi
        Entrées : x(float)
        Retourne : int
    """
    arr = round(x * pi)
    return arr

# ----- Fonction qui retourne les racines carrées de deux réels -----
def racine(a,b):
    """ rôle : retourner
        Entrées : a(float), b(float)
        Retourne : float
    """
    return math.sqrt(a), math.sqrt(b)

# ----- Programme principal -----
a = 2.57
b = 8.36

print(procédure1(a, b))

c = fonction1(b)
print("c = ", c)

a2, b2 = racine(a,b)
print(f"la racine carrée de {a} est {a2} et la racine carrée de {b} est {b2}.")
