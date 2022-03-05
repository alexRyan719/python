# Level 6 Kata - Code Wars
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" ) => returns "This is rehtona test"


def spin_words(sentence):
    return_string = ""
    word_list = sentence.split()
    
    for word in word_list:
        if len(word) >= 5:
            word = word[::-1]
        return_string += word
        return_string += " "
        
    return_string = return_string[:-1]
    
    return return_string
