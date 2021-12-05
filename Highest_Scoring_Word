# Level 6 Kata - Code Wars
# Shortly after doing this Kata, I realized using a Dictionary would be much more efficient and use less lines of code. 
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def high(x):
    # Declare a string variable to store the highest scoring word.
    top_word = ""
    
    # Create a list variable from the input string.
    word_list = x.split()
    
    # Create an int variable to keep track of the highest scoring word.
    highest_score = 0
    
    # Create a an int variable to keep track of the score to test.
    test_score = 0
    
    # Loop through the words in the word_list to find the highest scoring word.
    for word in word_list:
        # Calculate the word's score and compare to highest_score.
        for char in word:
            if char == 'a':
                test_score += 1
            elif char == 'b':
                test_score += 2
            elif char == 'c':
                test_score += 3
            elif char == 'd':
                test_score += 4
            elif char == 'e':
                test_score += 5
            elif char == 'f':
                test_score += 6
            elif char == 'g':
                test_score += 7
            elif char == 'h':
                test_score += 8
            elif char == 'i':
                test_score += 9
            elif char == 'j':
                test_score += 10
            elif char == 'k':
                test_score += 11
            elif char == 'l':
                test_score += 12
            elif char == 'm':
                test_score += 13
            elif char == 'n':
                test_score += 14
            elif char == 'o':
                test_score += 15
            elif char == 'p':
                test_score += 16
            elif char == 'q':
                test_score += 17
            elif char == 'r':
                test_score += 18
            elif char == 's':
                test_score += 19
            elif char == 't':
                test_score += 20
            elif char == 'u':
                test_score += 21
            elif char == 'v':
                test_score += 22
            elif char == 'w':
                test_score += 23
            elif char == 'x':
                test_score += 24
            elif char == 'y':
                test_score += 25
            elif char == 'z':
                test_score += 26
        # If the score of the current word is higher than the current highest_score, set to top_word and set highest_score.
        if test_score > highest_score:
            highest_score = test_score
            top_word = word
        # Reset test_score to properly compare the remaining words.
        test_score = 0    
    # Return the highest scoring word.
    return top_word
