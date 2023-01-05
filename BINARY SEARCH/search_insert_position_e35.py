"""
https://leetcode.com/problems/search-insert-position/description/

1/4/2022
binary search

--- PROMPT ---
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
perform basic binary search

consider where l and r are at the end of the loop.
Based on that, present the index solution

"""
# --- MY SOLUTION ---
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        """
        l = 0
        r = len(nums) - 1
        mid = (l + r) //2

        # simple binary search
        while l < r:
            if target == nums[mid]:
                return mid

            mid = (l+r)//2

            # if target is larger than mid - check right
            if target > nums[mid]:
                l = mid +1
            # if target is less than mid - check left
            if target < nums[mid]:
                r = mid 
        
        # at this point l == r
        # catch the case when target isn't in the nums list
        print(l, r)
        if target > nums[l]:
            return l + 1
        return l


        
            

# --- TEST ---


# --- ALT SOLN by others ---
