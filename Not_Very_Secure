# Level 5 Kata - Code Wars
# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

# The string has the following conditions to be alphanumeric:

# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore


def alphanumeric(password):
    # Declare a boolean to keep track and be returned.
    is_valid = True
    
    # Check if password is empty. If it is, it is not valid.
    if len(password) == 0:
        is_valid = False
    
    # Check each character in password to ensure it is alphanumeric.
    for char in password:
        if char.isalpha() == False and char.isdigit() == False:
            is_valid = False
        
    # Return the boolean.
    return is_valid
