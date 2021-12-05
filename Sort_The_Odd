# Level 6 Kata - Code Wars
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.


def sort_array(source_array):
    odd_array = []
    return_array = []
    index = 0
    
    for num in source_array:
        if num % 2 != 0:
            odd_array.append(num)
    
    odd_array.sort()
    
    for num in source_array:
        if num % 2 != 0:
            return_array.append(odd_array[index])
            index += 1
        else:
            return_array.append(num)
            
    return return_array
