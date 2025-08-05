import json
import random

# Constant for the file path to the words JSON file
FILE_PATH = 'hangman/resources/words.json'

def load_words(difficulty):
    """
    Load words from a JSON file.

    The JSON file should have a dictionary structure with difficulty levels ('easy', 'medium', 'hard') as keys,
    and lists of words as values.

    Returns:
        list: List of words for the given difficulty, or None if not found.
    """
    try:
        with open(FILE_PATH, 'r') as file:
            words = json.load(file)
            return words.get(difficulty)
    except FileNotFoundError:
        print(f"Error: The file {FILE_PATH} was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")

def difficulty_level():
    """Prompt user for difficulty level and return it."""

    level = input("Choose difficulty level (easy, medium, hard): ").strip().lower()
    if level == "easy":
        return load_words('easy')
    elif level == "medium":
        return load_words('medium')
    elif level == "hard":
        return load_words('hard')
    else:
        print("Invalid difficulty level. Please try again.")
        return difficulty_level()

def main():
    """Main function to run the Hangman game."""
    words = difficulty_level()

    if not words:
        print("No words available for the selected difficulty. Exiting game.")
        return

    chosen_word = random.choice(words)
    print(f"Word to guess: {'_ ' * len(chosen_word)}")
    
    lives = len(chosen_word)
    print(f"Lives remaining: {lives}")
    
    display_word = ['_'] * len(chosen_word)
    
    guessed_letters = set()

    while lives > 0 and "_" in display_word:
        user_input = input("Enter a letter to guess: ").strip().lower()
        if len(user_input) != 1 or not user_input.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        
        if user_input in chosen_word:
            for index, char in enumerate(chosen_word):
                if char == user_input:
                    display_word[index] = char
            print(f"Good guess! '{user_input}' is in the word.")
        else:
            lives -= 1
            print(f"Incorrect guess! Lives remaining: {lives}")

        if user_input in guessed_letters:
            print(f"You have already guessed '{user_input}'.")
            continue

        guessed_letters.add(user_input)

        print(" ".join(display_word))

    if "_" not in display_word:
        print("You win! The word was:", chosen_word.capitalize())
    else:
        print("Game over! The word was:", chosen_word.capitalize())

if __name__ == "__main__":
    main()
