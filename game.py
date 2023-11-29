from card import Card
from player import Player

class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.supply = [Card("Gold", 6, "Treasure"), Card("Silver", 3, "Treasure"), Card("Estate", 2, "Victory")]
        self.initialize_game()

    def initialize_game(self):
        # Initialize players' decks and the supply
        for player in self.players:
            player.deck = [Card("Copper", 0, "Treasure")] * 7 + [Card("Estate", 2, "Victory")] * 3
            # Shuffle each player's deck

    def play_game(self):
        turn = 0
        while not self.is_game_over():
            current_player = self.players[turn % len(self.players)]
            current_player.play_turn(self.supply)
            turn += 1

    def is_game_over(self):
        # Define the game over condition (e.g., a certain number of piles are empty)
        return False

# Additional methods can be added to manage the game state, supply, and victory conditions.
