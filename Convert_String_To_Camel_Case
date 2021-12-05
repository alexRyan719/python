# Level 6 Kata - Code Wars
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if 
# the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).


def to_camel_case(text):
    # Declare variable for return string
    result = ""
    
    # Declare boolean to set if '-' or '_' are encountered
    cap_it = False
    
    # Loop through input string checking for '-' or '_'. If found, capitalize next char and reset boolean
    for char in text:
        if char == '-' or char == '_':
            cap_it = True
        elif cap_it:
            char = char.upper()
            result += char
            cap_it = False
        else:
            result += char
    
    # Return the Camel Case string
    return result
