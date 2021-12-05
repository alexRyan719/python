# Level 6 Kata - Code Wars
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each
# other and preserving the original order of elements.


def unique_in_order(iterable):
    # Declare a list variable to construct and return.
    return_list = []
    
    # Check if input sequence is empy. If it is, return the empty list.
    if len(iterable) == 0:
        return return_list
    
    # Declare a variable to compare additional items to.
    first_item = iterable[0]
    return_list.append(first_item)
    
    # Loop through input sequence and build the return_list with unique items.
    for item in iterable:
        if item != first_item:
            return_list.append(item)
            first_item = item
            
    # Return the return_list
    return return_list
