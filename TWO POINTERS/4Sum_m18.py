"""
https://leetcode.com/problems/4sum/

12/3/2022

--- PROMPT ---
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

--- LESSONS ---
https://www.youtube.com/watch?v=EYeR-_1NRlQ
- neetcode does a recursive solution


--- QUESTIONS ---


--- PSEUDOCODE ---

O(n^3)

"""


# --- MY SOLUTION ---
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # sort array
        nums.sort()

        res, quad = [], []

        # helper function
        def kSum(k, start, target): # k in this case is 4, but can be flexible for larger sums
            
            # start with (non) base case
            if k != 2:

                # iterating the the entire array, except for the last k values (so that they can be picked later)
                for i in range(start, len(nums) - k + 1):
                    
                    # if duplicates exist, we should continue (we don't want this to fire in the begining, since there is no previous value)
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i + 1, target - nums[i])
                    quad.pop()
                return

                # base case, see LC two sum II for logic here

            # initialize the two pointers, left and right
            l, r = start, len(nums)-1
            
            while l < r:
                # if sum is less than target
                if nums[l] + nums[r] < target:
                    # increment left pointer bc sum is too small
                    l += 1
                     
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    # add nums[l] and nums[r] to the results list
                    res.append(quad + [nums[l], nums[r]])
                    
                    # update the left and right pointers to avoid duplicats
                    # arbitrarily update the left pointer (could b ethe right)
                    l += 1
                    # avoid selecting a duplicate, or go out of bounds (l < r)
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        # call the recursive function, with k = 0
        kSum(4, 0, target)

        # return soln list
        return res


# --- TEST ---


# --- ALT SOLN by others ---
