# Shayan Nicolas Hollet, 20146766
# Yanis Chikhar, 20245598

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image
import random
from math import sqrt, ceil

class Creator():
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size

    def make_cards(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Création des cartes visuelles***")

        for line in open(cards_file, "r").readlines():
            symbols = line.strip().split(" ")
            card_created_successfully = False

            while not card_created_successfully:
                card = Image.new("RGB", (self.pic_size, self.pic_size), "white")
                num_symbols = len(symbols)
                symbols_per_row = ceil(sqrt(num_symbols))
                
                zone_size = (self.pic_size - 2 * self.border_size) // symbols_per_row
                symbol_size = int(zone_size * 0.60)

                positions_ok = True  # Supposition initiale : toutes les positions sont correctes

                for index, symbol in enumerate(symbols):
                    img = Image.open(f"images/{symbol}.png")
                    img = img.resize((symbol_size, symbol_size))
                    img = img.rotate(random.randint(0, 360), expand=1)

                    row = index // symbols_per_row
                    col = index % symbols_per_row
                    x_zone_center = self.border_size + col * zone_size + zone_size // 2
                    y_zone_center = self.border_size + row * zone_size + zone_size // 2

                    x = x_zone_center - img.width // 2
                    y = y_zone_center - img.height // 2

                    # On vérifie si l'image dépasse les bordures de sa zone
                    if x < self.border_size + col * zone_size or \
                       y < self.border_size + row * zone_size or \
                       x + img.width > self.border_size + (col + 1) * zone_size or \
                       y + img.height > self.border_size + (row + 1) * zone_size:
                        positions_ok = False
                        break  # Sortir de la boucle for, car une position invalide a été trouvée

                    card.paste(img, (x, y), img)

                if positions_ok:
                    card_created_successfully = True
                    card.save(f"results/card{symbols[0]}.jpg")
                elif verbose:
                    print("Recommencement de la création de la carte, ajustement nécessaire.")
