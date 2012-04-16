#Simulated attack with counter
import random
z=1

lvlAtk = int(raw_input("attack level (0-20): "))
lvlDef = float(raw_input("defense level (0-20): "))
lvlHp = int((lvlDef + ((lvlDef / 4)*7) * 2 )+(lvlDef / 2 + (lvlDef / 13)*10 + (lvlDef / 23) + ((lvlDef / 7)*5) + lvlDef / 5 * lvlDef)+ 10)
hp = lvlHp
    
while z:
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

    pickBad = int(raw_input("Choose an enemy: \n 1. A punching bag: will not counterattack, but does not die. \n 2. A giant rat: Low counter, low HP \n 3. A cave monster: medium counter, medium HP. \n 4. An Omega Guardian: High Counter, High HP. \n (1-4): "))
    if pickBad == 1:
        enemy = ["A Punching Bag", "This dummy is best to train on, as it does not hurt you. But it also will not die.", 9999999999999, 0, 0]
    elif pickBad == 2:
        enemy = ["A Giant Rat", "This overgrown vermin will attack at the slightest provocation. Otherwise, it will just eat grain.", 10, 3, 6]
    elif pickBad == 3:
        enemy = ["A Cave Monster", "This tall, sludgy monster does not see the light of day. It is very territorial.", 82, 13, 36]
    elif pickBad == 4:
        enemy = ["An Omega Guardian", "Guardians are of the highest order of Omega infantry, and protect important charges.", 250, 50, 70]
    a=1
    while a:
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
                hp = hp + 30
            elif item == 2:
                hp = hp + 60
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
        
            

    
