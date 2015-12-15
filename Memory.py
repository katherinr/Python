# implementation of card game - Memory

import simplegui
import random
index1=-1
index2=-1
state=0
cards=[]
counter=0
exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# helper function to initialize globals
def new_game():
    global cards,state,exposed,counter
    state=0
    counter=0
    exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    label.set_text("Turns="+str(counter))
    cards=range(8)
    random.shuffle(cards)
    cards1=range(8)
    random.shuffle(cards1)
    cards.extend(cards1)
    return cards   


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards,exposed
    global state
    global index1,index2
    global counter
    index=pos[0]//50
    if (exposed[index]!=1): 
        if state == 0:
            exposed[index] = 1   
            index2 = index
            state = 1
        elif state == 1:
            exposed[index] = 1
            index1 = index
            state = 2
            counter+=1
        elif state == 2:
            exposed[index] = 1
            if cards[index2] != cards[index1]:
                exposed[index2] = 0
                exposed[index1] = 0
            index2 = index
            state = 1
            counter += 1
    label.set_text("Turns="+str(counter))
                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards,exposed,state
    pos=[5,80]
    pos_line_b=[25,0]
    pos_line_end=[25,100]
    del_pos_b=[0,0]
    del_pos_e=[0,100]
    for i in range(16):
       if (exposed[i]==1):
           current_card=str(cards[i])
           canvas.draw_text(current_card, pos, 80, "White")
       else:
           canvas.draw_line(pos_line_b,pos_line_end,50,"Green")
           canvas.draw_line(del_pos_b,del_pos_e,3,"Lime")
       pos[0]+=50
       pos_line_b[0]+=50
       pos_line_end[0]+=50 
       del_pos_b[0]+=50
       del_pos_e[0]+=50
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)

label = frame.add_label("Turns=0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
