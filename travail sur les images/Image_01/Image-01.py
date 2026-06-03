# bibliothèques utilisées
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def affichage(image) :
##    Décomposition des pixels
    largeur, hauteur = image.size # récupère les dimensions de l'image
    img_copie = np.copy(image) # On fait une copie de l'image originale
    for i in range(hauteur): # on parcours la hauteur de l'image
        for j in range(largeur): # on parcours la largeur de l'image
            r, v, b, a = img_copie[i, j] # on récupère les composantes r,v,b,a de chaque pixel
            print(f"r : {r}, v : {v}, b : {b}, a : {a}")   # on affiche les composantes de chaque pixel

##    affichage de l'image dans une fenêtre
    plt.subplot(1,2,1)
    plt.imshow(image, cmap='gray')
    plt.show()

image = Image.open("Logo NSI.png") # on crée un objet image à partir du fichier logo NSI.png
affichage(image) # on exécute la procédure affichage(image)