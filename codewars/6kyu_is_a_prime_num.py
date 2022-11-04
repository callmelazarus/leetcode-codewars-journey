# solution below works, but is not efficient... refactor!
def is_prime_slow(num):
    if num > 1:
        # if num % range of numbers -> if number forms, then there is a remainder. 
        # number % by itself, and 1, should return 0, that's it
        # loop thru checks from 1 to num
        counter = 0  # if counter
        for item in range(1,num+1): # range now includes 1 to number + 1. normally range starts at 0. I need to add one to the 2nd argumetn in order to have the # loops match the number
            # add to counter if modulus of value is 0
            # if counter = 2 -> prime number
            if num%item == 0:
                counter += 1
        if counter == 2:
            return True
    return False

def is_prime_still_slow(num):
    if num > 1:
        for item in range(2,num): 
            if num%item == 0:
                return False
            continue
        return True
    return False

import math 

def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)+1)):
            if num%i == 0: # than the number is not prime...
                return False 
        return True  # will return if true if we have tested this, and found no unique factors between 2 and sqrt of value
    return False # returns false for numbers 1, and less


print(is_prime(5098))

print(int(8.9))

# any number divided by itself and 1 will return modulo 0...

# break the loop ONCE we find a value that returns modulo > 0

# true is prime
# false is 

# input ->

# need to understand what are prime numbers...

# prime -> greater than 1
# check this with if statement

# prime -> no divisor besides 1 and itself


# output -> T/F if integer is prime