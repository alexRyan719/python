# Level 6 Kata - Code Wars
# Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.

# At long last, we need a way to unscramble what these pirates are saying.

# Write a function that will accept a jumble of letters as well as a dictionary, and output a list of words that the pirate might have meant.

# For example:

# grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
# Should return ["sport", "ports"].

# Return matches in the same order as in the dictionary. Return an empty array if there are no matches.

# Good luck!


def grabscrab(word, possible_words):
    # Define a return list to build and a boolean to use in the loops.
    return_list = []
    possible_match = True
    
    # Loop through the possible words and compare chars in word to each possible word.
    for target in possible_words:
        
        # Loop through each char in the possible word and verify there are the same amounts of that char in word.
        for char in target:
            if char not in word:
                possible_match = False
            if target.count(char) != word.count(char):
                possible_match = False
        if possible_match:
            return_list.append(target)
        possible_match = True
    
    # Return the return list.
    return return_list
