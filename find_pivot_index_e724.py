"""
https://leetcode.com/problems/find-pivot-index/description/

12/5/2022

Something like three pointers
Calculate the sum 1 time, and evaluate sum comparisons as you loop
sum fxn is O(n) time. 

--- PROMPT ---
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

--- LESSONS ---
exercise with list splicing
sum fxn in python is O(n) time

--- QUESTIONS ---

--- PSEUDOCODE ---
Loop thru the list, evaluating the sum to left and right of pivot
return pivot when sums match
"""


# --- MY SOLUTION ---
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # O(n) time
        # O(1) space
        
        # initialize sum values
        left = 0
        mid = 0
        right = sum(nums) # O(n), ran one time
        
        # loop thru the nums
        for i in range(len(nums)):
            # slowly build up the left sum based on pivot value (nums[i])

            # slowly reduce the right sum based on pivot value (nums[i])
            left += mid # slowly increase the sum of the left 
            mid = nums[i]
            right -= nums[i] # slowly decrement the sum value to the right
            if left == right:
                return i
        
        return -1

        # return leftmost pivot, if no pivot exists, return -1
        # pivot defined: values to left sum to values on right

        # loop thru the list
        # consider splicing, and comparing the sums

        # sum function, is linear time complexity, and therefore makes this problem too slow...
        # this solution is n^2

        # for i in range(0, len(nums)):
        #     left_sum = sum(nums[0:i])
        #     right_sum = sum(nums[i+1:])
        #     if left_sum == right_sum:
        #         return i
        # return -1


# --- TEST ---


# --- ALT SOLN by others ---
