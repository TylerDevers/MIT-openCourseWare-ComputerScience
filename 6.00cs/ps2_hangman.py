# 6.00 Problem Set 3
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"
print(WORDLIST_FILENAME)
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0) #opens word.txt and reads, 'r', the file. 0 means unbuffered.
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def hangman():
    #computer selects random word
    word = choose_word(wordlist)
    length  = len(word)
    print ("Hello, I am thinking of a word that is " + str(length) + " letters long.")

    for characters in str(length):
        blank_space = "-"
        print blank_space*length

    number_guesses = 10
    print "You have " + str(number_guesses) + " guesses left"

    avail_letters = "abcdefghijklmnopqrstuvwxyz"
    print "Your available letters are:"
    print avail_letters

    #while guess counter is less than 10
    guess_counter = 10
    guess = ""
    while guess_counter > 0:
        guess = raw_input("What is your guess?")
        #guess = guess.lowercase
        if guess not in word:
            avail_letters.remove(guess)
            guess_counter -= 1
            print "Nope! Try again. You now have {guess_counter} guesses left. Your available letters are:"
            print avail_letters
        else:
            avail_letters.remove(guess)
            guess_counter -= 1
            print "Excellent! You found one! You have {guess_counter} guesses left. Your available letters are:"
            print avail_letters
    print "out of guesses!"
    #if word does not contain -, then you won
    #else if letter guess is in word, replace '-' with guess, and remove letter from avail_letters.
    #increment guess counter
print hangman()
