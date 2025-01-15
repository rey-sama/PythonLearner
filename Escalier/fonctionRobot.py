def afficheFond(ecran):
    fond = (255,255,255)
    ligne = (0, 0, 0)
    ecran.fill(fond)

    for x in range(0,550,50):
        pygame.draw.line(ecran,ligne, (0, x), (500, x))
        pygame.draw.line(ecran,ligne, (x, 0), (x, 500))

def gauche(persoRect):
    persoRect.x-=50

def droite(persoRect):
    persoRect.x+=50

def haut(persoRect):
    persoRect.y-=50

def bas(persoRect):
    persoRect.y+=50

def bouge(rectPerso,tabMove,i):
    if(i<len(tabMove)):
        move=tabMove[i]
        if(move=="droite"):
            droite(rectPerso)
            return (1,0)
        elif(move=="gauche"):
            gauche(rectPerso)
            return (-1,0)
        elif(move=="haut"):
            haut(rectPerso)
            return (0,-1)
        elif(move=="bas"):
            bas(rectPerso)
            return (0,1)
    return None
