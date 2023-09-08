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