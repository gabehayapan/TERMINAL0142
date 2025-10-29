import random
import time
import threading
import sys

# List of words for the guessing game
words = ["python", "vim", "terminal", "game", "hangman", "programming"]

# Function to pick a random word
def choose_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to randomly shake the word display
def shake_word(word, guessed_letters, stop_event):
    while not stop_event.is_set():
        time.sleep(0.2)  # Shake every 0.2 seconds
        shaking_word = list(display_word(word, guessed_letters))
        for i in range(len(shaking_word)):
            if shaking_word[i] == '_':
                if random.random() > 0.7:  # 30% chance to replace an underscore
                    shaking_word[i] = random.choice("abcdefghijklmnopqrstuvwxyz")
        sys.stdout.write(f"\rWord: {''.join(shaking_word)}")
        sys.stdout.flush()  # Force the output to update immediately
        if all(letter in guessed_letters for letter in word):  # Stop shaking once the word is guessed
            break

# Timer function to track 3 minutes and print "Ramen nobityau!!!"
def timer_function(start_time, time_limit):
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("\nRamen nobityau!!! Time's up!")
            break
        time.sleep(1)  # Check every second to reduce unnecessary CPU usage

# Game function
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts a player has
    start_time = time.time()  # Record the starting time
    time_limit = 180  # 3 minutes (180 seconds)
    stop_event = threading.Event()  # This will signal the shaking thread to stop
    print("Welcome to the Guessing Game!")
    print("Try to guess the word:")
    
    # Start the shaking effect in a separate thread
    shaking_thread = threading.Thread(target=shake_word, args=(word, guessed_letters, stop_event))
    shaking_thread.daemon = True  # Allow the game to continue when the shaking ends
    shaking_thread.start()

    # Start the timer in a separate thread to track the 3-minute limit
    timer_thread = threading.Thread(target=timer_function, args=(start_time, time_limit))
    timer_thread.daemon = True  # This thread can run in the background without blocking the game
    timer_thread.start()

    while attempts > 0:
        # Show the current state of the word
        current_word = display_word(word, guessed_letters)
        
        print(f"\nWord: {current_word}")
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
        if not all(letter in guessed_letters for letter in word):
            print(f"Game over! The word was: {word}")

    # Stop the shaking thread when the game ends
    stop_event.set()

# Start the game
if __name__ == "__main__":
    play_game()

