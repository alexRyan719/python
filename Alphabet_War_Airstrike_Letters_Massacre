# Level 6 Kata - Code Wars
# Introduction
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters called airstrike to help them in war - dashes and dots are spreaded everywhere on the battlefield.

# Task
# Write a function that accepts fight string consists of only small letters and * which means a bomb drop place. Return who wins the fight after bombs are exploded. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:

#  w - 4
#  p - 3 
#  b - 2
#  s - 1
# The right side letters and their power:

#  m - 4
#  q - 3 
#  d - 2
#  z - 1
# The other letters don't have power and are only victims.
# The * bombs kill the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ );


def alphabet_war(fight):
    combatants = "wpbsmqdz"
    battle_field = []
    index = 1
    point_dict = {"w":4, "p":3, "b":2, "s":1, "m":-4, "q":-3, "d":-2, "z":-1}
    
    for char in fight:
        battle_field.append(char)
    
    if fight[0] == "*":
        battle_field[0] = "_"
        battle_field[1] = "_"
    if fight[-1] == "*":
        battle_field[-1] = "_"
        battle_field[-2] = "_"
    
    while index < len(fight)-1:
        if fight[index] == "*":
            battle_field[index] = "_"
            battle_field[index - 1] = "_"  
            battle_field[index + 1] = "_"
        index += 1
    
    points = 0
    
    new_fight = "".join(battle_field)
    
    for char in new_fight:
        if char in combatants:
            points += point_dict[char]
    
    if points > 0:
        return "Left side wins!"
    elif points < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"
