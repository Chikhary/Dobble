

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

from collections import deque
import random # pour le melange des symboles sur chaque carte # for mixing symbols on each card

class Generator():
    def __init__(self, order = 7):
        self.order = order

    def generate_dobble(self):
        n = self.order
        count = 0
        total_symbols = n**2 + n + 1
        symbols = deque(range(1, total_symbols + 1))
        
        matrix = [[[] for _ in range(n)] for _ in range(n)]
        horizon = [[] for _ in range(n + 1)]

        # Insertion des symboles horizontalement, ligne par ligne
        for row in range(n):
            elem = symbols.popleft()
            for col in range(n):
                matrix[row][col].append(elem)
            horizon[count].append(elem)
        count += 1

        # Insertion des symboles en diagonale, ligne par ligne
        for bond in range(n-1):
            for col in range(n):
                elem = symbols.popleft()
                for i in range(n):
                    row = i % n if bond == 0 else ((bond+1) * i) % n
                    newCol = (col + i) % n
                    matrix[row][newCol].append(elem)
                horizon[count].append(elem)
            count += 1

        # Insertion des symboles verticalement, colonne par colonne
        for col in range(n):
            elem = symbols.popleft()
            for row in range(n):
                matrix[row][col].append(elem)
            horizon[count].append(elem)

        # Ajouter le dernier symbole a toutes les cartes de l'horizon
        last_symbol = symbols.pop()
        for card in horizon:
            card.append(last_symbol)

        return matrix, horizon, symbols

    def generate(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Generation des cartes***")

        matrix, horizon, symbols = self.generate_dobble()

        # melange aleatoire des symboles sur les cartes,
        # pour ne pas avoir des répétitions de symboles sur les mêmes endroits des cartes
        # random mixing of symbols on the cards,
        # so as not to have repetitions of symbols on the same places on the cards
        
        for row in matrix:
            for card in row:
                random.shuffle(card)
        for card in horizon:
            random.shuffle(card)

        # ecriture des cartes dans le fichier cards_file
        # writing cards in the cards_file file
            
        with open(cards_file, 'w') as file:
            for row in matrix:
                for card in row:
                    file.write(' '.join(map(str, card)) + ' \n')
            for card in horizon:
                file.write(' '.join(map(str, card)) + ' \n')

        if verbose:
            print(f"Cards have been written to {cards_file}")