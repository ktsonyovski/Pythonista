""""Helper to initialize the player hands."""
from helpers.deck_functions import get_random_card, draw_two_cards

class Player:

    def __init__(self, player, deck) -> None:
        self.name = player
        self.hand = []
        self.deck = deck

    def starting_hand(self):
        draw_two_cards(self.hand, self.deck)
        return self.hand

    def hit(self):
        card = get_random_card(self.deck)
        self.hand.append(card)
        return card
