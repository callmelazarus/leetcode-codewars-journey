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
# Complete the 'findMaxDistinctItems' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#
"""
n items in cart
cost of ith item is 'i' dollars
m items have been bought, represented in array arr
k dollars

return - int - max number of distinct items one can have IN TOTAL, after purchasing any number of items from k

ex:
n = 10 items
m = 3 items already bought - represented in array
k = 10
arr [1, 3, 8] - already purchased items - you can not include these

initialize counter (which we will add with m at the end)
iterate from 0 to n items
we want the maximum total items that we can purchase, less than 'k' dollars
if value is found in arr - skip to next value
if value is not found in arr - 
    reduce k by value
    check if k is positive
        increase counter 
     once k is negative
        return counter + m
return m if the prev return never fires

"""

def findMaxDistinctItems(n, k, arr):
    # Write your code here
    
    count = 0
    print('k: ', k)
    print('n: ', n)
    m = len(arr)
    print('array: ', arr)
    for i in range(1,n+1):
        if i not in arr:
            k -= i
            if k >= 0:
                count += 1
                print('count: ', count)
                print('k: ', k)
            else:
                total = count + m
                return total
    return m
                
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = findMaxDistinctItems(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()



# --- TEST ---


# --- ALT SOLN by others ---
