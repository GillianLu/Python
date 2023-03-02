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


x = 0
limit = 999999

while x < limit:
    artist = str(input())
    if artist == "stop":
        break
    food = str(input())
    if food == "stop":
        break
    emotion = str(input())
    if emotion == "stop":
        break
    name = str(input())
    if name == "stop":
        break
    organ = str(input())
    if organ == "stop":
        break
    song = str(input())
    if song == "stop":
        break
    
    def create_story(artist,food, emotion, name, organ, song): 
        print()
        print("The Majestic " + artist)
        print()
        print("Once upon a time, in a far away kingdom, there lived a ruler known as The Majestic " + artist + ".")
        print("Beloved by all the people, The Majestic " + artist + " was quite unique, always wearing a")
        print("crown made of " + food + " and " + emotion + ".")
        print()
        print("But one day, the evil villain " + name + " broke into the palace to kidnap The Majestic " + artist + ".")
        print("Thankfully, the beloved ruler was skilled in the martial arts. One swift kick to " + name + "'s")
        print(organ + " sent the evildoer flying across the room yelling " + song + "!")
        print()
        print("The end.")
        return " " 
        
        
    print(create_story(artist,food, emotion, name, organ, song))
    
    x += 1
    
    
    
    
    