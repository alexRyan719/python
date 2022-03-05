# Level 5 Kata - Code Wars
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    # Declare a list to store individual words in the input sentence and a string to return.
    word_list = text.split()
    return_string = ""
    
    # Transform each word in word_list to the Pig Latin version - move the first letter to the end and add "ay."
    for word in word_list:
        if word.isalpha():
            return_string += word[1:] + word[0] + "ay" + " "
        else: 
            return_string += word + " "
            
    # Remove the trailing space.
    return_string = return_string[:-1]
        
    # Return the return string.
    return return_string
