# Gillian Nicole G. Lu, 203063
# March 14, 2022

# I certify that this submission complies with the DISCS Academic Integrity
# Policy.

# If I have discussed my Python language code with anyone other than
# my instructor(s), the extent of each discussion has been clearly 
# noted along with a proper citation in the comments of my program.

# If any Python language code or documentation used in my program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website, or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

################################################################################

# https://www.programiz.com/python-programming/methods/string/isnumeric
# https://www.w3schools.com/python/ref_random_random.asp

################################################################################

# your code goes here


print("LET'S PLAY HANGMAN \n")


import random

#function list

#getting the blanks

def blanks(word):
    blanks = ""
    for letter in word:
        blanks += "-"
    return blanks

# substitute for join/concatenates everything into one string
def combine(letter_list):
    combine = ""
    for letter in letter_list:
        combine = combine + letter
    return combine

#auto-updating

def updatingblanks(guess, secretword, blankslisted):
    x = 0
    for letter in secretword:
        if guess == letter:
            blankslisted[x] = guess
        x += 1
    return [combine(str(item)) for item in blankslisted]

# printing what has not yet been guessed
def is_in_list(guess, unused_letters):
    unused_letters[:] = [letter for letter in unused_letters if letter != guess]
    return unused_letters[:]

# accepting baby letters  
def case_sensitive(guess):
    if guess == "A" or guess == "a":
        return "A"
    elif guess == "B" or guess == "b":
        return "B"
    elif guess == "C" or guess == "c":
        return "C"
    elif guess == "D" or guess == "d":
        return "D"
    elif guess == "E" or guess == "e":
        return "E"
    elif guess == "F" or guess == "f":
        return "F"
    elif guess == "G" or guess == "g":
        return "G"
    elif guess == "H" or guess == "h":
        return "H"
    elif guess == "I" or guess == "i":
        return "I"
    elif guess == "J" or guess == "j":
        return "J"
    elif guess == "K" or guess == "k":
        return "K"
    elif guess == "L" or guess == "l":
        return "L"
    elif guess == "M" or guess == "m":
        return "M"
    elif guess == "N" or guess == "n":
        return "N"
    elif guess == "O" or guess == "o":
        return "O"
    elif guess == "P" or guess == "p":
        return "P"
    elif guess == "Q" or guess == "q":
        return "Q"
    elif guess == "R" or guess == "r":
        return "R"
    elif guess == "S" or guess == "s":
        return "S"
    elif guess == "T" or guess == "t":
        return "T"
    elif guess == "U" or guess == "u":
        return "U"
    elif guess == "V" or guess == "v":
        return "V"
    elif guess == "W" or guess == "w":
        return "W"
    elif guess == "X" or guess == "X":
        return "X"
    elif guess == "Y" or guess == "y":
        return "Y"
    elif guess == "Z" or guess == "z":
        return "Z"
    
        
#finding the clones
def duplicate(guess,used):
    
    for x in used:
        if used.count(x) > 1:
            ans = True
        else:
            ans = False
    return ans
  


#unused * used letters
unused_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
used = []
random_words = ["HELL", "PAIN", "HELP", "COLOSSAL","MIKASA","ATENEO","ANNIE","BRAIN","DAMAGE","GILLIAN","AWESOME"]
play = True
rounds = 0

#main loop
while rounds >= 0:
    sample = 0
    while sample >= 0:
        choose = str(input("Would you like the program to choose a random word?(Yes/No): "))
        
        while choose != "No":
            randomify = int((10*(random.random()))//1 - 1)
            words = random_words[randomify]
            print(f"Here is the word to be guessed by your opponent: {words} \n")
            blankslisted = list(blanks(words))
            guess_limit = len(words) - 1
            guess_count = 0
            guessed = False
            
            
            while not guessed:
                guess = input("\nInput your guess here: ")
                used.append(guess)
                
                if guess.isnumeric():
                    print("Please enter a valid letter \n")
                    print(f"Guess the word: {guess_limit} guess(es) left: {updatingblanks(case_sensitive(guess),words,blankslisted)}")
                
                elif duplicate(guess,used) == True:
                    print("You have already used that letter")
                    
                
                elif guess.isnumeric() == False:
                    print(f"Guess the word: {guess_limit} guess(es) left: {updatingblanks(case_sensitive(guess),words,blankslisted)}")
                    print(f"Unused letters: {combine(is_in_list(case_sensitive(guess), unused_letters))}")
                    guess_limit -= 1
                
                if blankslisted == list(words):
                    print("\nCONGRATULATIONS! YOU WIN!")
                    break
                elif guess_limit < 0 and blankslisted != list(words):
                    print("\nSORRY,YOU ARE HANGED!")
                    break
            used = []
            break
 
        while play and choose != "Yes": 
            secretword = str(input("Please enter a word for the other player to guess: "))
            blankslisted = list(blanks(secretword))
            guess_limit = int(input("Please enter the number of guesses allowed: "))
            guess_limitz = guess_limit - 1
            guessed = False
            while not guessed:
                
                guess = input("\nInput your guess here: ")
                used.append(guess)
                
                if guess.isnumeric() == True:
                    print("Please enter a valid letter \n")
                    print(f"Guess the word: {guess_limitz} guess(es) left: {updatingblanks(case_sensitive(guess), secretword, blankslisted)}")
                    
                elif duplicate(guess,used) == True:
                    print("You have already used that letter")
                
                elif guess.isnumeric() == False:
                    print(f"Guess the word: {guess_limitz} guess(es) left: {updatingblanks(case_sensitive(guess), secretword, blankslisted)}")
                    print(f"Unused letters: {combine(is_in_list(case_sensitive(guess), unused_letters))}")
                    guess_limitz -= 1
                
                if blankslisted == list(secretword):
                    print("\nCONGRATULATIONS! YOU WIN!")
                    break
                elif guess_limitz < 0 and blankslisted != list(secretword):
                    print("\nSORRY, YOU ARE HANGED")
                    break
            break
          
        again = str(input("\nWould you like to play again? (Yes/No) "))        
        if again == "No":
            break
        else:
            continue
        
    
    if again == "No":
        break
    else:
        continue
    
    