# Level 6 Kata - Code Wars
# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.


def digital_root(n):
    # Declare a boolean to keep track of when to break out of the while loop
    one_digit = False
    
    # Declare an int variable to store the value of the sum of the digits
    sum = 0
    
    # Declare a new int variable to copy the input int variable
    n_copy = n
    
    # Loop through the input integer and add each digit. Repeat process until the sum variable is only one digit
    while one_digit == False:
        for digit in str(n_copy):
            sum += int(digit)
        if len(str(sum)) == 1:
            one_digit = True
        else:
          n_copy = sum
          sum = 0
                
    # Return the finalized, one digit sum
    return sum
