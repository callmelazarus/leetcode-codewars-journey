"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

2/1/2023
arrays
loops

--- PROMPT ---
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---


# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
input is array of numbers

sum of just 4 of the 5 elements to create min and max

process:
Sum all values.
Create solution list
iterate thru list, subtracing values and adding to soln list

find min and max from soln list
output

output -> Print two space-seperated integers with min and max values


"""
# --- MY SOLUTION ---
#!/bin/python3

import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    sum_all_values = sum(arr)
    soln_set = []
    for item in arr:
        soln_set.append(sum_all_values - item)
    min_value = min(soln_set)
    max_value = max(soln_set)
    print(min_value, max_value)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


# --- TEST ---


# --- ALT SOLN by others ---
