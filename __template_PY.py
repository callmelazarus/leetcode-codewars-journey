"""
https://leetcode.com/problems/last-stone-weight/description/

3/26/2023

--- PROMPT ---
Given an array of integers, where all elements but one occur twice, find the unique element.

Example

The unique element is .

Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers
Returns

int: the element that occurs only once
Input Format

The first line contains a single integer, , the number of integers in the array.
The second line contains  space-separated integers that describe the values in .

Constraints

It is guaranteed that  is an odd number and that there is one unique element.
, where .

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
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
"""
loop thru list, counting the number of times a number exists

loop thru that dictionary, and see if a number has a count of 1
return that number

time: O(n)
space: O(n)
"""
def lonelyinteger(a):
    # Write your code here
    counter = {}
    for letter in a:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    for key, value in counter.items():
        if value == 1:
            return key

# --- TEST ---


# --- ALT SOLN by others ---
