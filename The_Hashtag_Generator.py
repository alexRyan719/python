# Level 5 Kata - Code Wars
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    # Declare a return string and list to construct the return string.
    return_string = "#"
    word_list = s.lower().split()
    capitalized_list = []
    temp = ""
    
    # Check if input string is empty.
    if len(s) == 0:
        return False
    
    # Capitalize the first letter of each word.
    for word in word_list:
        if len(word) == 1:
            capitalized_list.append(word.upper())
        else:
            temp = word[0].upper() + word[1:]
            capitalized_list.append(temp)
        
    # Construct the hashtag / return string from the capitalized words.
    for word in capitalized_list:
        return_string += word
    
    # If the hashtag is over 140 characters, return False.
    if len(return_string) > 140:
        return False
    
    # Return the return string.
    return return_string
