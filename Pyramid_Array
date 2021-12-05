# Level 6 Kata - Code Wars
# Write a function that when given a number >= 0, returns an Array of ascending length subarrays.


def pyramid(n):
    # Declare a return array to build.
    return_array = []
    
    # Declare an array element to build and add to the return array.
    array_element = [] 

    # Declare index variables for the inner loop index and outer loop index.
    outer_index = 0
    inner_index = 0
        
    # Loop to build return array of arrays.
    while outer_index < n:
        while inner_index <= outer_index:
            array_element.append(1)
            inner_index += 1
        return_array.append(array_element)
        
        # Reset array_element and inner_index to be used for the next iteration.
        array_element = []
        inner_index = 0
        outer_index += 1
    
    # Return the finalized array.
    return return_array
