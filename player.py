class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []
        self.discard_pile = []

    def draw_card(self):
        if not self.deck:
            self.deck, self.discard_pile = self.discard_pile, []
            # Normally you would shuffle the deck here
        if self.deck:
            self.hand.append(self.deck.pop())

    def play_turn(self, supply):
        # Basic turn structure: Draw a card, play actions, buy cards
        self.draw_card()
        print(f"{self.name}'s hand: {', '.join(str(card) for card in self.hand)}")
        # Additional actions would go here
        # Implement buying cards from the supply here

# Further functions can be added to manage the player's actions, hand, deck, etc.
