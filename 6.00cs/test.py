guess = list(raw_input("give me the word: "))
print guess
#guess = guess.split() #split method turns it into a list.
guess_list = list(guess)
print guess_list
print len(guess_list)
joined = ''.join(guess_list)
print joined
