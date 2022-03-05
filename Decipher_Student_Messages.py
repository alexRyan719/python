# Level 6 Kata - Code Wars
# Two students are giving each other test answers during a test. They don't want to be caught so they are sending each other coded messages.
# For example one student is sending the following message: "Answer to Number 5 Part b". He starts with a square grid (in this example a 5x5 grid) 
# and he writes the message down, including with spaces:

#Answe
#r to 
#Numbe
#r 5 P
#art b
# He then starts writing the message down one column at a time, from the top to the bottom. The encoded message is now: "ArNran u rstm5twob e ePb"
# You are the teacher of this class. Your job is to decipher the messages and bust the students.

# Task
# Complete the function that takes one parameter (the encoded message) and return the original message.

# Note: The length of the string is always going to be a perfect square.

# Have fun !!!


def decipher_message(message):
    import math
    decoded_message = ""
    
    width = int(math.pow(len(message),.5))
    height = int(math.pow(len(message),.5))
    x = 0
    y = 0
    index = 0
    
    # Initialize a 2D array as Matrix.
    Matrix = [[0 for x in range(width)] for y in range(height)]
    
    # Populate Matrix with input message.
    while y < height:
        while x < width:
            Matrix[x][y] = message[index]
            x += 1
            index += 1
        x = 0
        y += 1
    
    x = 0
    y = 0
    
    # Build decoded message by traversing Matrix vertically.
    while x < width:
        while y < height:
            decoded_message += Matrix[x][y]
            y += 1
            index += 1
        y = 0
        x += 1
    
    
    
    return decoded_message
