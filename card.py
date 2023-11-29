class Card:
    def __init__(self, name, cost, card_type):
        self.name = name
        self.cost = cost
        self.card_type = card_type  # 'Action', 'Treasure', 'Victory'

    def __str__(self):
        return f"{self.name} (Cost: {self.cost}, Type: {self.card_type})"

# Basic treasure cards
copper = Card("Copper", 0, "Treasure")
silver = Card("Silver", 3, "Treasure")
gold = Card("Gold", 6, "Treasure")

# Basic victory cards
estate = Card("Estate", 2, "Victory")
duchy = Card("Duchy", 5, "Victory")
province = Card("Province", 8, "Victory")

# You can add more cards, especially action cards with special effects
