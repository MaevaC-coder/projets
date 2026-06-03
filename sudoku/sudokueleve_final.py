from tkinter import *
import tkinter.font as font
from tkinter.filedialog import *
import math
from timeit import default_timer
from copy import deepcopy

# fonction permettant de vérifier si le chiffre est dans la ligne
def Testligne(chiffre,ligne,grille1): # Rémy
    """ Description : vérifie si le chiffre est dans la ligne
       Entrées : chiffre (INT) de 1 à 9, ligne (INT) de 1 à 9 et la grille1 (STR)
       Retour : Booléan, VRAI si déjà présent
    """
    result = False
# Variable permettant de créer une boucle.
    for i in range(9):
# Permet de demander si le chiffre est dans la ligne
        if str(chiffre) == grille1[(ligne-1)*9 + i] :
# Permet de dire si le résultat est vrai.
            result = True
# Permet de retourner result.
    return result

def TestColonne(chiffre, colonne, grille1):  #Ethan
    """ Description : vérifie si le chiffre est dans la colonne
       Entrées : chiffre (INT) de 1 à 9, colonne (INT) de 1 à 9 et la grille1 (STR)
       Retour : Booléan, VRAI si déjà présent
    """
    resultat=False  #On donne à la variable qu'elle est tout le temps fausse.
    for ligne in range(9):  #On fait une boucle 9 fois.
        index = colonne - 1 + ligne * 9  #On récupère l'index de la colonne.
        if grille1[index] == str(chiffre):  #On regarde si il y a déjà le chiffre dans la colonne.
            resultat=True   #Si tout marche la variable sera bonne.
    return resultat  #Et donc ici on retourne le résultat.

def TestCarre(chiffre,ligne,colonne,grille1):  # Maëva
    """ Description : vérifie si le chiffre est dans le carré
       Entrées : chiffre (INT) de 1 à 9, ligne (INT) de 1 à 9, colonne (INT) de 1 à 9 et la grille1 (STR)
       Retour : Booléan, VRAI si déjà présent
    """
    resultat_carre = False # Avant le test, le résultat est obligatoirement faux.
    indice_c_carre = (colonne-1)//3*3 # On calcule l'indice de la colonne de départ du carré où on veut poser le chiffre.
    indice_l_carre = (ligne-1)//3*3 # On calcule l'indice de la ligne de départ du carré où on veut poser le chiffre.
    indice_depart_carre = indice_l_carre*9 + indice_c_carre # On calcule l'indice de la case de départ du carré à l'aide des deux indices calculés précedemment.
    for j in range(3): # On répète l'opération qui suit 3 fois.
        if str(chiffre) in grille1[indice_depart_carre:indice_depart_carre+3] : # On vérifie si le chiffre que l'on veut mettre est compris dans la ligne du carré que l'on regarde.
            resultat_carre = True # Si c'est le cas, le résultat vaut True.
        indice_depart_carre += 9 # On ajoute 9 à l'indice de départ du carré pour passer à la ligne suivante.
    return resultat_carre # On retourne le résultat.

def gagner(grille1):
    """ Description : Indique si la grille1 est complète
       Entrées : grille1 (STR)
       Sorties : VRAI si toutes les cases sont pleines
    """
    return "0" not in grille1 # On teste s'il reste des cases vides dans le sudoku.

def sauveFichierTxt():
    """ Description : Sauvegarde dans un fichier texte le sudoku
       Entrées :
       Retour :
    """
    fichier = open("sudoku.txt", "a")
    for i in range (9):
        ligne =''
        for j in range(8,-1,-1):
            ligne =  str(Grille[i][j])+'  '+ligne
        fichier.write(ligne+"\n")
        if (i+1)%3==0:
            fichier.write("\n")
    fichier.close()

def ouvreFichierTxt(nom):
    """ Description : Ouvre un fichier texte contenant un sudoku et crée une liste de valeur
       Entrées : nom du fichier texte
       Retour : liste des valeurs du sudoku
    """
    fichier = open(nom, "r")
    valeur=fichier.read()
    fichier.close()
    valeur = valeur.replace(' ','')
    valeur = valeur.replace('\n','')
    return valeur


