""""Helper to initialize the player hands."""

class Player:
    """Player class implementation"""

    def __init__(self) -> None:
        self.hand = []

    def score(self) -> int:
        """Return current player score"""
        return sum(self.hand)
