# Créé par leou, le 05/05/2025 en Python 3.7
def affiche_tour(variable):

    if tour_humain == True:
        tour_affichage = police_tour.render(f'à ton tour !', 1, (255,255,255) )
        screen.blit(affichage_tour,(715, 500))
    if tour_machine == True:
        tour_affichage = police_tour.render(f'ce n est pas encore ton tour...', 1, (255,255,255) )
        screen.blit(affichage_tour,(715, 500))