def choixfichier():
    """ Description : Choix du fichier texte contenant un sudoku, prépare la grille et l'affiche
       Entrées :
       Retour :
    """
    global valeurs
    nomfichier = askopenfilename(title="Ouvrir votre Sudoku",filetypes=[('txt files','.txt'),('all files','.*')])
    valeurs=ouvreFichierTxt(nomfichier)
    affectergrille(valeurs)
    affichegrille()
    # affiche le nom du fichier
    canvas.create_text(400,590,text=nomfichier,fill='white',font=("arial", 12),tag=('fichier'))
    # active les boutons chiffres
    for i in range(9):
        bouton[i]['state']=ACTIVE
        bouton[i].pack()

# Pour les tests --------------------------------------
Grille =   [[0,0,0,0,5,0,0,0,0],
            [0,2,3,6,0,4,0,8,1],
            [4,0,0,1,0,0,6,0,0],
            [1,6,0,9,0,0,8,5,0],
            [7,0,5,8,0,2,4,0,6],
            [0,4,9,0,0,7,0,3,2],
            [0,0,1,0,0,5,0,0,9],
            [5,9,0,7,0,1,2,4,0],
            [0,0,0,0,9,0,0,0,0]]
###Grille=[[0,0,0,0,0,0,0,0,0] for _ in range(9)]
possibles=deepcopy(Grille)


def initialiserwidget():
    """ Description : Rend les boutons non valise et efface le texte affiché
       Entrées :
       Sorties :
    """
    global chiffre,start,stopchrono
    for i in range(9):
        bouton[i].config(state=DISABLED,bg='SystemButtonFace',disabledforeground='grey')
        bouton[i].pack()
    monTexte.set("                                                                                                                 ")
    texteLabel.pack()
    chiffre=0
    stopchrono=False
    start=0


def affectergrille(valeur):
    """ Description : Place les valeurs dans la grille et crée la liste des possibles
       Entrées : Liste des valeurs
       Sorties :
    """
    global possibbles
    # en mode test
    ##    for i in range(81):
    ##        Grille[i//9][i%9]=int(valeur[i])
    for i in range(9):
        for j in range(9):
            if Grille[i][j]==0:
                possibles[i][j]=['1','2','3','4','5','6','7','8','9']
            else:
                possibles[i][j]=['']
    creepossible()
    supprimepossible()

