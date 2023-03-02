# Gillian Nicole G. Lu, 203063
# March 7, 2022

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

test_case = 1
not_reversed = []
reverse = []

num = input().split()

while test_case > 0:
    for x in num:
        not_reversed.append(x)

    starting = len(not_reversed) - 1
    reverse = [not_reversed[x] for x in range(len(not_reversed) - 1, -1, -1)]
    
    if reverse[0] == "0" and not_reversed[0] == "0":
        break
    elif reverse == not_reversed and reverse[0] != str(0) and not_reversed[0] != str(0):
        print("Yes")
    else:
        print("No")
    
    test_case += 1
    not_reversed.clear()
    reverse.clear()
    num = input().split()
    
