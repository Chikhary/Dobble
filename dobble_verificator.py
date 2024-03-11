# Shayan Nicolas Hollet, 20146766
# Yanis Chikhar, 20245598

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

#import os.path

class Verificator():
    def __init__(self):
        pass  

    def verify(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Verification des cartes***")
        
        resultat = []
        file = open(cards_file,"r").readlines()
        for i in range(len(file)):
            carte = file[i].split(" ")
            carte.pop()
            resultat.append(carte)

        order = len(resultat[0]) 
        trueorder = len(set(resultat[0]))
        for i in range(len(resultat)):
            temp1 = set(resultat[i])
            for j in range(i+1,len(resultat)):
                temp2 = set(resultat[j])
                if len(temp1.intersection(temp2)) != 1:
                    return 2
        if order != trueorder:
            return 1
        img = set()
        for i in range(len(resultat)):
            temp1 = set(resultat[i])
            if len(temp1) != trueorder or len(resultat[i]) != len(temp1):
                return 1
            for j in range(len(resultat[i])):
                img.add(resultat[i][j])   
        test = (trueorder-1)**2 + trueorder 
        if len(img) != test or len(resultat) != test:
            return 1
        
        return 0

        
