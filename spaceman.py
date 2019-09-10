"""
Todos:
print Letters that are yet to be guessed
print out project specs before starting game
tries need to be fixed
tell attempts when guessed wrong
"""


import random
import string
from PIL import Image

img = Image.open("ascii_image.png")

alphabets = list(string.ascii_lowercase)
letters_guessed = []


def load_word():
    """
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns:
           string: The secret word to be used in the spaceman guessing game
    """
    f = open('word.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    """
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    """
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    return set(letters_guessed).issuperset(set(secret_word))
    # Thanks https://stackoverflow.com/questions/3931541/how-to-check-if-all-of-the-following-items-are-in-a-list


def get_guessed_word(secret_word, letters_guessed):
    """
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for
     letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string
         should contain the letter at the correct position.  For letters in the word that the user has not yet guessed,
          shown an _ (underscore) instead.
    """
    
    # TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed
    #  correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    underscore_list = ["_" for _ in range(len(secret_word))]
    for i, j in enumerate(secret_word):
        if j in letters_guessed:
            underscore_list[i] = j
    return " ".join(underscore_list)


def is_guess_in_word(guess, secret_word):
    """
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    """
    # TODO: check if the letter guess is in the secret word
    letters_guessed.append(guess)
    if guess in secret_word:
        return True
    return False


def spaceman(secret_word):
    tries = 1 * len(secret_word)
    """
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    """
    
    # TODO: show the player information about the game according to the project spec
    print("You have to guess a secret word which is {} characters long\none letter at a time. "
          "Only input one alphabet each time and you'll know if the alphabet\n"
          "is present in the words or is not. You have {} attempts".format(tries, tries))
    
    # TODO: Ask the player to guess one letter per round and check that it is only one letter
    keep_going = True
    while keep_going:
        guess = input("Enter an alphabet\n")
        tries -= 1
        if len(guess) != 1 or not guess.isalpha():
            print("Only valid inout is one Alphabet at a time\n")
            continue
        letters_guessed.append(guess)
        # keep_going = False
        
        # TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if guess in secret_word:
            get_guessed_word(secret_word, letters_guessed)
            print(secret_word)
            print("You got that letter right\n {} tries left to guess the rest of the letters".format(tries))
            print(" ".join(letters_guessed))

        elif guess not in secret_word:
            print(secret_word)
            get_guessed_word(secret_word, letters_guessed)
            print("Wrong letter, try again\n{} attempts left".format(tries))
            print("Here are the alphabets you have not guessed")
            letters_to_be_guessed = list(set(alphabets) - set(letters_guessed))
            for i in letters_to_be_guessed:
                print(i, end=" ")
    
    # TODO: show the guessed word so far
        print("The letters you have guessed so far are:")
        print(get_guessed_word(secret_word, letters_guessed))
    
    # TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed):
            print("You won!")
            keep_going = False
        
        elif tries <= 0:
            print("Game Over")
            img.show()
            print("The word was {}, {} chars long".format(secret_word, len(secret_word)))
            keep_going = False


# These function calls that will start the game
# secret_word = load_word()
# spaceman(load_word())

#
# loaded_word = load_word()
# print(loaded_word)
# get_guessed_word(loaded_word, letters_guessed)
# get_guessed_word(loaded_word, letters_guessed)

def play_game():
    spaceman(load_word())
    while True:
        answer = input("Would you like to play again?[Y/N]\n")
        if answer.upper() == 'Y':
            letters_guessed.clear()
            spaceman(load_word())
            continue
        elif answer.upper() == "N":
            break
        else:
            print("Choose either Y/N")
            continue


play_game()


