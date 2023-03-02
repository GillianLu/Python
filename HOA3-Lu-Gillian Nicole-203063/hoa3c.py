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

def negate(a):
    return -a

def add(a,b):
    return a + b

def maximum(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

x = 0
limit = 1000

while x < limit:
    S = str(input())
    
    if S == "negate":
        a = int(input())
        print(negate(a))
    
    if S == "add":
        a = int(input())
        b = int(input())
        print(add(a,b))
  
    if S == "maximum":
        a = int(input())
        b = int(input())
        c = int(input())
        print(maximum(a,b,c))
    if S == "stop":
        break
print(" ")

        


             
             

    
        
    
    
    


