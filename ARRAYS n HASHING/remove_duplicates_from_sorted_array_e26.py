"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

3/15/2023

arrays, two pointers
--- PROMPT ---
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.



--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
use 2 pointers to consider if a value is 


"""
# --- MY SOLUTION ---
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # time: O(N)
        # Space: O(1) - no new memory

        n = len(nums)
        # represents how many unique values there are. This will increment whenever we see a unique value
        insertIndex = 1

        # start at the 1st index (2nd number in list)
        for i in range(1, n):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array with that value
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex += 1       
        return insertIndex



# --- TEST ---


# --- ALT SOLN by others ---
