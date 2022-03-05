# Level 6 Kata - Code Wars
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers
# or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.


def find_outlier(integers):
    if integers[0] % 2 == 0 and integers[1] % 2 == 0:
        # find the odd
        for target_int in integers:
            if target_int % 2 != 0:
                return target_int
    elif integers[1] % 2 == 0 and integers[2] % 2 == 0:
        # find the odd
        for target_int in integers:
            if target_int % 2 != 0:
                return target_int
    elif integers[0] % 2 == 0 and integers[2] % 2 == 0:
        # find the odd
        for target_int in integers:
            if target_int % 2 != 0:
                return target_int
    else:
        # find the even
        for target_int in integers:
            if target_int % 2 == 0:
                return target_int
        
    return None
