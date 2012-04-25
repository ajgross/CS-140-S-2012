# Adam Gross
# Battle in the Big Room
#V 0.1
#
#
import random
def pregame():
    lvlAtk = int(raw_input("attack level (0-20): "))
    lvlDef = float(raw_input("defense level (0-20): "))
    lvlHp = int((lvlDef + ((lvlDef / 4)*7) * 2 )+(lvlDef / 2 + (lvlDef / 13)*10 + (lvlDef / 23) + ((lvlDef / 7)*5) + lvlDef / 5 * lvlDef)+ 10)
    hp = lvlHp
    pickSwd = int(raw_input("Choose a Sword: \n 1. A Rusty Dagger. \n 2. A Broad Sword. \n 3. A Bastard Sword. \n 4. A Keen Short Sword. \n (1-4): "))
    if pickSwd == 1:
        sword = ("A Rusty Dagger", "The rust buildup on this 6-inch dagger has made it very dull.", 0, 1, 2, 1, False)
    elif pickSwd == 2:
        sword = ("A Broad Sword", "This 21-inch Sword is very heavy.", 5, 5, 12, 50, False)
    elif pickSwd == 3:
        sword = ("A Bastard Sword", "This Sword is nearly three feet long and requires both hands to use.", 12, 30, 36, 40, True)
    elif pickSwd == 4:
        sword = ("A Keen Short Sword", "This 12-inch classic is very sharp.", 1, 14, 24, 16, False)
    minAtk = lvlAtk * (lvlAtk/8) + sword [3] #max Base Attack 50, min Base Attack 0. Sword added post facto
    pickDef = int(raw_input("Choose your armor \n 1. Clothing. \n 2. Chain Mail. \n 3. Plate Armor. \n (1-3): "))
    if pickDef == 1:
        armor = ("Clothing", "Stylish, but does not offer much protection.", 0)
    elif pickDef == 2:
        armor = ("Chain Mail", "Armor made from interlocking rings.", .14)
    elif pickDef == 3:
        armor = ("Plate Armor", "Armor made of plates of steel", .22)
    ymax = 8
    xmax = 8
    x = (xmax / 2)                                                      # Generates user in middle (or closest to it) of room
    y = (ymax / 2)

    debug = 0
    pick3 = 0
    move = 0
    pot = 6
    spot = 3

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
        # enemies
    bad1 = ["A Giant Rat", "This overgrown vermin will attack at the slightest provocation. Otherwise, it will just eat grain.", 10, 3, 6]
    xbad1 = random.randint(0,8)
    ybad1 = random.randint(0,8)
    bad2 = ["A Cave Ghoul", "This monster doesn't want you in his Big Room.", 80, 6, 9]
    xbad2 = random.randint(0,8)
    ybad2 = random.randint(0,8)
    bad3 = ["A Wild Marcus Darden", "With terrifying dreadlock whips and soothingly low voice, this feind is a double threat", 120, 10, 25]
    xbad3 = random.randint(0,8)
    ybad3 = random.rantint(0,8)
    game = 1
    

def draw():
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
                elif bad1:
                    if xbad1 == o and ybad1 == p:
                        print "O"
                elif bad2:
                    if xbad2 == o and ybad2 == p:
                        print "O"
                elif bad3:
                    if xbad3 == o and ybad3 ==p:
                        print "O"
                else:
                    print "+",
            print "#"
def explore():
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
def grab():
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
def getDir():
    while not a:
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

