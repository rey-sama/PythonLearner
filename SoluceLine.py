exec(open('TestRobot.py').read())

mouvement=[]

for i in range(9): #On répète 9 fois...
	mouvement.append("droite") #...l'ajout de la direction "droite".

go(mouvement)
