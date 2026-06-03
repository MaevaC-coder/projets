tour_machine = True
mikado = [1,2,3,4,5,6,7,8]
goblet = {8 : [1,2,3], 7 : [1,2,3],6 : [1,2,3],5 : [1,2,3],4 : [1,2,3],3 : [1,2,3],2 : [1,2,3],1 : [1,2,3]}
deroule = []
coup = 0
print(goblet[len(mikado)][0])
defaite = False

def ia(mikado,goblet,coup):
    deroule = []
    while len(mikado) != 0:
        if tour_machine == True:
            partie.append(goblet[len(mikado)])
            deroule.append(goblet[len(mikado)][0])
            coup = goblet[len(mikado)][0]
    supprimer(deroule,goblet)

def supprimer(deroule,goblet):
    if defaite == True:
        coup = 0
        goblet[partie[len(partie)]][0]
    else:
        coup = 0


