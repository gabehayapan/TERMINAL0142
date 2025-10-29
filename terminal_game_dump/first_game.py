import random

# List of words for the guessing game
words = ["python", "vim", "terminal", "game", "hangman", "programming"]

# Function to pick a random word
def choose_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Game function
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts a player has
    print("Welcome to the Guessing Game!")
    print("Try to guess the word:")

    while attempts > 0:
        # Show the current state of the word
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")

        # Take a letter input from the player
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

# Start the game
if __name__ == "__main__":
    play_game()
