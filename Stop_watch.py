#  "Stopwatch: The Game"
import simplegui

message = "0:00.0"
attempts = 0   # number of clicks of the stop button
count = 0	   # number of successful clicks
time = 0	   # the timer
tries = "0/0"  # successful attempts/attempts
check = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    data="NULL"
    if (t==0):
        data="0:00.0"
        
    if (t<10):
        data="0:00."+str(t)
        
    if (t<100 and t>=10):
        data="0:0"+str(t/10)+"."+str(t%10)
       
    if (t>=100 and t<600):
        data="0:"+str(t/10)+"."+str(t%10)
         
    if (t>=600 and t<1200):
        t=t-600
        if (t<100):
            data="1:0"+str(t/10)+"."+str(t%10)    
        if (t>100):
            data="1:"+str(t)+"."+str(t%10)
    if (t>=1200):
       first_digit=str(t/600)
       rem=t%600
       if (rem==0):
           data=first_digit+":00.0"
            
       if (rem<10):
           data=first_digit+":00."+str(rem)
            
       if (rem<100 and rem>=10):
           data=first_digit+":"+str(rem/10)+"."+str(t%10)
       
       if (rem>=100 and rem<600):
           data=first_digit+":"+str(rem/10)+"."+str(t%10)
                    
    return data
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global check
    timer.start()
    check = True
    

def stop():
    global tries, time, count, attempts, check
    timer.stop()
    if (check!=False):
        attempts+=1
        check = False
        if (time%10==0):
            count+=1
    tries=str(count)+ "/" + str(attempts)
    

def reset():
    global count, time, attempts, tries, message, check
    check = False 
    timer.stop()
    tries = "0/0"
    attempts = 0
    count = 0
    time = 0
  
def update():
    global time, message, check
    message=format(time)
    return message   

def timer_handler():
    global time
    time += 1
    
    
# define event handler for timer with 0.1 sec interval
 
timer = simplegui.create_timer( 100, timer_handler)

# define draw handler
def draw(canvas):
    message=update()
    canvas.draw_text(message, [100,150], 46, "White")
    canvas.draw_text(tries, [240,30], 26, "Lime")
    
# create frame
frame=simplegui.create_frame("Stopwatch_game",300,300)
frame.set_draw_handler(draw)

# register event handlers
frame.add_button("Start",start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()
format(0)

