# Level 6 Kata - Code Wars
# Implement a function, so it will produce a sentence out of the given parts.

# Array of parts could contain:

# words;
# commas in the middle;
# multiple periods at the end.
# Sentence making rules:

# there must always be a space between words;
# there must not be a space between a comma and word on the left;
# there must always be one and only one period at the end of a sentence.
# Example:

# makeSentence(['hello', ',', 'my', 'dear']) // returns 'hello, my dear.'


def make_sentences(parts):
    # Declare a string to build and return.
    return_string = ""
    
    # Iterate through each part in parts. Check if the part is a comma and construct the return string accordingly.
    for part in parts:
        if part == ",":
            return_string += part
        else:
            return_string += " " + part
    
    # Remove the leading space.
    return_string = return_string[1:]
    
    # Remove all periods and trailing spaces from the end.
    while return_string[-1] == "." or return_string[-1] == " ":
        return_string = return_string[:-1]
    
    
    # Add a period to the end.
    return_string += "."
    
    # Return the return string.
    return return_string
