# Adam Gross
# POLYBIUS: A GIANT ROOM EXPLORATION GAME
# V 2.0
#
# V 2.0 is essectially a re-write. Patches the corridor closed,
#           so you can't just walk around into infinity. Also, brings in 3 winning solutions.

# V 1.2 features a working door that generates randomly along the
#       east wall of the big room. This door is unlocked by the key placed in
#       V 1.0.5

# V 1.1.5 features a locator that hides the map until the locator is found

# V 1.1 features a graphical map of the character, room, and key

# V 1.0.5 features a key placed randomly in the map. this key does nothing, but
#         can only be picked up once

# V 1.0.1 features a debug menu, type 'debug' to turn it on/off during exploration

# V 1.0 allows you to pick the size of the room

# V 0.9 works. all you can do is explore a 6x6 room.

# V 0.9B works, but you don't know when you are walking into a wall.

import random                                                       # imports random, allows to select random key, locator, door, etc. location
z = 1                                                               # enters the for loop
print "PPPPP OOOOO L   Y   Y BBBB  IIIII U   U SSSSS"
print "P   P O   O L    Y Y  B   B   I   U   U S    "
print "PPPPP O   O L     Y   BBBB    I   U   U SSSSS"               # This is a fancy freakin' title
print "P     O   O L     Y   B   B   I   U   U     S"
print "P     OOOOO LLLLL Y   BBBB  IIIII UUUUU SSSSS"
print " ___________________________________________ "
print "        A GIANT ROOM EXPLORATION GAME        "
print "                 V 2.0B \n \n"


# Size Selector Node
maxbig = int(raw_input("Size of room: "))                           # How big do you want the room to be?
while not maxbig:                                                   # Takes care of stupid people
    print "Since you put yourself in NOTHING, you cannot move, and have already lost. Good Job, Genius."
    fail = raw_input("Change room size? (y/n):")
    if fail == "y":
        maxbig = int(raw_input("Enter something other than zero this time: "))
    if fail == "n":
        z = 0
        maxbig = 1
if z:
    print "type 'q' anytime to quit"
xmax = maxbig
ymax = maxbig

x = (xmax / 2)                                                      # Generates user in middle (or closest to it) of room
y = (ymax / 2)

debug = 0
pick3 = 0
move = 0

# Random Object Generation Node
     #key
keyout = 1
keyin = 0
xkey = random.randint(0,xmax)                                       # puts the key some
ykey = random.randint(0,ymax)
     #locator
locatorout = 1
locatorin = 0
xlocator = random.randint(x-1,x+1)
ylocator = random.randint(y-1,y+1)
     #door
ydoor = random.randint (0,ymax)
l=0

