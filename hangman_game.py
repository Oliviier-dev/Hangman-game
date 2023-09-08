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