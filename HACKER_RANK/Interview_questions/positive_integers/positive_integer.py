"""
https://leetcode.com/problems/last-stone-weight/description/

3/26/2023

--- PROMPT ---



--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---




"""
# --- MY SOLUTION ---
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getOptimalValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

"""
return - minimized max value, after performing the operations noted 

input an array of certain numbers.
Select a range - struggled to understand how the range is formed here both the l and right

iterate thru that range, with index i
update the array[l+i] with arr[l+i] & arr[r-i] operation
return the max value of that resulting array
"""

def getOptimalValue(a):
    # Write your code here
    print('a: ', a)
    r = len(a)
    print('r: ', r)
    for i in range(0,r):
        print(a[i])
        a[i] = a[i] & a[r-1-i]
    return max(a)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = getOptimalValue(a)

    fptr.write(str(result) + '\n')

    fptr.close()




# --- TEST ---


# --- ALT SOLN by others ---
