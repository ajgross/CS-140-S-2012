# Roll for Damage
# Subnode for RPG
# V 0.1
#
#
# This is the attack node for swords
# tuple = ('name', 'itemdesc', lowatk, hiatk, critch, noshield)
import random
print "'q' to quit, 'info' for item description."
z = 1
lvlatk = int(raw_input("attack level(0-8): "))
while z:
#begin
    
    pick3 =  raw_input("Pick from \n Sword 1: A dagger, mid class damage roll, 1% chance of critical. \n Sword 2: A Broad Sword, low damage, but 50% chance of critical \n Sword 3: A Two Handed Sword, High damage roll, 20 % chance of critical \n (1-3) : ")
    if pick3 == '1':
        weapon = ('Rusty Dagger', 'A Dagger with a 6 inch blade, the rust buildup has dulled it immensely', 0, 1, 3, 1, 0)
    elif pick3 == '2':
        weapon = ('Broad Sword', 'An 18 inch sword that is very heavy.', 2, 15, 20, 50, 0)
    elif pick3 == '3':
        weapon = ('Two-Handed Sword', 'since this sword is nearly 3 feet long, it requires both hands for use, your shield has been unequipped', 5, 30, 55, 20, 1)
    elif pick3 == 'q':
        z = 0
    elif pick3 == 'info':
        print weapon[1]
    else:
        pick3 = b4
    b4 = pick3
    lowHit = weapon [3]
    highHit = weapon [4]
    
    if lvlatk >= weapon [2]:
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
        if lvlatk == weapon [2] * 2:
            critch = weapon [5] * 2
        else:
            critch = weapon [5]
        critGo = random.randint(1, 100)
        if not critGo > critch:
            criticalHit = 1
            lowHit = lowHit + highHit
            highHit = highHit * 2
        
        else:
            criticalHit = 0
        if criticalHit:
            print 'It\'s a critical hit!'
        hit = random.randint(lowHit, highHit)            
        print hit
    else:
        print 'Miss!'
    
