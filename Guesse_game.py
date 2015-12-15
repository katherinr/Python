# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
max_n=7
count=0
high=100
secret_number=0

# helper function to start and restart the game
def new_game():
    global high
    global secret_number
    global count
    count=0
    if (high==100):
        print ""
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is 7"
        secret_number=random.randrange(0,100)
    if (high==1000):
        print ""
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is 10"
        secret_number=random.randrange(0,1000)
    #return secret_number
  
# define event handlers for control panel
def range100():
   # button that changes range to range [0,100) and restarts
    global high
    global max_n
    high=100
    max_n=7
    new_game()
    
def range1000():
    global high
    global max_n
    high=1000
    max_n=10
    new_game()

def input_guess(guess):
    # main game logic goes here	
    global count
    global secret_number
    g=int(guess)
    count=count+1
    n=max_n-count
    print ""
    print "Guess was", g
    print "Number of remaining guesses is", n
    if(count<=max_n):
        if (g>secret_number):
            print "Lower!"
        if (g<secret_number):
            print "Higher!"
        if (g==secret_number):
            print "Correct!"
            new_game()
    else:
        print "You ran out of guesses. Your number was",secret_number
        new_game()

# create frame
frame=simplegui.create_frame("Guesse_Game",200,200)

# register event handlers for control elements
frame.add_button("Range is [0,1000)",range1000, 100)
frame.add_button("Range is [0,100)", range100, 100)
frame.add_input("Input guess",input_guess,100)

new_game()

# call new_game and start frame
frame.start()
