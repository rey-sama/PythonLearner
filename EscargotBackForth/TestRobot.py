import sys, pygame
from pygame.locals import*
import time

largeur = 501
hauteur = 501

colorRed=[]
colorGreen=[(0,0),(4,5)]

exec(open('fonctionRobot.py').read())

def go(mouvement):
    pygame.init()
    ecran=pygame.display.set_mode((largeur,hauteur))
    persoImg = pygame.image.load("Perso.png").convert_alpha()
    persoRect=persoImg.get_rect()

    afficheFond(ecran)    
    
    numMouvement = 0

    pos=[0,0]
    
    pygame.display.flip()
    while True:
        afficheFond(ecran)
        for tupleC in colorGreen:
            ecran.fill((0,255,0), (tupleC[0]*50+1, tupleC[1]*50+1,49,49))
        for tupleC in colorRed:
            ecran.fill((255,0,0), (tupleC[0]*50+1, tupleC[1]*50+1,49,49))
        ecran.blit(persoImg,persoRect)
        pygame.display.flip()
        time.sleep(0.4)

        resultMove = bouge(persoRect,mouvement,numMouvement)
        if resultMove is not None:
            pos[0]+=resultMove[0]
            pos[1]+=resultMove[1]
            coord=(pos[0],pos[1])
            if (coord not in colorGreen) and (coord not in colorRed):
                colorGreen.append(coord)
            elif (coord not in colorRed):
                colorRed.append(coord)
                colorGreen.remove(coord)
            else:
                colorRed.remove(coord)
        
        numMouvement+=1
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

