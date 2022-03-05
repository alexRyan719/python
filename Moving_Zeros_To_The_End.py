# Level 5 Kata - Code Wars
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(array):
    # Declare a list variable and count variable.
    new_list = []
    zero_count = 0
    
    # Construct the new array with non zero values. Keep track of how many zero values there are.
    for num in array:
        if num == 0:
            zero_count += 1
        else:
            new_list.append(num)
    
    # Add the zeros to the end of the array / list.
    while zero_count > 0:
        new_list.append(0)
        zero_count -= 1
        
    # Return the completed array / list.
    return new_list
