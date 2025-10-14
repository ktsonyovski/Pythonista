"""Helper method to get the deck of cards"""
import json
import random
from pathlib import Path

class Deck:
    """Deck initialization class"""
    def __init__(self, deck: str) -> None:
        self.deck = self.load_deck(deck)

    def load_deck(self, deck) -> list:
        """Load deck from JSON file and return a list of card values."""
        script_dir = Path(__file__).parent
        decks_path = script_dir.parent / "resources" / "decks.json"

        try:
            with open(decks_path, encoding="utf-8") as file:
                return json.load(file)[deck]
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"File not found at {decks_path}") from exc

    def deal_card(self) -> int:
        """Get a random card from a deck."""
        card = random.choice(self.deck)
        return card

    def shuffle_deck(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)
        return self.deck
