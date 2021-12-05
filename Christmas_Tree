# Level 6 Kata - Code Wars
# Create a function that returns a christmas tree of the correct height.

# For example:

# height = 5 should return:

#     *    
#    ***   
#   *****  
#  ******* 
# *********
# Height passed is always an integer between 0 and 100.

# Use \n for newlines between each line.

# Pad with spaces so each line is the same length. The last line having only stars, no spaces.


def christmas_tree(height):
    padding = height -1 
    return_string = ""
    for num in range(1, height+1):
        return_string += ' ' * padding
        return_string += '*' * (num * 2 - 1)
        return_string += ' ' * padding
        return_string += "\n"
        padding -= 1
    return_string = return_string[:-1]
    return return_string
