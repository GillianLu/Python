# Gillian Nicole G. Lu, 203063
# Feb 27,  2022

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


limit = int(input())

count = 0
big = 0
small = 9999999


while count < limit:
    n = int(input()) #5

    if n > big:
        big = n
    
    if n < small:
        small = n    
    count += 1
    
def diff():
    return big - small
    
print("Maximum " + "= " + str(big))
print("Minimum " + "= " + str(small))
print("Range " + "= " + str(diff()))
    

