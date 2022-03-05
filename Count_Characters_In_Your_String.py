# Level 6 Kata - Code Wars
# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    char_dict = {}
    
    for char in string:
        if char not in char_dict:
            char_dict.update({ char : 1 })
        else:
            char_dict[char] += 1
    
    return char_dict
