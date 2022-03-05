# Level 6 Kata - Code Wars
# Task
# You will be given a string of English digits "stuck" together, like this:

# "zeronineoneoneeighttwoseventhreesixfourtwofive"

# Your task is to split the string into separate digits:

# "zero nine one one eight two seven three six four two five"


def uncollapse(digits):
    digit_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    temp_string = ""
    return_list = []
    return_string = ""
    
    for char in digits:
        temp_string += char
        if temp_string in digit_list:
            return_list.append(temp_string)
            temp_string = ""
    
    return_string = " ".join(return_list)
    
    return return_string
