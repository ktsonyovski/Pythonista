"""Rock paper scissors game againts computer"""
import random

OUTCOMES = {
    ('rock', 'rock') : "It's a draw!",
    ('paper', 'paper') : "It's a draw!",
    ('scissors', 'scissors') : "It's a draw!",
    ('rock', 'scissors') : 'You win!',
    ('paper', 'rock') : 'You win!',
    ('scissors', 'paper') : 'You win!',
    ('rock', 'paper') : 'You lose!',
    ('scissors', 'rock') : 'You lose!',
    ('paper', 'scissors') : 'You lose!'
}

CHOICES = ['rock', 'paper', 'scissors']

def rock_paper_scissors(user_input: str) -> str:
    """
    Plays a round of rock-paper-scissors against the computer.

    Args:
        user_input (str): The player's choice ('rock', 'paper', or 'scissors').

    Returns:
        str: Outcome message including both choices and result.
    """
    user_choice = user_input.lower()
    if user_choice not in CHOICES:
        raise ValueError(f"Invalid input: {user_input}\nPlease choose rock, paper, or scissors!")

    computer_choice = random.choice(CHOICES)
    result = OUTCOMES.get((user_choice, computer_choice))

    return f"The computer chose: {computer_choice}\nYou chose: {user_choice}\n{result}"
