# Level 4 Kata - Code Wars
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

def solution(string,markers):
    to_add = True
    return_string = ""
    index = 0
    while index < len(string):
        if string[index] in markers:
            print(string[index])
            return_string = return_string.rstrip(" ")
            to_add = False
            index += 1
            while to_add == False and index < len(string):
                if string[index] == "\n":
                    to_add = True
                    return_string += string[index]
                index += 1
        else:
            return_string += string[index]
            index += 1
    return return_string
