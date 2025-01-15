exec(open('TestRobot.py').read())

mouvement=[]
for j in range(5):
    for i in range(9-2*j):
        mouvement.append("droite")
    for i in range(9-2*j):
        mouvement.append("bas")
    for i in range(9-2*j):
        mouvement.append("gauche")
    for i in range(9-2*j):
        mouvement.append("haut")
    mouvement.pop()
    mouvement.append("droite")
mouvement.pop()
for i in range(len(mouvement)-1,-1,-1):
    if mouvement[i]=="bas":
        mouvement.append("haut")
    elif mouvement[i]=="haut":
        mouvement.append("bas")
    elif mouvement[i]=="gauche":
        mouvement.append("droite")
    elif mouvement[i]=="droite":
        mouvement.append("gauche")
go(mouvement)
