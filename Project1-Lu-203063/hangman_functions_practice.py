# Hangman Functions Practice (2nd Sem AY 2021-22)

# 1
print('#1')
# a string of blanks (hyphens) equal in length to word
# examples:
    # if word is 'DOG' then to_blanks will return '---'
    # if word is 'HEART' then to_blanks will return '-----'
    # if word is 'PINEAPPLE' then to_blanks return make '---------'
def to_blanks(word):
    pass

print(to_blanks('DOG')) # Expected output: ---
print(to_blanks('HEART')) # Expected output: -----
print(to_blanks('PINEAPPLE')) # Expected output: ---------

# 2
print('\n#2')
# concatenates each letter in a list to form one string
# example: ['A', 'B', 'C'] returns 'ABC'
def combine(letter_list):
    pass

print(combine(['A', 'B', 'C'])) # Expected output: ABC
print(combine(['B', 'A', '-', 'A', '-', 'A'])) # Expected output: BA-A-A

# 3
print('\n#3')
# returns a string where the
# hyphens are replaced with the corresponding letter
# whenever the player inputs a correct letter
# (i.e. a letter that occurs in the word)
# example:
    # the word is 'CHOCOLATE'
    # the player has currently guessed 'CH-C---T-'
    # the player then inputs the letter 'O'
    # this should result in 'CH-C---T-' becoming 'CHOCO--T-'
def update_blanks(current_guess, word_to_guess, entered_letter):
    pass

word = 'CHOCOLATE'
guess = 'CH-C---T-'
user_input = 'O'
print(update_blanks(guess, word, user_input)) # Expected output: CHOCO--T-

word = 'TABLE'
guess = '-----'
user_input = 'B'
print(update_blanks(guess, word, user_input)) # Expected output: --B--

# 4
print('\n#4')
# checks if a letter is in a list
# examples:
    # list is ['A', 'B', 'C'] and player enters letter 'B'
    # then the function returns True
    
    # list is ['A', 'B', 'C'] and player enters letter 'E'
    # then the function returns False
def is_in_list(entered_letter, letter_list):
    pass

letters = ['A', 'B', 'C']
user_input1 = 'A'
user_input2 = 'E'
print(is_in_list(user_input1, letters)) # Expected output: True
print(is_in_list(user_input2, letters)) # Expected output: False

# 5
print('\n#5')
# removes all elements in list equal to to_remove
# example:
    # list is ['A', 'B', 'C'] and player enters letter 'B'
    # then the function returns the list ['A', 'C']
# HINT: Make a new list with the most recently entered letter filtered out
def remove_item(items, to_remove):
    pass

unused_letters = ['A', 'B', 'C', 'E', 'G', 'J', 'K']

user_input = 'G'
unused_letters = remove_item(unused_letters, user_input)
print(unused_letters) # Expected output: ['A', 'B', 'C', 'E', 'J', 'K']

user_input = 'A'
unused_letters = remove(unused_letters, user_input)
print(unused_letters) # Expected output: ['B', 'C', 'E', 'J', 'K']