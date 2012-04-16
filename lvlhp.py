z=1
while z:
    lvlDef = float(raw_input("defense level (0-20): "))
    lvlHp = int((lvlDef + ((lvlDef / 4)*7) * 2 )+(lvlDef / 2 + (lvlDef / 13)*10 + (lvlDef / 23) + ((lvlDef / 7)*5) + lvlDef / 5 * lvlDef)+ 10)
    hp = lvlHp
    print hp
