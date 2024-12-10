# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random

# Hangman stages
Hangman = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
 =========''']

# Word list and random selection
word_list = ["caprioara", "catel", "rechin", "elefant"]
cuvant_random = random.choice(word_list)
print(cuvant_random)

# Placeholder and initial settings
placeholder = "_" * len(cuvant_random)
lives = 6
game_over = False

# Main game loop
while not game_over:
    print(placeholder)
    alegere_litera = input("Guess a letter: ").lower()

    if alegere_litera in cuvant_random:
        # Update placeholder with guessed letter
        for index in range(len(cuvant_random)):
            if cuvant_random[index] == alegere_litera:
                placeholder = placeholder[:index] + alegere_litera + placeholder[index + 1:]
    else:
        lives -= 1
        print(Hangman[lives])

    # Check for game end conditions
    if "_" not in placeholder:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print("You lose! The word was:", cuvant_random)










