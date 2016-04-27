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
    word_list = list(word)
    missing_letters = '-'*length
    letters_list = list(missing_letters)
    print ("Hello, I am thinking of a word that is " + str(length) + " letters long.")
    print missing_letters

    number_guesses = 10
    print "You have " + str(number_guesses) + " guesses left"

    letters = "abcdefghijklmnopqrstuvwxyz"
    avail_letters = list(letters)
    print "Your available letters are:"
    print letters

    #while guess counter is less than 10
    guess_counter = 10
    guess = ""
    while guess_counter > 0:
        guess = raw_input("What is your guess?")
        guess = guess.lower()
        #use list() to split the word into a list of characters.
        #iterate over the list when word guesses are made.
        if guess not in avail_letters:
            print "You have either used that letter already, or chosen a character that is not allowed."
        elif guess not in word:
            avail_letters.remove(guess)
            guess_counter -= 1
            print "Nope! Try again. You now have {guess_counter} guesses left. Your available letters are:".format(guess_counter=guess_counter)
            print ''.join(avail_letters)
            print missing_letters
        else:
            avail_letters.remove(guess)
            guess_counter -= 1
            print "Excellent! You found one! You have {guess_counter} guesses left. Your available letters are:".format(guess_counter=guess_counter)
            print ''.join(avail_letters)
            for l in letters_list:
                index = word_list.index(guess)
                letters_list[index] = guess
                missing_letters.join(letters_list) 
            print missing_letters

    print "out of guesses!"
    #if word does not contain -, then you won
    #else if letter guess is in word, replace '-' with guess, and remove letter from avail_letters.
    #increment guess counter
print hangman()

"""random pick of word, request letter guess, if guess is in word remove guess from avail_letters and add it to print out of word. Will probably need ot convert guess and avail_letters to list to iterate over them, then .join them together. Need to print out dashes instead of the word to mimic a missing word, then replace those dashes with the correct letter guess. Perhaps make a list of dashes that can be iterated over to replace the dashes using the index"""
#next up, print blank spaces at each iteration, replace blank spaces with the correctly guessed letters.
