exec(open('TestRobot.py').read())

mouvement=[]

for i in range(9): #On répète 9 fois ...
	mouvement.append('bas') #...le mouvement bas ...
	mouvement.append("droite") # ...suivi du mouvement droite.

go(mouvement)
