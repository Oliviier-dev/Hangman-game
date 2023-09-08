#Group members:
# KATUMBA Frank
# BYIRINGIRO Olivier
# MUNEZERO Michel

import random

word_list = ["apple", "dog", "cat", "tree", "house", "book", "sun", "water", "friend", "smile"]
random_word = random.choice(word_list).lower()  # Convert random_word to lowercase
lives = 6
display = []

game_over = False
#print(random_word)

for letter in random_word:
    display += "_"

print(' '.join(display))  # Join the dashes and display as a single string

guessed_letters = []
warnings = 3

while not game_over: # Running the game till game_over = True
    guessed_letter = input("Guess a letter: ").lower()  # Convert guessed_letter to lowercase

    if not guessed_letter.isalpha(): # Checking if the entered guess isn't an alphabet
        if warnings > 0:
            warnings -= 1
            print(f"Invalid input. Please enter a letter. You have {warnings} warning(s) left.")
        else:
            lives -= 1  # Deduct a life when warnings are exhausted
            print("You have no warnings left. You lose a guess.")
        continue

    if guessed_letter in guessed_letters: # Checking if the user tries to enter the guessed word twice
        if warnings > 0:
            warnings -= 1
            print(f"You've already guessed the letter '{guessed_letter}'. Try again. You have {warnings} warning(s) left.")
        else:
            lives -= 1
            print(f"You've already guessed the letter '{guessed_letter}'. You have no warnings left. You lose a guess.")
            print(f"Remaining guesses: {lives}")

            if lives == 0:
                game_over = True
                print("You lose")

        continue

    guessed_letters.append(guessed_letter)

    for position in range(len(random_word)): # Looping all over the random word choosen
        letter = random_word[position]

        if letter == guessed_letter: #Replacing the letetr to the _ if the user got it right
            display[position] = guessed_letter

    remaining_letters = []
    for letter in random_word: #tracking the remaining letters to be guessed
        if letter not in guessed_letters:
            remaining_letters.append(letter)

    print(f"Guessed letters: {' '.join(guessed_letters)}")
    print(' '.join(display))  # Join the displayed word (dashes) and display as a single string