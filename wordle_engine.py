
#######################################################
# wordle_engine
#########################################################


# Container for color control codes.
class wordle_colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
wordle_alphabet = "abcdefghijklmnopqrstuvwxyz"

def welcome_string():
    return (
        f"Welcome to {wordle_colors.GREEN}W{wordle_colors.RED}o{wordle_colors.BLUE}r"
        f"{wordle_colors.YELLOW}d{wordle_colors.CYAN}l{wordle_colors.MAGENTA}e{wordle_colors.ENDC}"
    )

def create_letter_status():
    """ Initialize and Return a new dictionary that maps each letter to
        wordle_colors.BLUE """
    blue_alpha = {}  # Initializing the dict
    for letter in wordle_alphabet:  # looping through the alphabet
        blue_alpha[letter] = wordle_colors.BLUE  # adding each letter and the color blue to it
    return blue_alpha

def load_words(filename: str):
    """ Load the words from the specified file and place them
        in a set.
        Ignore any lines that begin with "#"
        """
    # wordles = set(open("sample_word_list.txt").read().splitlines()) - first try

    wordles = set()  # initializing the set
    with open(filename, 'r') as f:  # reading from the file
        for line in f.readlines():
            if line.startswith('#'):  # excluding unwanted lines
                continue
            line = line.strip('\n')
            wordles.add(line)  # adding wanted lines
    return wordles

def format_guess(target, guess):
    """ Return a string that contains the user's guess formatted
        so that each letter is colored
        * GREEN:  The letter is placed correctly.
        * YELLOW: The letter appears in the target word,
                  but in a different location.
        * RED:    The letter does not appear in the target word
        Also, the string should end with wordle_colors.ENDC """
    '''formatted_letters = ""
    for letter, color_code in alphabet_dict.items():
        formatted_letters += f"{color_code}{letter}"
    formatted_letters += f"{wordle_colors.ENDC}"
    return formatted_letters'''
    # My original function

    '''# Check if letters in the word or not.
        for letter in guess:
        if letter in target:
            wordle_alphabet[letter] = wordle_colors.YELLOW
        else:
            wordle_alphabet[letter] = wordle_colors.RED
    # Checks if letters are in the right location
    for i in range(len(guess)):
        if target[i] == guess[i]:
            wordle_alphabet[guess[i]] = wordle_colors.GREEN
    formatted_guess = ""
    for letter in guess:
        formatted_guess += letter
    formatted_guess += f"{wordle_colors.ENDC}"
    return formatted_guess'''


# Redone
    formatted_guess = ""
    for index, letter in enumerate(guess):  # looping through guess while saving both the current letter, and the index
        if letter in target:  # It's a correct letter
            if target[index] == letter:  # If it's in the correct position
                formatted_guess += f"{wordle_colors.GREEN}{letter}"  # add the letter, colored green, to the new string.
            else:  # If it's in the wrong position
                formatted_guess += f"{wordle_colors.YELLOW}{letter}"  # add the letter in Yellow
        else:  # If it's not even in the target word
            formatted_guess += f"{wordle_colors.RED}{letter}"  # add the letter in red
    formatted_guess += f"{wordle_colors.ENDC}"
    return formatted_guess
    # another try
    '''update_letter_status(wordle_alphabet, target, guess)
    formatted_guess = ""
    for letter in guess:
        formatted_guess += wordle_alphabet[letter]
    return formatted_guess'''

def update_letter_status(letter_status: dict, target, guess):
    """ Update the letter status dictionary to show which letters
        have been used and whether they appear in the target word.
        Specifically:
        * BLUE:   Letter has not been used in a guess
        * GREEN:  Letter appears in the correct location in some guess.
        * YELLOW: Letter is in the target word and appears in some guess
                  (but not in the correct location)
        * RED:    Letter does  not appear in the target word, but has
                  been used in at least one guess."""
    for letter in guess:
        if letter in target:  # Check if letters in target or not.
            if letter_status[letter] != wordle_colors.GREEN:  # If the right position's been found already, we don't want to change that.
                letter_status[letter] = wordle_colors.YELLOW  # Change the letter's color to Yellow
        else:  # The letter's not in the target word
            letter_status[letter] = wordle_colors.RED  # Change the letter's color to red
    for i in range(len(guess) - 1):
        if target[i] == guess[i]:   # Checks if letters are in the right location
            letter_status[guess[i]] = wordle_colors.GREEN  # If they are - Change their color to green

def format_letters(alphabet_dict):
    """ Generate a string that lists all the letters of the alphabet
        colored according to the rules given in update_letter_status.
        the string should end with wordle_colors.ENDC """
    formatted_letters = ""
    for letter, color_code in alphabet_dict.items():  # Iterating through the alphabet dict, while saving both the letter and the color.
        formatted_letters += f"{color_code}{letter}"  # Adding the color and the letter
    formatted_letters += f"{wordle_colors.ENDC}"  # Adding the ending for the string
    return formatted_letters

def print_list_helper(formatted_list: list):  # just a little method to help me print the list of guesses
    print_string = ""
    for word in formatted_list:  # looping through the list
        print_string += word + " - "  # adding each guess to the string
    return print_string
