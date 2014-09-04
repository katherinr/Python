# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
import math
def number_to_name(number):
    if(number==0):
        name="rock"
    elif(number==1):
        name="Spock"
    elif(number==2):
        name="paper"
    elif(number==3):
        name="lizard"
    else:
        name="scissors"
    return name
       
def name_to_number(name):
    if(name=="rock"):
       number=0
    elif(name=="Spock"):
       number=1
    elif(name=="paper"):
       number=2
    elif(name=="lizard"):
       number=3
    elif(name=="scissors"):
       number=4
    else:
        return None
    return number
    
def rpsls(name): 
    play_number=name_to_number(name)
    print "Player choses",name
    comp_number=random.randrange(0,4)
    print "Computer choses",number_to_name(comp_number)
    if(play_number-comp_number==0):
      print "Computer and player tie!"
      print
      return None
    dif=(play_number-comp_number) % 5
    if  (dif==1) or (dif==2):
        print "Player wins!"
    elif (dif==3) or (dif==4):
        print "Computer wins!"
    print
            
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



