"""

https://leetcode.com/problems/house-robber-ii/

3/31/2023
dynamic programming
related to house robbing 1

--- PROMPT ---
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

--- LESSONS ---
solving these problems - you need to first figure things out without coding, and then present 
solution in code.

this problem shows the process of updating 2 variables, using 3 variables.
You calculate a variable (say v3)
you update v1 = v2
then update v2 = v3 (the variable you just updated)

--- QUESTIONS ---


--- PSEUDOCODE ---

Houses are now arranged in a circle.
if we rob the zeroth index, we can't rob the last index, and vice versa.


time - O(N)
space O(1)


"""
# --- MY SOLUTION ---
class Solution:
    def rob(self, nums: List[int]) -> int:
        # conditions to check
        # consider if the list is just 1 value long
        # skip first house
        # skip last house
        return max(nums[0],
        self.helper(nums[1:]),
        self.helper(nums[:-1]))
        

    def helper(self, nums):
        # store max amount you can store 
        rob1, rob2 = 0, 0

        for n in nums:
            # store max values 
            newRob = max(rob1+ n, rob2)
            rob1 = rob2
            rob2 = newRob

            #rob2 will contain the max rob
        return rob2



# --- TEST ---


# --- ALT SOLN by others ---
