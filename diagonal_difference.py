"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two
3/4/2023

--- PROMPT ---
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
sum total for left diag
sum total for right diag
find the length of the array, and ajust to zero index

loop thru the list once to build the sum total of the left, from 0 -> length -1
loop thru list to build the sum total of the right, from length-1 -> 0

abs difference




"""
# --- MY SOLUTION ---

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
"""

"""
def diagonalDifference(arr):
    # Write your code here
    l = 0
    r = 0
    n = len(arr)
    print(n)
    
    for i in range(0,n):
        l += arr[i][i]
    
    count=0
    for i in range(n-1,-1,-1):
        if count < n:
            r += arr[count][i]
            count += 1
    
    return abs(r-l)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



# --- TEST ---


# --- ALT SOLN by others ---
