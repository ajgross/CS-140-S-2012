# Adam Gross
# The Big Room (or, My First World)
# V 0.9
#
#I decided to, instead of making the origin 0,0 and creating a negative aspect,
# make the world in the first quadrant entirely. type debug to see coordinates.


# change z to 0 to break the program. Do it. I dare you.
z = 1
# change to edit room size
xmax = 6
ymax = 6
# the x min and y min are 0
x = int(xmax / 2)
y = int(ymax / 2)
# turns off debug in case it is on
debug = 0
# exit variable
print "Type q anytime to exit."

while z:
    print "You are in a large room."
# Wall Proximity Alarms
    if x == 1: 
        print "There is a wall nearby to the West."
    if x == xmax - 1: # if one less than the maxSize of room x
        print "There is a wall nearby to the East."
    if y == 1:
        print "There is a wall nearby to the South."
    if y == ymax - 1: # if one less then the maxSize of room y
        print "There is as wall nearby to the North."
# Wall Warnings        
    if x == 0:
        print "You are standing next to a wall on the West."
    if x == xmax: # if maxSize x
        print "You are standing next to a wall on the East."
    if y == 0:
        print "You are standing next to a wall on the South."
    if y == ymax: # if maxSize y
        print "You are standing next to a wall on the North."

# Directional Marking
    if x == 0:
        if y == 0:
            print "Obvious directions are: N, E."
        elif y == ymax:
            print "Obvious directions are: E, S."
        else:
            print "Obvious directions are: N, E, S."
    elif x == xmax:
        if y == 0:
            print "Obvious directions are: N, W."
        elif y == ymax:
            print "Obvious directions are: S, W"
        else:
            print "Obvious directions are: N, S, W"
    elif y == 0: # extra if/elif statements would be redundant
        print "Obvious directions are N, E, W."
    elif y == ymax:
        print "Obvious directions are E, S, W."
    else:
        print "Obvious directions are N, E, S, W."
    if debug: # debug describes position and max when on (via bool)
        print "positon(x,y): (", x, ",", y, ")", "roomSize: (", xmax, ",", ymax, ")"
# Choosing the direction
        
    h = raw_input("Choose a direction: ")
    
# Traveling around
    if h == 'S' or h == 's':
        if y - 1 == -1:
            print "\n You can not travel south any further. \n"
        else:
            y = y - 1
            print "\n You travel south for a bit."
        
    elif h == 'E' or h == 'e':
        if x + 1 == xmax + 1:
            print "\n You can not travel east any further. \n"
        else:
            x = x + 1
            print "\n You travel east for a bit."
            
    elif h == 'N' or h == 'n':
        if y + 1 == ymax +1:
            print "\n You can not travel north any further. \n"
        else:
            y = y + 1
            print "\n You travel north for a bit."

    elif h == 'W' or h == 'w':
        if x - 1 == -1:
            print "\n You can not travel west any further. \n"
        else:
            x = x - 1
            print "\n You travel west for a bit."
    elif h == 'Q' or h == 'q':
        z = 0
    elif h == "debug": #Turns debug on/off
        if debug == 0:
            debug = 1
        else:
            debug = 0

    else:
        print "\n I do not understand that. \n"
        
print "Goodbye."
while debug < 5000000:
    debug = 1+debug

            
        
    
