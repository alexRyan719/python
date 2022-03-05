# Level 6 Kata - Code Wars
# Background:
# You're working in a number zoo, and it seems that one of the numbers has gone missing!

# Zoo workers have no idea what number is missing, and are too incompetent to figure it out, so they're hiring you to do it for them.

# In case the zoo loses another number, they want your program to work regardless of how many numbers there are in total.

# Task:
# Write a function that takes a shuffled list of unique numbers from 1 to n with one element missing (which can be any number including n). Return this missing number.

# Note: huge lists will be tested.

# Examples:
# [1, 3, 4]  =>  2
# [1, 2, 3]  =>  4
# [4, 2, 3]  =>  1


def find_missing_number(numbers):
    # Declare int variables for missing animal and index.
    missing_animal = 0
    index = 0
    
    # Check for empty inputs.
    if len(numbers) == 0:
        return 1
    
    # Sort the numbers.
    numbers = sorted(numbers)
    
    # Locate the missing animal.
    for num in range(1,len(numbers)+1):
        if num != numbers[index]:
            missing_animal = num
            break
        index += 1
    
    # Check for last animal missing.
    if missing_animal == 0:
        missing_animal = numbers[-1] + 1
    
    # Return the missing animal.
    return missing_animal
