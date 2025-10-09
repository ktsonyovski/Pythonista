"""Helper method to get the deck of cards"""
import json
import random
from pathlib import Path

def load_deck() -> dict:
    """Load deck from JSON file with robust path resolution."""
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    deck_path = script_dir.parent / "resources" / "deck.json"

    try:
        with open(deck_path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found at {deck_path}") from exc

def get_random_card(card_deck):
    """Get a random card name and its value from a deck."""
    card = random.choice(list(card_deck.values()))
    return card

def draw_two_cards(hand: list, card_deck):
    """Draw two cards"""
    for _ in range(2):
        card = get_random_card(card_deck)
        hand.append(card)
    return hand
