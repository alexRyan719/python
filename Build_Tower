# Level 6 Kata - Code Wars
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *


def tower_builder(n_floors):
    padding = " " * (n_floors -1)
    stars = "*"
    tower = []
    floor = ""
    
    while n_floors > 0:
        floor = padding + stars + padding
        tower.append(floor)
        padding = padding[1:]
        stars += "**"
        n_floors -= 1
    
    return tower
