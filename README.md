# Hangman Game

A terminal-based Hangman game built using Python.

## Features

- Random English word selection
- External word list support
- ASCII gallows with seven visual stages
- Hidden word display
- Letter tracking
- Duplicate guess protection
- Input validation
- Six incorrect attempts
- Victory and defeat screens
- Replay option
- Built-in fallback word list

## Technologies Used

- Python 3
- Random module
- pathlib module
- Python sets and functions

## Project Structure

Hangman_Game/
├── hangman.py
├── words.txt
└── README.md

## Installation

1. Install Python 3.
2. Download or clone this repository.
3. Ensure `hangman.py` and `words.txt` are in the same folder.

## Run the Game

Open a terminal in the project directory and run:

    python hangman.py

On Windows, you can also use:

    py hangman.py

## How to Play

1. The game selects a random word.
2. Enter one letter per turn.
3. Correct guesses reveal letters.
4. Incorrect guesses update the gallows.
5. You have six incorrect guesses.
6. Guess the entire word to win.

## Author

L. Shanmukha Sai
Siddhartha Academy of Higher Education
