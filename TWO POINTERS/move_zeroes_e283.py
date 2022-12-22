"""
https://leetcode.com/problems/move-zeroes/description/

12/21/2022
2 pointers
clever - think of another way to cleverly solve the problem. 
move all non-zeros to the beginning of list (same question, asked differently)


--- PROMPT ---
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        

        bubble up the zero by pushing non-zeros to left side, this will result in a list with zeros on the right end
        swap elements if non zero value is found (this pushes non-zero val to beginning of list)
        if zero is seen, don't swap it

        time: O(n)
        space: sorted list in place


"""
# --- MY SOLUTION ---
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        """
        n = len(nums)

        l = 0

        for r in range(n):
            # if number is not zero, swap it 
            # this will push all non-zero values to the left of the list
            if nums[r] != 0:
                nums[r], nums[l]= nums[l], nums[r]
                l +=1


# --- TEST ---


# --- ALT SOLN by others ---
