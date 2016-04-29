guess = ['a','b','c']
print guess.index('b') # is 1
print guess[1] # is b
print ""

insert = ['2','2','3']
print insert.index('2') #is 1
print insert[1] #is 2

number_to_insert = "2"

# for x in range(len(guess)):
#     print "here is the guess list: {x}.".format(x=guess)
#     print "here is the guess list index: {index}".format(index=insert[:])

#put insert values into guess. if the number to insert is in insert, then change that index value in guess.
for x in guess:
    if number_to_insert in insert:
        guess[insert.index(number_to_insert)] = number_to_insert
        insert[insert.index(number_to_insert)] = "?"

print guess
print insert
