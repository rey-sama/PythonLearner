exec(open('TestRobot.py').read())

mouvement=[]
for j in range(5): #J parcours les valeurs de 0 à 4
    #(9-2*j) sera égal à 9, puis 7, puis 5, puis 3, puis 1
    for i in range(9-2*j): #On ajoute (9-2*j)...
        mouvement.append("droite") #... le mouvement "droite"
    for i in range(9-2*j): #On ajoute (9-2*j)...
        mouvement.append("bas") #... le mouvement "bas"
    for i in range(9-2*j): #On ajoute (9-2*j)...
        mouvement.append("gauche") #... le mouvement "gauche"
    for i in range(9-2*j): #On ajoute (9-2*j)...
        mouvement.append("haut") #... le mouvement "haut"
    mouvement.pop() #On retite le dernier "haut" en trop pour finir un carré
    mouvement.append("droite") #On se déplace sur la droite pour commencer le nouveau carré plus petit
mouvement.pop() #On retire le dernier mouvement de "droite" qui permettait de commencer le carré suivant car il n'y en a plus

go(mouvement)
