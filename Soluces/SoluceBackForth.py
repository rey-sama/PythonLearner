exec(open('TestRobot.py').read())

mouvement=[]
for j in range(9): #On répète 9 fois...
    mouvement.append("droite") #...l'ajout de la direction "droite".
for j in range(9): #On répète 9 fois...
    mouvement.append("gauche") #...l'ajout de la direction "gauche" pour revenir au départ.

go(mouvement)
