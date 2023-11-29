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

    def buy_card(self, card, supply):
        if card in supply and self.can_afford(card):
            self.discard_pile.append(card)
            supply.remove(card)
            print(f"{self.name} bought {card.name}")
        else:
            print("Cannot buy this card")

    def can_afford(self, card):
        # Simplified: count number of treasure cards in hand
        treasure = sum(c.card_type == "Treasure" for c in self.hand)
        return treasure >= card.cost

    # More functions for actions, playing cards, etc., can be added