def fight():
    while a:
        print "You have engaged", enemy[0], "!!!"
        s = int(raw_input("What do you do? \n 1. Attack. \n 2. Use Item \n 3. Run. \n 4. Quit. \n (1-4): "))
        if s == 1:
            minHit = sword [3]
            maxHit = sword [4]
            critch = sword [5]
            if lvlAtk >= sword [2]:
                ifhit = random.randint(1, 50)
                if ifhit >= 2: 
                    doeshit = 1
                else:
                    doeshit = 0
            else:
                print 'Your insufficient weapons proficiency inhibits your ability to use this weapon.'
                ifhit = random.randint(1,50)
                if ifhit >= 30:
                    doeshit = 1
                else:
                    doeshit = 0
            if doeshit:
                if lvlAtk == sword [2] * 2:
                    critch = sword [5] * 2
                critGo = random.randint(1, 100)
                if not critGo > critch:
                    criticalHit = 1
                    minHit = minHit + maxHit
                    maxHit = maxHit * 2
        
                else:
                    criticalHit = 0
                if criticalHit:
                    print 'It\'s a critical hit!'
                hit = random.randint(minHit, maxHit)
                enemy [2] = enemy [2] - hit
                print hit, 'Damage Inflicted'
                if enemy [2] < 1:
                    print 'you have defeated', enemy [0], '!'
                    a=0
            else:
                print 'Miss!'
                hit = 0
        
        if s == 2:
            item = int(raw_input("Choose an Item: \n 1. Health Potion \n 2. Super Health Potion \n(1-2): "))
            if item == 1:
                if pot = True:
                    hp = hp + 30
                    pot = pot - 1
                else:
                    print "You no longer have any Potions!"
            elif item == 2:
                if spot = True:
                    hp = hp + 60
                    spot = spot-1
                else:
                    print "You no longer have any Super Potions!"
            elif item == 3:
                hp = lvlHp
            hit = 0    
        if s == 3:
            enemy = 0
            print "Got away safely!"
        if s == 4:
            a = 0
            z = 0
        #enemy's Turn
        if enemy [2] > 0:
            minCtr = enemy [3]
            maxCtr = enemy [4]
            ctr = random.randint(minCtr,maxCtr)
            ctr = int(ctr * (1 - armor [2]))
            hp = hp - ctr
            print ctr, "Damage Recieved! \n You have", hp, "HP left!"
            if hp < 1:
                print "You have been defeated by", enemy [0], '!'
                a=0
def postMove():
    bmo = 1
    while bmo < 5:
        badmove = random.randint
        if bmo = 1:
            if bad1:
                if badmove == 1:
                    if xbad1 > 0:
                        xbad1 = xbad1 - 1
                elif badmove == 2:
                    if xbad1 < 8:
                        xbad1 = xbad1 + 1
                elif badmove == 3:
                    if ybad1 > 0:
                        ybad1 = ybad1 - 1
                elif badmove == 4:
                    if ybad1 < 8:
                        ybad1 = ybad1 + 1
        elif bmo = 2:
            if bad2:
                if badmove == 1:
                    if xbad2 > 0:
                        xbad2 = xbad2 - 1
                elif badmove == 2:
                    if xbad2 < 8:
                        xbad2 = xbad2 + 1
                elif badmove == 3:
                    if ybad2 > 0:
                        ybad2 = ybad2 - 1
                elif badmove == 4:
                    if ybad2 < 8:
                        ybad2 = ybad2 + 1
        elif bmo = 3:
            if bad3:
                if badmove == 1:
                    if xbad3 > 0:
                        xbad3 = xbad3 - 1
                elif badmove == 2:
                    if xbad3 < 8:
                        xbad3 = xbad3 + 1
                elif badmove == 3:
                    if ybad3 > 0:
                        ybad3 = ybad3 - 1
                elif badmove == 4:
                    if ybad3 < 8:
                        ybad3 = ybad3 + 1
def winning():
    if l:
        if y == ymax and x == 0:
            if bad1 = False and bad2 = False and bad3 = False:
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
            else:
                print "Defeat your enemies before leaving."
                    
                    
            
    move = 1 + move
def main ()
    pregame()
    while game:
        draw()
        explore()
        grab()
        if x == xbad1 and y == ybad1:
            a=1
        if x == xbad2 and y == ybad2:
            a=1
        if x == xbad3 and y == ybad3:
            a=1
        getDir()
        fight()
        winning()
if __name__=='__main__':
    main()

    
