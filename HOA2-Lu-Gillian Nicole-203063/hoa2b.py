# Gillian Nicole G. Lu, 203063
# February 15, 2022

# I/we certify that this submission complies with the DISCS Academic Integrity
# Policy.

# If I/we have discussed my/our Python language code with anyone other than
# my/our instructor(s), my/our groupmate(s), the teaching assistant(s),
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my/our program.

# If any Python language code or documentation used in my/our program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website, or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

################################################################################

# cite your sources here, if any

################################################################################

# your python code starts here

grade = int(input())

while grade != -1:
    if 92 <= grade <= 100:
        print("A")
    elif 87 <= grade <= 91:
        print("B+")  
    elif 83 <= grade <= 86:
        print("B")
    elif 79 <= grade <= 82:
        print("C+")
    elif 75 <= grade <= 78:
        print("C")
    elif 70 <= grade <= 74:
        print("D")
    else:
        print("F")
    grade = int(input())




    
