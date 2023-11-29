from card import Card, copper, silver, gold, estate, duchy, province
from player import Player

class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.supply = [copper, silver, gold, estate, duchy, province] * 10  # Simplified supply
        self.initialize_game()

    def initialize_game(self):
        # Initialize players' decks and the supply
        for player in self.players:
            player.deck = [copper] * 7 + [estate] * 3
            # Shuffle each player's deck

    def play_game(self):
        turn = 0
        while not self.is_game_over():
            current_player = self.players[turn % len(self.players)]
            current_player.play_turn(self.supply)
            self.player_turn_actions(current_player)
            turn += 1

    def player_turn_actions(self, player):
        # Example: Player can buy a card
        print("Available cards to buy: ", ', '.join(str(card) for card in self.supply))
        buy_choice = input(f"{player.name}, choose a card to buy or type 'skip': ")
        if buy_choice.lower() != 'skip':
            chosen_card = next((card for card in self.supply if card.name.lower() == buy_choice.lower()), None)
            if chosen_card:
                player.buy_card(chosen_card, self.supply)

    def is_game_over(self):
        # Define the game over condition (e.g., a certain number of piles are empty)
        return False

# Additional methods can be added to manage the game state, supply, and victory conditions.
