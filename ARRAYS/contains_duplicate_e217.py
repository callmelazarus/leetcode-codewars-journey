"""
https://leetcode.com/problems/contains-duplicate/

11/18/2022

--- PROMPT ---
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

--- LESSONS ---
- sort fxn in python is time complexity O(nlogn)
- set function in python has a O(1) time complexity, worst case O(n), with space complexity of O(n)



--- QUESTIONS ---

"""


# --- MY SOLUTION ---
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        revised_set = set(nums)
        if len(nums) == len(revised_set):
            return False
        return True



# --- PSUEDOCODE ---
"""
        # input - numbers
        # converting list to set, and compare lengths

        # output - true or false. True: if values appear at least twice. False if element is distinct


"""
# --- TEST ---



# --- ALT SOLN by others ---
