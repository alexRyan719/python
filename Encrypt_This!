# Level 6 Kata - Code Wars
# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.


def encrypt_this(text):
    return_string = ""
    if len(text) == 0:
        return return_string
    word_list = text.split()
    for word in word_list:
        if len(word) == 1:
            return_string += str(ord(word[0]))
        elif len(word) == 2:
            return_string += str(ord(word[0]))
            return_string += word[1]
        else:
            return_string += str(ord(word[0]))
            return_string += word[-1]
            return_string += word[2:-1]
            return_string += word[1]
        return_string += " "
    return_string = return_string.rstrip()
    return return_string
