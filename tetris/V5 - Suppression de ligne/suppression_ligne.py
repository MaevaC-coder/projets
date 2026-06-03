# Créé par maeva.cussonneau, le 07/01/2025 en Python 3.7

def supprimer_ligne_complete(ecran):
    # Trouver les lignes complètes
    lignes_completes = [i for i in range(len(ecran)) if all(ecran[i])]

    # Supprimer les lignes complètes et ajouter des lignes vides en haut
    for ligne in lignes_completes:
        del ecrane[ligne]
        ecran.insert(0, [0] * len(ecran[0]))

    return len(lignes_completes)

# Exemple d'utilisation
ecran = {
    "E": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
}

lignes_supprimees = supprimer_ligne_complete(ecran)
print(f"Lignes supprimées: {lignes_supprimees}")
print("Nouvelle ecran:")
for ligne in ecran:
    print(ligne)

ajoute_carre_ecran(ecran, piece):