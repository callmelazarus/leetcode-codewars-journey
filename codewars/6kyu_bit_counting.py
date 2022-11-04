"""

Date:  8/3/2022

Write a function that takes an integer as input, and returns the
number of bits that are equal to one in the binary representation of 
that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, 
so the function should return 5 in this case
"""
"""
to turn something to binary:
you need to divide the num by 2. the remainder
"""


def count_bits(n):
    binary_list = []
    while n/2 >= 1 or n%2 == 1:
        binary_list.append(n%2)
        n = n//2 # 
    print(binary_list)
    print(sum(binary_list))



# bin function. string count method

def count_bits_clever(n):
    return bin(n).count("1") 



    # turn n into binary
    # need to select the right loop....
    # number % 2 -> add to into list
    # if modulo 2 == 0 -> end loop / break

    # sum list


count_bits(13)