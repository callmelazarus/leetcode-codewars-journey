"""
https://leetcode.com/problems/binary-search/

11/5/2022

--- PROMPT ---
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


--- LESSONS ---


--- QUESTIONS ---
Trick is - how do I return the INDEX of the targeted number


"""


# --- MY SOLUTION ---
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # the trick is - hwo 
        if target not in nums:
            return -1
        else:

            if len(nums) == 1:
                return mid_index

            n = len(nums)
            mid_index = n//2
            left = nums[0:mid_index]
            right = nums[mid_index:n]

            if target in left:
                search(left, target)
            else:
                search(right, target)


# --- PSUEDOCODE ---
"""
# taking in list, and a target value (int).
# return index of the value. 
# return -1 if the value is not in the list

quick check, if target not in list -> return -1

establish middle, and check if target is in right or left

if in right -> find another middle and check if target is in right or left

end of the line - if if you are left with 1 element. on left or right

"""
# --- TEST ---



# --- ALT SOLN by others ---
