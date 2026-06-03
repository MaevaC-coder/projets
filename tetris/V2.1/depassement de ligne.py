# Créé par maeva.cussonneau, le 17/12/2024 en Python 3.7

# Si les coordonnées de la piece tombe sous 0 alors on passe a la piece suivante
if y_piece >= 640:
    # On ajoute 1 au coordonées y de la pièce pour la faire tomber
    pieces_placees.append((current_piece, x_piece, y_piece))

    # Si les coordonnées de la piece sont supérieures à la ligne du haut alors on a un game over
    if y_piece < 0:
        perdu = True
