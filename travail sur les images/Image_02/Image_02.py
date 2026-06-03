# bibliothèques utilisées
from PIL import Image # PIL est la bibliothèque spécialisée dans le traitement de l'image
from io import BytesIO # module pour transformer en bytes
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# affiche côte-à-côte l'image originale et l'image transformée
def affichage(img_modif) :
    plt.subplot(1,2,1)
    plt.imshow(image, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(img_modif, cmap='gray')
    plt.show()

# enregistrement de l'image
def sauve_image(img_modif, fichier) :
    img_save = Image.fromarray(img_modif) # reconvertit le tableau de pixels en image
    img_save.save(fichier) # La bibliothèque PIL permet d'enregistrer dans tous les formats classiques d'image

# transforme les pixels en blanc ou en noir
def noir_et_blanc(img_origine):
    img_copie = np.copy(img_origine) # On fait une copie de l'original
    for i in range(hauteur):
        for j in range(largeur):
            r, v, b, a = img_copie[i, j]

##            Transformation des pixels
            if ((int(r)+int(v)+int(b))/3) >= 127:      # si la moyenne des couleurs >= 127 on transforme les pixels en blanc
                r = 255
                v = 255
                b = 255
            else:                       # sinon on transforme les pixels en noir
                r = 0
                v = 0
                b = 0

##            Reconstitution de l'image
            img_copie[i, j] = (r, v, b, a)
    return img_copie

# Garde seulement les pixels rouges dans une image
def rouge(img_origine):
    """ rôle : garder seulement les pixels rouges dans une image
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_r = np.copy(img_origine)
    for k in range(hauteur):
        for l in range(largeur):
            r, v, b, a = img_copie_r[k, l]
            v = 0
            b = 0
            img_copie_r[k, l] = (r, v, b, a)
    return img_copie_r

# Garde seulement les pixels bleus dans une image
def bleu(img_origine):
    """ rôle : garder seulement les pixels bleus dans une image
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_b = np.copy(img_origine)
    for m in range(hauteur):
        for n in range(largeur):
            r, v, b, a = img_copie_b[m, n]
            v = 0
            r = 0
            img_copie_b[m, n] = (r, v, b, a)
    return img_copie_b

# Garde seulement les pixels verts dans une image
def vert(img_origine):
    """ rôle : garder seulement les pixels verts dans une image
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_v = np.copy(img_origine)
    for o in range(hauteur):
        for p in range(largeur):
            r, v, b, a = img_copie_v[o, p]
            b = 0
            r = 0
            img_copie_v[o, p] = (r, v, b, a)
    return img_copie_v

#créé un négatif de l'image d'origine
def negatif(img_origine):
    """ rôle : créer un négatif de l'image d'origine
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_n = np.copy(img_origine)
    for q in range(hauteur):
        for s in range(largeur):
            r, v, b, a = img_copie_n[q, s]
            r = 255 - r
            v = 255 - v
            b = 255 - b
            img_copie_n[q, s] = (r, v, b, a)
    return img_copie_n

#transforme l'image couleur en une image niveau de gris
def gris(img_origine):
    """ rôle : transformer l'image couleur en une image niveau de gris
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_g = np.copy(img_origine)
    for i1 in range(hauteur):
        for j1 in range(largeur):
            r, v, b, a = img_copie_g[i1, j1]
            g = r*0.2125 + v*0.7154 + b*0.0721
            r = g
            v = g
            b = g
            img_copie_g[i1, j1] = (r, v, b, a)
    return img_copie_g

#augmente la luminosité
def plus_lumineuse(img_origine):
    """ rôle : augmenter la luminosité d'une image
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_pl = np.copy(img_origine)
    for w in range(hauteur):
        for x in range(largeur):
            r, v, b, a = img_copie_pl[w, x]
            r = r + 60
            v =  v + 60
            b = b + 60
            if r>255:
                r = 255
            if v>255:
                v = 255
            if b>255:
                b = 255
            img_copie_pl[w, x] = (r, v, b, a)
    return img_copie_pl

#baisse la luminosité
def plus_sombre(img_origine):
    """ rôle : baisser la luminosité d'une image
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_ps = np.copy(img_origine)
    for a1 in range(hauteur):
        for b1 in range(largeur):
            r, v, b, a = img_copie_ps[a1, b1]
            r = r - 60
            v =  v - 60
            b = b - 60
            if r<0:
                r = 0
            if v<0:
                v = 0
            if b<0:
                b = 0
            img_copie_ps[a1, b1] = (r, v, b, a)
    return img_copie_ps

#affiche les pixels vert dans leur couleur d'origine et les autres en gris
def filtre_vert(img_origine):
    """ rôle : afficher les pixels vert dans leur couleur d'origine et les autres en gris
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_fv = np.copy(img_origine)
    for y in range(hauteur):
        for z in range(largeur):
            r, v, b, a = img_copie_fv[y, z]
            if v-b<10 or v-r<10:
                g = r*0.2125 + v*0.7154 + b*0.0721
                r = g
                v = g
                b = g
            img_copie_fv[y, z] = (r, v, b, a)
    return img_copie_fv

#affiche les pixels bleus dans leur couleur d'origine et les autres en gris
def filtre_bleu(img_origine):
    """ rôle : affiche les pixels bleus dans leur couleur d'origine et les autres en gris
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_fb = np.copy(img_origine)
    for c1 in range(hauteur):
        for d1 in range(largeur):
            r, v, b, a = img_copie_fb[c1, d1]
            if b-r<32 or b-v<32:
                g = r*0.2125 + v*0.7154 + b*0.0721
                r = g
                v = g
                b = g
            img_copie_fb[c1, d1] = (r, v, b, a)
    return img_copie_fb

#affiche les pixels rouges dans leur couleur d'origine et les autres en gris
def filtre_rouge(img_origine):
    """ rôle : affiche les pixels rouges dans leur couleur d'origine et les autres en gris
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_fr = np.copy(img_origine)
    for e1 in range(hauteur):
        for f1 in range(largeur):
            r, v, b, a = img_copie_fr[e1, f1]
            if r-v<170 or r-b<10:
                g = r*0.2125 + v*0.7154 + b*0.0721
                r = g
                v = g
                b = g
            img_copie_fr[e1, f1] = (r, v, b, a)
    return img_copie_fr

#affiche les pixels jaunes dans leur couleur d'origine et les autres en gris
def filtre_jaune(img_origine):
    """ rôle : affiche les pixels jaunes dans leur couleur d'origine et les autres en gris
        Entrée : img_origine(img)
        Sortie : img
    """
    img_copie_fj = np.copy(img_origine)
    for g1 in range(hauteur):
        for h1 in range(largeur):
            r, v, b, a = img_copie_fj[g1, h1]
            if r-b<70 or v-b<70:
                g = r*0.2125 + v*0.7154 + b*0.0721
                r = g
                v = g
                b = g
            img_copie_fj[g1, h1] = (r, v, b, a)
    return img_copie_fj

def menu():
    if(combobox.get() == "Noir & Blanc"):
        image_noir_et_blanc = noir_et_blanc(image) # transforme l'image grâce à la fonction "noir_et_blanc()"
        affichage(image_noir_et_blanc) # affiche côte-à-côte l'image originale et l'image transformée
        sauve_image(image_noir_et_blanc, "image_noir_et_blanc.png") # enregistre l'image dans le répertoire courant

    if(combobox.get() == "Rouge"):
        image_rouge = rouge(image)
        affichage(image_rouge)
        sauve_image(image_rouge, "image_rouge.png")

    if(combobox.get() == "Bleu"):
        image_bleu = bleu(image)
        affichage(image_bleu)
        sauve_image(image_bleu, "image_bleu.png")

    if(combobox.get() == "Vert"):
        image_vert = vert(image)
        affichage(image_vert)
        sauve_image(image_vert, "image_vert.png")

    if(combobox.get() == "Négatif"):
        image_negatif = negatif(image)
        affichage(negatif(image))
        sauve_image(image_negatif, "image_negatif.png")

    if(combobox.get() == "Niveau de gris"):
        image_gris = gris(image)
        affichage(gris(image))
        sauve_image(image_gris, "image_gris.png")

    if(combobox.get() == "Plus lumineuse"):
        image_plus_lumineuse = plus_lumineuse(image)
        affichage(plus_lumineuse(image))
        sauve_image(image_plus_lumineuse, "image_plus_lumineuse.png")

    if(combobox.get() == "Plus sombre"):
            image_plus_sombre = plus_sombre(image)
            affichage(plus_sombre(image))
            sauve_image(image_plus_sombre, "image_plus_sombre.png")

    if(combobox.get() == "Filtre vert"):
        image_filtre_vert = filtre_vert(image)
        affichage(filtre_vert(image))
        sauve_image(image_filtre_vert, "image_filtre_vert.png")

    if(combobox.get() == "Filtre bleu"):
        image_filtre_bleu = filtre_bleu(image)
        affichage(filtre_bleu(image))
        sauve_image(image_filtre_bleu, "image_filtre_bleu.png")

    if(combobox.get() == "Filtre rouge"):
        image_filtre_rouge = filtre_rouge(image)
        affichage(filtre_rouge(image))
        sauve_image(image_filtre_rouge, "image_filtre_rouge.png")

    if(combobox.get() == "Filtre jaune"):
        image_filtre_jaune = filtre_jaune(image)
        affichage(filtre_jaune(image))
        sauve_image(image_filtre_jaune, "image_filtre_jaune.png")

    else:
        fenetre.destroy()

image = Image.open("i7.png") # donner le chemin complet si pas dans le même répertoire
# image contient un tableau de quadruplets donnant les valeurs RVBA de chaque pixel
largeur, hauteur = image.size # récupère les dimensions de l'image

fenetre = tk.Tk()
fenetre.title("Micro-projet Images")
fenetre.geometry("%dx%d%+d%+d" % (250,100,(fenetre.winfo_screenwidth()-250)//2,(fenetre.winfo_screenheight()-100)//2)) # Taille et position de la fenetre
label = tk.Label(fenetre,text = "Choisir une action")
label.pack()
combobox = ttk.Combobox(fenetre, values=["Quitter", "Noir & Blanc", "Rouge", "Bleu", "Vert", "Négatif", "Niveau de gris", "Plus lumineuse","Plus sombre" , "Filtre vert", "Filtre bleu", "Filtre rouge", "Filtre jaune"])
combobox.current(0)
combobox.pack()
bouton_ok = tk.Button(fenetre, text='OK', command=menu)
bouton_ok.pack()

fenetre.mainloop()



