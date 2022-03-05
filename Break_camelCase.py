# Level 6 Kata - Code War
# Complete the solution so that the function will break up camel casing, using a space between words.


def solution(s):
    new_string = ""
    
    for char in s:
        if char.islower():
            new_string += char
        else:
            new_string += " "
            new_string += char
            
    return new_string
