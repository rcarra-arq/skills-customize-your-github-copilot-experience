
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python that practices string handling, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Game Setup

#### Description

Create the Hangman game structure by selecting a random secret word and displaying its hidden form to the player.

#### Requirements
Completed program should:

- Use a predefined list of secret words.
- Choose a random word from the list.
- Display the word as underscores for each unknown letter.
- Show the current puzzle state after each guess.

### 🛠️ Guess Handling

#### Description

Allow the player to enter letter guesses, update the puzzle display, and keep track of guessed letters.

#### Requirements
Completed program should:

- Accept one-letter guesses from the user.
- Reveal correct letters in the puzzle when guessed.
- Ignore repeated guesses and continue the game.
- Maintain a list of letters already guessed.

### 🛠️ Attempts and Game Ending

#### Description

Track wrong guesses, limit attempts, and finish the game with a win or loss message.

#### Requirements
Completed program should:

- Count incorrect guesses and reduce remaining attempts.
- End the game when the word is fully revealed or attempts run out.
- Display a clear win message when the player guesses the word.
- Display a loss message and reveal the secret word if attempts are exhausted.
