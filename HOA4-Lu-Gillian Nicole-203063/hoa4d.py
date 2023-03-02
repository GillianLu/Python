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

case = 1
start = 0
new = []
n = int(input())

while case > 0:
    if n == -1:
        break
    
    while n > start:
        word = input()
        new.append(word)
        n -= 1
        starting = len(new) - 1
        reversed_list = [new[x] for x in range(len(new) - 1, -1, -1)]
        
    print("Case " + str(case) + ":")
    for x in reversed_list:
        print(x)
        
    case += 1
    new.clear()
    reversed_list.clear()
    n = int(input())
    
    
    
  
    
        
    
        
        
    
    
    

