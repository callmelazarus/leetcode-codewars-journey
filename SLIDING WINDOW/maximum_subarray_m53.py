"""
https://leetcode.com/problems/maximum-subarray/

4/9/2023
sliding window / greedy

--- PROMPT ---
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.


--- LESSONS ---
again give it some time, you can solve these problems


--- QUESTIONS ---

--- PSEUDOCODE ---
worst case condition is O(N^3) - where you have to build out the sums multiple arrays 

remove negative pre-fixes (sliding window)
O(N)

"""
# --- MY SOLUTION ---
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # initialize the max subarray
        maxSub = nums[0]

        # set current sum
        curSum = 0

        for n in nums:
            # if the current sum is negative, reset curSum to 0 (no need to keep track of neg values)
            if curSum < 0:
                curSum = 0
            
            # add the current value to curSum (at this point, curSum could be 0)
            curSum += n

            # set maxSub to be the max of either the maxSum or curSum
            maxSub = max(maxSub, curSum)
        return maxSub



# --- TEST ---


# --- ALT SOLN by others ---
