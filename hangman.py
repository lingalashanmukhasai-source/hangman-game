
import random

# Words used in the game
WORDS = [
    "PYTHON", "COMPUTER", "HANGMAN", "DEVELOPER",
    "PROGRAM", "KEYBOARD", "NETWORK", "GITHUB",
    "SOFTWARE", "CHALLENGE", "JAVASCRIPT", "DATABASE"
]

MAX_ATTEMPTS = 6

# ASCII gallows stages: 0 to 6 incorrect guesses
HANGMAN_ART = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]

def display_word(secret_word, guessed_letters):
    """Show guessed letters and mask the remaining letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = set()

    print("\n" + "=" * 35)
    print("       WELCOME TO HANGMAN")
    print("=" * 35)
    print(f"\nYou have {MAX_ATTEMPTS} incorrect guesses available.")

    while len(wrong_guesses) < MAX_ATTEMPTS:
        print(HANGMAN_ART[len(wrong_guesses)])
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Attempts remaining:", MAX_ATTEMPTS - len(wrong_guesses))

        if guessed_letters:
            print("Guessed letters:", " ".join(sorted(guessed_letters)))
        else:
            print("Guessed letters: None")

        guess = input("\nEnter a letter: ").strip().upper()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter one English letter (A-Z).")
            continue

        # Prevent duplicate guesses from costing an attempt
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter. Try another!")
            continue

        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            wrong_guesses.add(guess)
            print("Incorrect guess!")

        # Check for victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 35)
            print("       YOU WIN! CONGRATULATIONS!")
            print("=" * 35)
            print(HANGMAN_ART[len(wrong_guesses)])
            print("The word was:", secret_word)
            print("You guessed the word successfully!")
            return

    # Display defeat screen
    print(HANGMAN_ART[MAX_ATTEMPTS])
    print("\n" + "=" * 35)
    print("          GAME OVER!")
    print("=" * 35)
    print("The word was:", secret_word)
    print("Better luck next time!")

if __name__ == "__main__":
    play_hangman()