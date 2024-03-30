
#######################################################
# wordle
#########################################################

# This is the "main" portion of your game.
# Any code that uses stdin or stdout (i.e., input() and print())
# should go in this file.

import wordle_engine
import random
import sys


# Print a greeting
print(wordle_engine.welcome_string())

# Load the list of valid words
valid_words = wordle_engine.load_words("combined_wordlist.txt")

# TODO choose a random word from valid_words
wordle_words = wordle_engine.load_words("shuffled_real_wordles.txt")
choice_list = list(wordle_words)  # so that we can have random access
target = random.choice(choice_list)  # chose a new target!

# implementation of the rest of the game
turn = 1  # to keep count of the turns
guess = ""
alphabet_dict = wordle_engine.create_letter_status()  # initializing the alphabet dictionary as all blue
guesses = []  # initializing a list to keep all the guesses in
while turn <= 6:  # making sure that the user has maximum six tries
    # printing the guesses list, the updated alphabet and prompting the user
    guess = input(f"Your guesses: {wordle_engine.print_list_helper(guesses)}\n{wordle_engine.format_letters(alphabet_dict)}\nGuess a word: ").lower()
    # Data Validation -  if the input isn't acceptable skip the rest of the loop instructions
    # so that the guesses list, and the turns count don't become corrupted)
    if len(guess) != 5:  # ensure that length of guess is exactly 5
        print("Please enter a 5 letter word!")
        continue
    if guess not in choice_list:  # ensure that guess is a valid word
        print("not a valid word. Please try again.")
        continue
    if guess == target:  # check if user won (in order to finish and exit)
        # print the guesses, the correct word, and the message "You win!". Then exit.
        print(f'{wordle_engine.print_list_helper(guesses)}\nGood Job! The word was {target}\nYou Win!!!')
        exit()
    wordle_engine.update_letter_status(alphabet_dict, target, guess)  # update the dictionary
    guess = wordle_engine.format_guess(target, guess)  # format guess with the right colors
    if guesses.count(guess) > 0:  # check that user doesn't guess duplicate word (part of data validation)
        print("You already guessed that word")
        continue
    guesses.append(guess)  # add the current guess to the list of guesses
    turn += 1  # Keep count of the turn
# once it's out of the loop... We know that the user lost (otherwise we would have broken out of the loop...)
print(f"Sorry, You Lose.\nThe word was {target}")
