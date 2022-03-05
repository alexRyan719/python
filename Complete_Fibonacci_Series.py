# Level 6 Kata - Code Wars
# The function 'fibonacci' should return an array of fibonacci numbers. The function takes a number as an argument to decide how many no. of elements to produce. 
# If the argument is less than or equal to 0 then return empty array

# Example:

# fibonacci(4) # should return  [0,1,1,2]
# fibonacci(-1) # should return []


def fibonacci(n):
    # Declare list and count variables.
    count = 2
    fib_list = []
    return_list = []
    
    # Check for inputs of less than or equal to zero.
    if n <= 0:
        return fib_list
    
    # Build basic Fibonacci list.
    fib_list.append(0)
    fib_list.append(1)
    
    # Calculate out to 10 or n, whichever is higher.
    if n > 10:
        while count < n:
            fib_list.append(fib_list[count-2] + fib_list[count-1])
            count +=1
    else:
        while count < 10:
            fib_list.append(fib_list[count-2] + fib_list[count-1])
            count +=1
    
    # Reset count to build return list.
    count = 0
    
    # Calculate the Fibonaccis series for n elements.
    while count < n:
        return_list.append(fib_list[count])
        count +=1
        
    # Return the return list.
    return return_list