# The World Supernode
while z:
    
    # Locator Node
    if locatorin and x <= xmax:
        for p in range (xmax + 2):
            print "#",
            for o in range (ymax + 2):
                if p == 0 or p == xmax + 2:
                    print "#",
                elif x == o and y == p:
                    print "X",
                elif xkey == o and ykey == p:
                    if keyout:
                        print "4",
                    if not keyout:
                        print "+",
                else:
                    print "+",
            print "#"
    if x > xmax:                                                # locator does not work if in the corridor
        print "You are outside the range of the locator, so it is of no use to you"

    print "\n"
    if x < xmax:
        print "You are stumbling about in a large, dark room."
    if x > xmax and x < 2 * xmax:
        print "You are stumbling about in a long, dark corridor."

    # Wall Alarm Node
    if x == 1:
        print "There is a wall nearby to the West."
    if x == 0 :
        print "You are standing next to a wall on the West."
    if x <= xmax:
        if y == 1:
            print "There is a wall nearby to the North."
        if y == 0:
            print "You are standing next to a wall on the North."
        if y == ymax - 1:
            print "There is a wall nearby to the South."
        if y == ymax:
            print "You are standing next to a wall to the South."
    if y != ydoor:
        if x == xmax - 1:
            print "There is a wall nearby to the East."
        if x == xmax:
            print "You are standing next to a wall to the East."
    if y == ydoor:
        if x == xmax - 1:
            print "There is a door nearby to the East."
        if x == xmax:
            if keyout:
                print "This door is locked. You must find the key to unlock it."
            if keyin:
                print "You slide the key into a lock. It clicks and slides open to reveal a long, dark corridor."
                keyin = 0
            else:
                print "This door is already unlocked. You may come and go as you please."
    if x > xmax and x < 2 * xmax:
        print "You are standing next to walls on the North and South."
    if x == 2 * xmax:
        print "You have come to a dead end."
        
    # Item Grab Node
        #Key
    if keyout:
        if x == xkey or x == xkey + 1 or x == xkey - 1:
            if y == ykey + 1 or y == ykey - 1:
                               print "There is a small, golden glow nearby."
            elif x == xkey + 1 or x == xkey - 1:
                if y == ykey:
                    print "There is a small, golden glow nearby."
            if y == ykey and x == xkey:
                print "You have found a key!"
                keyout = 0
                keyin = 1
        #Locator
    if locatorout:
        if y == ylocator and x == xlocator:
            print "You have found a locator!"
            locatorout = 0
            locatorin = 1
    # Directional Marking Node
    if x <= xmax:
        if x == 0:
            if y == 0:
                print "Obvious directions are: E, S."
            elif y == ymax:
                print "Obvious directions are: N, E."
            else:
                print "Obvious directions are: N, E, S."
        elif x == xmax and y != ydoor:
            if y == 0:
                print "Obvious directions are S, W."
            elif y == ymax:
                print "Obvious directions are N, W."
            else:
                print "Obvious directions are N, S, W."
        elif x == xmax and y == ydoor:
            if not keyout:
                if y == ymax:
                    print "Obvious directions are N, E, W."
                if y == 0:
                    print "Obvious directions are S, W, E."
                else:
                    print "Obvious directions are N, E, S, W."
        elif y == 0:
            print "Obvious directions are S, E, W."
        elif y == ymax:
            print "Obvious directions are N, E, W"
        else:
            print "Obvious directions are N, E, S, W."
    elif x > xmax and x <= 2 * xmax - 1:
        print "Obvious directions are E, W."
    elif x == 2 * xmax:
        print "You have no choice to travel W."
    #Debug Node
    if debug: 
        print "{positon(x,y): (", x, ",", y, ")", "roomSize: (", xmax, ",", ymax, ")}"
        if keyout:
            print "key (x,y): (", xkey,",",ykey,")"
        elif keyin:
            print "key is in inventory"
        else:
            print "key not in play"
        if locatorout:
            print "locator (x,y): (",xlocator,",",ylocator,")"
        elif locatorin:
            print "locator is in inventory"
            
    # Choosing the Direction
    h = raw_input ("Choose a Direction: ")

    #Directional Movment Node
    if h == 'S' or h == 's':
        if y + 1 == ymax + 1 or x > xmax:
            print "\n You cannot travel South any further. \n"
        else:
            y = y + 1
            print "\n You travel South for a bit. \n"
    elif h == 'N' or h == 'n':
        if y - 1 == -1 or x > xmax:
            print "\n You cannot travel North any further. \n"
        else:
            y = y - 1
            print "\n You travel North for a bit. \n"
    elif h == 'W' or h == 'w':
        if x - 1 == -1:
            print "\n You cannot travel West any further. \n"
        else:
            x = x - 1
            print "\n You travel West for a bit. \n"
    elif h == 'E' or h == 'e':
        if y != ydoor or keyout or keyin:
            if x + 1 == xmax + 1:
                print "\n You cannot travel East any further. \n"
            else:
                x = x + 1
                print "\n You travel East for a bit. \n"
        else:
            if not keyout and not keyin:
                if x + 1 == xmax * 2 + 1:
                    print "\n You cannot travel East any further. \n"
                else:
                    x = x + 1
                    print "\n You travel East for a bit. \n"
    elif h == 'Q' or h == 'q':
        z = 0
    elif h == 'debug':
        if not debug:
            debug = 1
            print "\n Debug ON \n"
        else:
            debug = 0
            print "\n Debug OFF \n"
    else:
        print " \n I do not understand that \n"

    #Pick a Thing Node     
    if not l:
        if x == xmax * 2:
            print "A selection of items lay before you."
            print "     1. A Jetpack"
            print "     2. A Keg of Beer"
            print "     3. A Laptop with only this game installed on it."
            pick3 = raw_input("Select one item to take, sacrificing the other two. (1-3): ")
            if pick3 == "1":
                print "You have selected the Jetpack. The Keg and Laptop disapear."
                print "Something draws you to the Southwest corner of the large, dark room."
                l = 1
            elif pick3 == "2":
                print "You have selected the Keg of Beer. The Jetpack and Laptop dissapear."
                print "Something draws you to the Southwest corner of the large, dark room."
                l = 1
            elif pick3 == "3":
                print "You have selected the Laptop. The Jetpack and Laptop dissapear"
                print "Something draws you to the Southwest corner of the large, dark room."
                l = 1
            else:
                print "I didn't understand that."
            
            
    if l:
        if y == ymax and x == 0:
            if pick3 == "1":
                print "You locate a hole in the ceiling of the room, large enough to pass through."
                print "You activate the jetpack and fly to safety."
                print "You escaped the room with", move, "moves."
                z = 0
            if pick3 == "2":
                print "You locate a perfect place upon which to do the perfect kegstand."
                print "Just before you complain that the keg is tapped and begin to stagger around into doom,"
                print "Federal agents storm in through a small hole in a ceiling. They grab you and take you"
                print "to an undisclosed location and probe your brain."
                print "You have left the room with", move, "moves."
                z = 0
            if pick3 == "3":
                print "You pick a place to sit down and open the computer, the program begins automatically..."
                ass = 0
                while ass < 100000000:
                    if ass == 50000000:
                        print "My God, this takes FOREXER!"
                    ass = ass + 1
                print "You complete the game, and the rock you are sitting on pulls you downward."
                print "You have been swallowed by the room with", move, "moves."
                z = 0
                
                
            
    move = 1 + move                              
print "Goodbye."
            
            
            
            
            
            
            
                        
                
        
