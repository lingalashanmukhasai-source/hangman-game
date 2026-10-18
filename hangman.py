import random
from pathlib import Path

# ==========================================
# HANGMAN GAME
# A terminal-based word guessing game
# ==========================================

MAX_ATTEMPTS = 6

# Locate words.txt in the same directory as this script
WORD_FILE = Path(__file__).with_name("words.txt")

# Built-in fallback words if words.txt is unavailable
FALLBACK_WORDS = [
    "PYTHON",
    "COMPUTER",
    "HANGMAN",
    "DEVELOPER",
    "PROGRAM",
    "KEYBOARD",
    "NETWORK",
    "GITHUB",
    "SOFTWARE",
    "CHALLENGE",
    "DATABASE",
    "ALGORITHM",
    "VARIABLE",
    "FUNCTION",
    "INTERNET",
    "SECURITY",
    "APPLICATION",
]

# ASCII gallows stages: 0 through 6 incorrect guesses
HANGMAN_ART = [
    r"""
     +---+
     |   |
         |
         |
         |
    ========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
    ========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
    ========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
    ========
    """
]


def load_words():
    """Load valid English words from words.txt."""

    try:
        with WORD_FILE.open("r", encoding="utf-8") as file:
            words = [
                line.strip().upper()
                for line in file
                if line.strip().isascii()
                and line.strip().isalpha()
                and len(line.strip()) > 1
            ]

        if words:
            print(f"Word list loaded: {len(words)} words.")
            return words

        print("Warning: words.txt is empty or contains no valid words.")

    except OSError:
        print("Warning: words.txt could not be opened.")

    print("Using the built-in word list instead.")
    return FALLBACK_WORDS.copy()


def display_word(secret_word, guessed_letters):
    """Display correctly guessed letters and mask the others."""

    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def display_game_status(secret_word, guessed_letters, wrong_guesses):
    """Display the current game state."""

    mistakes = len(wrong_guesses)

    print(HANGMAN_ART[mistakes])
    print("Word:", display_word(secret_word, guessed_letters))
    print(f"Incorrect guesses: {mistakes}/{MAX_ATTEMPTS}")
    print(f"Attempts remaining: {MAX_ATTEMPTS - mistakes}")

    all_guesses = guessed_letters | wrong_guesses

    if all_guesses:
        print("Guessed letters:", " ".join(sorted(all_guesses)))
    else:
        print("Guessed letters: None")


def play_hangman():
    """Run one complete Hangman game."""

    words = load_words()
    secret_word = random.choice(words)

    guessed_letters = set()
    wrong_guesses = set()

    print("\n" + "=" * 42)
    print("          WELCOME TO HANGMAN")
    print("=" * 42)
    print("Guess the hidden word one letter at a time.")
    print(f"You can make up to {MAX_ATTEMPTS} incorrect guesses.")
    print("Enter one English letter (A-Z) per turn.")

    while len(wrong_guesses) < MAX_ATTEMPTS:

        display_game_status(
            secret_word,
            guessed_letters,
            wrong_guesses
        )

        guess = input("\nEnter your guess: ").strip().upper()

        # Validate input
        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            print("Invalid input. Please enter one letter from A to Z.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters or guess in wrong_guesses:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        # Process the guess
        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"Correct! '{guess}' is in the word.")
        else:
            wrong_guesses.add(guess)
            print(f"Incorrect! '{guess}' is not in the word.")

        # Check for victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 42)
            print("       CONGRATULATIONS! YOU WIN!")
            print("=" * 42)
            print(HANGMAN_ART[len(wrong_guesses)])
            print("The word was:", secret_word)
            print("Excellent work! You guessed the word.")
            return

    # Display defeat screen
    print(HANGMAN_ART[MAX_ATTEMPTS])
    print("\n" + "=" * 42)
    print("              GAME OVER")
    print("=" * 42)
    print("You have used all six incorrect guesses.")
    print("The correct word was:", secret_word)
    print("Better luck next time!")


def main():
    """Start the game and optionally allow another round."""

    while True:
        play_hangman()

        play_again = input(
            "\nWould you like to play again? (Y/N): "
        ).strip().upper()

        if play_again != "Y":
            print("\nThanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()