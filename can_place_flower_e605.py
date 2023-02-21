"""
https://leetcode.com/problems/can-place-flowers/

2/18/2023

--- PROMPT ---

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

input - flowerbed array, and integer for new flowers


output - t/f if the add'l flowers will violate rule:
rule - flowers cannot be planted in adjacent plots

iterate thru the array with 1 pointer, looking 2 ahead.
only iterate length-3 times. 

if value is 1.
check next - if 1 - return False
check 2 values away -if 0, turn to 1. elif 1. do nothing.

if value is 0.
check next - if 1 - do nothing. if 0, check 2 values away (if 0 - turn next to 1)
check 2 values away - if 1 - return false

n can be 0

lesson - no need for pointers - just the indeces to your advantage


--- process here ---
NC - believes this is more of a medium difficulty
Recognize if the first part is 1, or the first part is 0, and then move forward.
Assuming that the left, and right indeces of the array, outer bound, are value '0'
like this... 0 [0, 0, 1] 0

if the element to the left and to the right of a point is 0, plant flower

time: O(n)
space: O(n)


"""
# --- MY SOLUTION ---
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # increase space complexity, by adding 0 in the beginning and end
        f = [0] + flowerbed + [0]

        length = len(f)

        for i in range(1, length -1): # skip first and last
            if f[i-1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        
        if n <= 0:
            return True
        return False


# --- TEST ---


# --- ALT SOLN by others ---
