"""Blackjack main implementation.
Objective is to have a hand value as close to 21 as possible without exceeding it."""
from helpers.deck_functions import load_deck
from helpers.player_functions import Player

DECK = load_deck()

kayo = Player("kayo", DECK)
user = Player("user", DECK)

kayo_hand = kayo.starting_hand()
kayo_score= sum(kayo_hand)
print(f"{kayo_hand} with score {kayo_score}")

def blackjack(player):
    hand = player.hand
    hand_score = sum(hand)

    if hand_score == 21:
        print("Blackjack!")
    if hand_score > 21:
        print("Bust!")
    print(f"Your hand: {hand} with score {hand_score}")
    user_input = input(f"Your score is {hand_score}, do you want to hit or skip?: ").lower()
    if user_input == "hit":
        card = player.hit()
        hand_score = sum(hand)
        print(f"You drew: {card}, score is {hand_score}")
    else:
        print(f"Final hand: {hand} with score {hand_score}")

blackjack(kayo)