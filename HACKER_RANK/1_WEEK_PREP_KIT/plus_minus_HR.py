"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

1/31/2022
Arrays

--- PROMPT ---
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.


--- LESSONS ---
How to print something to the 6th decimal place using .format
https://docs.python.org/3/library/stdtypes.html#str.format
    print('{0:.6f}'.format(zero/total))

--- QUESTIONS ---

--- PSEUDOCODE ---
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
Based on that array, we need to figure out how many pos, negative, and zeros there are
- Print out ratios of these values to the 6 places after decimal

process:
iterate to count pos / neg / zero
take ratio of pos/total, etc. and print them
find out how to show value to the 6th dec point
Time: O(N)
SPACE: O(1)
"""
# --- MY SOLUTION ---

#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0 
    for item in arr:
        if item > 0:
            pos += 1
        elif item < 0:
            neg += 1
        else:
            zero += 1
    total = pos + neg + zero
    print('{0:.6f}'.format(pos/total))
    print('{0:.6f}'.format(neg/total))
    print('{0:.6f}'.format(zero/total))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

# --- TEST ---


# --- ALT SOLN by others ---
