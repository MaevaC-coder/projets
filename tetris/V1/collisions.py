# Créé par maeva.cussonneau, le 12/12/2024 en Python 3.7

# fonction de la classe carre pour les collisions
def collision(self,autres_carres):
    """ rôle : gérer les collisions entre carres
        entrées : self(carre) : le carré qu'on regarde pour voir s'il entre en collision,
                autres_carres(list(carre)) : la liste tous les autres carrés posés avec leurs informations, dont les coordonnées
        sortie : none
    """
    # il n'y a pas encore de collision
    collide=False

    # on prend chaque carré dans toute la liste de carrés déjà posés
    for carre2 in autres_carres:
        # si leur coordonnées se superposent (si elles se touchent)
        if self.rectangle.colliderect(carre2.rectangle) == 1:
            # il y a collision

            collide=True

    # si il y a collision
    if collide:
            #compléter le code pour stopper le carre
