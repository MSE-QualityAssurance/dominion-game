class Card:
    def __init__(self, name, cost, card_type):
        self.name = name
        self.cost = cost
        self.card_type = card_type  # 'Action', 'Treasure', 'Victory'

    def __str__(self):
        return f"{self.name} (Cost: {self.cost}, Type: {self.card_type})"

# Add more card types and specific cards here as needed
