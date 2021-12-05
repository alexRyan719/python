# Level 5 Kata - Code Wars
# Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to 
# the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably 
# drink those beers, because let's pretend it's Friday too.

# A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

# Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:

# your referral bonus, and

# the price of a beer can

# For example:

# beeramid(1500, 2); // should === 12
# beeramid(5000, 3); // should === 16

def beeramid(bonus, price):
    # Calculate how many beers you can buy with your bonus.
    beers = bonus // price
    
    # Check for negative funds.
    if beers < 0:
        return 0
    
    # Declare a row counter and total count of beers used.
    pyramid = 0
    row_count = 0
    
    # Calculate the beer pyramid.
    while pyramid < beers:
        pyramid += row_count ** 2
        row_count += 1
    
    # Error handle for looping too many times.
    if pyramid > beers:
        pyramid -= row_count ** 2
        row_count -= 1
    
    # Return the number of complete levels possible.
    if row_count == 0:
        return row_count
    else:
        return row_count - 1
