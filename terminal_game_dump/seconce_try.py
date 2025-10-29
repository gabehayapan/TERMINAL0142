import random
import time
import threading

# List of words for the guessing game
words = ["python", "vim", "terminal", "game", "hangman", "programming"]

# Function to pick a random word
def choose_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to randomly shake the word display
def shake_word(word, guessed_letters):
    while True:
        time.sleep(0.2)  # Shake every 0.2 seconds
        # Randomly replace one of the underscores with a random letter (for the shaking effect)
        shaking_word = list(display_word(word, guessed_letters))
        for i in range(len(shaking_word)):
            if shaking_word[i] == '_':
                if random.random() > 0.7:  # 30% chance to replace an underscore
                    shaking_word[i] = random.choice("abcdefghijklmnopqrstuvwxyz")
        print("Word: " + ''.join(shaking_word), end="\r")  # Overwrite previous line
        if all(letter in guessed_letters for letter in word):  # Stop shaking once the word is guessed
            break

# Game function
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts a player has
    print("Welcome to the Guessing Game!")
    print("Try to guess the word:")
    
    # Start the shaking effect in a separate thread
    shaking_thread = threading.Thread(target=shake_word, args=(word, guessed_letters))
    shaking_thread.daemon = True  # Allow the game to continue when the shaking ends
    shaking_thread.start()

    while attempts > 0:
        print(f"Attempts remaining: {attempts}")
        
        # Show the current state of the word
        current_word = display_word(word, guessed_letters)
        print(f"Word: {current_word}")
        
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

