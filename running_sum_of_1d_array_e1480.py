"""
https://leetcode.com/problems/running-sum-of-1d-array/description/

12/5/2022

loop, mutate list
easy

--- PROMPT ---
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

"""


# --- MY SOLUTION ---
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

    # calculate a running sum of values

    # loop thru the solution, continually adding the sums from prev values
    
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums

# --- TEST ---


# --- ALT SOLN by others ---
