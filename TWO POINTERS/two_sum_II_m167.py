"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

12/2/2022

2 pointers, use the fact that the list is sorted to your advantage
video.assist

--- PROMPT ---


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
use the fact that the list is sorted to your advantage

"""


# --- MY SOLUTION ---
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # time complexity O(n)
        
        # use the fact that these elements are sorted to our advantage

        # initialize two pointers based on index
        l = 0
        r = len(numbers) - 1

        # loop thru
        while l < r:
            curSum = numbers[l] + numbers[r]

            # if curr sum is too large, we know that the right pointer's value will never be part of soln
            # decrement the right pointer
            if curSum > target:
                r -= 1

            # if curr sum is smaller than target, than the left pointer will never be part of soln
            # increase left pointer
            if curSum < target:
                l += 1

            # if curSum matches target
            if curSum == target:
                #indeces are 'weird' here. first item is 1st index.
                # therefore increase indexes
                return [l+1, r+1]

# --- TEST ---


# --- ALT SOLN by others ---