def creepossible():
    """ Description : Prépare l'affichage des possibles
       Entrées :
       Sorties :
    """
    for i in range(9):
        for j in range(9):
            if Grille[i][j]==0:
                    posx=j*52+172
                    posy=i*58+52
                    for k in range(9):
                        canvas.create_text(posx+(k%3)*15,posy+(k//3)*15,text=possibles[i][j][k],fill='grey',font=("arial", 10),tag=('pos'+str(i)+str(j)+str(k),"possibles"))
    canvas.itemconfigure("possibles",state="hidden")



def supprimepossible():
    """ Description : Supprime les possibles après le positionnement d'un chiffre
       Entrées :
       Sorties :
    """
    for i in range(9):
        for j in range(9):
            if Grille[i][j]!=0:
                for k in range(9):
                    if len(possibles[k][j])>1:
                        possibles[k][j][Grille[i][j]-1]=''
                        canvas.delete('pos'+str(k)+str(j)+str(Grille[i][j]-1))
                    if len(possibles[i][k])>1:
                        possibles[i][k][Grille[i][j]-1]=''
                        canvas.delete('pos'+str(i)+str(k)+str(Grille[i][j]-1))
                xcarre=i//3*3
                ycarre=j//3*3
                for k in range(3):
                    for l in range(3):
                        if len(possibles[k+xcarre][l+ycarre])>1:
                            possibles[k+xcarre][l+ycarre][Grille[i][j]-1]=''
                            canvas.delete('pos'+str(k+xcarre)+str(l+ycarre)+str(Grille[i][j]-1))

    return


def action_chiffre(chif):
    """ Description : Active tous les boutons chiffres et désactive le chiffre choisi
       Entrées : Chiffre choisi
       Sorties :
    """
    global chiffre,start
    if start==0:
        start = default_timer()
        canvas.itemconfigure(text_clock,state="normal")
        updateTime()
    bouton[-chiffre].config(state=ACTIVE,bg='SystemButtonFace')
    bouton[-chiffre].pack()
    bouton[-chif].config(bg='mediumseagreen',disabledforeground='black')
    bouton[-chif].pack()
    bouton[-chif].config(state=DISABLED)
    bouton[-chif].pack()
    chiffre= chif
    monTexte.set('                                                                                                         ')
    texteLabel.pack()
    return


def ligne_colonne(x,y):
    """ Description : Traduit les coordonnées de la souris en ligne et colonne de la grille
       Entrées : Coordonnée du clic
       Sorties : ligne et colonne de la grille
    """
    colonne= (x-164)//52 +1
    ligne= (y-40)//58 +1
    return ligne,colonne


#capture des clics de souris
def action_clic_souris(event):
    """ Description : Traitement après le clic de la souris
       Entrées :
       Sorties :
    """
    global ligne,colonne,stopchrono
    canvas.focus_set()
    x = event.x
    y = event.y
    if chiffre!=0:
        if  x>160 and x<630 and y>40 and y<560:
            ligne,colonne=ligne_colonne(x,y)
            Grillebis=''
            for i in Grille:
                for j in i:
                    Grillebis=Grillebis+str(j)
            # Affichage des erreurs à partir de la variable Grillebis
            if Testligne(chiffre,ligne,Grillebis) or TestColonne(chiffre,colonne,Grillebis) or TestCarre(chiffre,ligne,colonne,Grillebis):      # A modifier
                monTexte.set('                     Ce numéro est impossible dans cette case.                              ')

            # Gestion du clic
            else:
                # Création du chiffre sur la grille
                monTexte.set('                                                                                  ')
                texteLabel.pack()
                posx=(colonne-1)*52+188
                posy=(ligne-1)*58+69
                canvas.create_text(posx,posy,text=str(chiffre),font=f1,tag='chiffresaisi')
                # Efface les possibles de la case sur la grille
                for k in range(9):
                    canvas.delete('pos'+str(ligne-1)+str(colonne-1)+str(k))
                #print('pos'+str(ligne-1)+str(colonne-1)+str(chiffre-1))
                # Affectation du chiffre à la grille
                Grille[ligne-1][colonne-1]=chiffre
                # Efface les possibles de la case dans la liste des possibles
                possibles[ligne-1][colonne-1]=['']
                canvas.pack()
                # Supprime les possibles dans la ligne, la colonne et le carré
                supprimepossible()
                menubar.entryconfigure(3, state=NORMAL)
                # Message si la grille est complète
                Grillebis=''
                for i in Grille:
                    for j in i:
                        Grillebis=Grillebis+str(j)
                if gagner(Grillebis) :
                    stopchrono=True
                    monTexte.set('                  BRAVO ! Vous avez gagner                              ')
                    texteLabel.pack()
        # Message si l'on clique en dehors de la grille
        else:
            monTexte.set('                        Cliquer dans la grille !                             ')
            texteLabel.pack()
    # Message pour indique de choisir un chiffre à placer
    else:
        monTexte.set('                        Il faut choisir un chiffre !                             ')
        texteLabel.pack()
    return


def affichegrille():
    """ Description : Affiche les chiffres sur la grille
       Entrées :
       Sorties :
    """
    canvas.delete('chiffres')
    for i in range(9):
        for j in range(9):
            if Grille[i][j]!=0:
                posx=j*52+188
                posy=i*58+69
                canvas.create_text(posx,posy,text=str(Grille[i][j]),font=f1,tag='chiffres')
    monTexte.set("                         Commencer par choisir un chiffre sur la droite.                                         ")
    texteLabel.pack()
    canvas.pack()

def effacer():
    """ Description : Efface les chiffres sur la grille
       Entrées :
       Sorties :
    """
    canvas.delete("possibles")
    canvas.delete("chiffres")
    canvas.delete("chiffresaisi","fichier")
    canvas.itemconfigure(text_clock,state="hidden")
    initialiserwidget()


def reinitialiser():
    """ Description : Efface les chiffres sur la grille et la réinitialise
       Entrées :
       Sorties :
    """
    canvas.delete('chiffresaisi')
    canvas.delete('possibles')
    canvas.delete(text_clock)
## en mode test
##    affectergrille(valeurs)
    affectergrille(0)
    affichegrille()
    # active les boutons chiffres
    for i in range(9):
        bouton[i]['state']=ACTIVE
        bouton[i].pack()

def annule():
    """ Description : Efface le dernier chiffre sur la grille
       Entrées :
       Sorties :
    """
    dernier = canvas.find_all()[-1]
    if "chiffresaisi" in canvas.gettags(dernier):
        canvas.delete(dernier)
        Grille[ligne-1][colonne-1]=0
 #       menubar.entryconfigure(3, state=DISABLED)

def resoudre():
    return

#fenêtre
stopchrono=False
chiffre=0
start=0
root = Tk()
root.geometry("%dx%d%+d%+d" % (800,660,100,100))
root.config(background='grey')
root.title("Sudoku")




## Affichage de la grille vide
canvas = Canvas(root, width='800', height = '610', background='mediumseagreen')

image = PhotoImage(file='grille vide.png')
item = canvas.create_image(150, 30, image = image,anchor=NW)
f1 = font.Font(family='consolas',size='28')
canvas.pack()

def updateTime():
    if not stopchrono:
        now = default_timer() - start
        minutes, seconds = divmod(now, 60)
        hours, minutes = divmod(minutes, 60)
        str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
        canvas.itemconfigure(text_clock, text=str_time)
        root.after(1000, updateTime)


text_clock = canvas.create_text(40, 20,fill='white',font=("arial", 14))



## Affichage de la zone de texte
cadre=Frame(root,background="grey",borderwidth=3,relief='sunken')
cadre.place(height=160, width=600, x=10, y =550)
cadre.pack()

monTexte=StringVar()
monTexte.set("                                                                                                                 ")
texteLabel = Label(cadre, textvariable = monTexte,font=("arial", 12),background='White',fg='red')
texteLabel.pack()



## Affichage des chiffres à choisir
canvas2 = Canvas(root, width='50', height = '610', background='grey')
button9 = Button(canvas2, width=3, height = 1,text="  9  ",state=DISABLED,command=lambda: action_chiffre(9))
button8 = Button(canvas2, width=3, height = 1,text="  8  ",state=DISABLED,command=lambda: action_chiffre(8))
button7 = Button(canvas2, width=3, height = 1,text="  7  ",state=DISABLED,command=lambda: action_chiffre(7))
button6 = Button(canvas2, width=3, height = 1,text="  6  ",state=DISABLED,command=lambda: action_chiffre(6))
button5 = Button(canvas2, width=3, height = 1,text="  5  ",state=DISABLED,command=lambda: action_chiffre(5))
button4 = Button(canvas2, width=3, height = 1,text="  4  ",state=DISABLED,command=lambda: action_chiffre(4))
button3 = Button(canvas2, width=3, height = 1,text="  3  ",state=DISABLED,command=lambda: action_chiffre(3))
button2 = Button(canvas2, width=3, height = 1,text="  2  ",state=DISABLED,command=lambda: action_chiffre(2))
button1 = Button(canvas2, width=3, height = 1,text="  1  ",state=DISABLED,command=lambda: action_chiffre(1))

bouton = [button9,button8,button7,button6,button5,button4,button3,button2,button1]
f = font.Font(family='calibri',size='24',weight='bold')
for i in range(9):
    bouton[i]['font']=f
    bouton[i].pack()

canvas2.place(height=610, width=50, x=750, y =2)

## créer les menus et  sous-menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command=effacer)
filemenu.add_command(label="Ouvrir", command=choixfichier)
filemenu.add_command(label="Enregistrer", command=sauveFichierTxt)
filemenu.add_command(label="Quitter", command=root.destroy)

posmenu = Menu(menubar,tearoff=0)
posmenu.add_command(label="Afficher", command= lambda: canvas.itemconfigure("possibles",state="normal"))
posmenu.add_command(label="Cacher", command= lambda: canvas.itemconfigure("possibles",state="hidden"))

resolmenu = Menu(menubar,tearoff=0)
resolmenu.add_command(label="Proposition", command=resoudre)
resolmenu.add_command(label="Résoudre", command=resoudre)

menubar.add_cascade(label="Fichier", menu=filemenu)
menubar.add_command(label="Réinitialiser", command=reinitialiser)
menubar.add_command(label="Retour", command=annule)
menubar.add_cascade(label="Possibles", menu=posmenu)
menubar.add_cascade(label="Solution", menu=resolmenu)


# afficher le menu
root.config(menu=menubar)

#association clic-action
canvas.bind("<Button-1>", action_clic_souris)

#Lancement fenêtre
root.mainloop()






