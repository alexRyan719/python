# Level 6 Kata - Code Wars
# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the 
# missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']


def solution(s):
    if len(s) % 2 != 0:
        s = s + '_'
    
    return_arr = []
    index = 0
    temp_str = ""
    
    while index < len(s) - 1:
        temp_str = s[index] + s[index+1]
        return_arr.append(temp_str)
        index += 2
        
    return return_arr
