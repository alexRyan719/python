# Level 6 Kata - Code Wars
# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    odd_one = 0
    
    for num in seq:
        if seq.count(num) % 2 != 0:
            odd_one = num
    
    return odd_one
