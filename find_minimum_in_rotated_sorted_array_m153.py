"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

1/4/2023 
binary search
helper function
recursion


--- PROMPT ---
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---




"""
# --- MY SOLUTION ---
class Solution:
    def findMin(self, nums):
        """
        input -> list of int, rotated

        output -> return smallest int

        key: an inflection point must exist, when the numbers no longer increase

        conditions:
        O(log n) - use binary search

        the first and last numbers tell you something
        if the last value is smaller than first value, smaller value on right side

        Ex 1:
        0 1 2 3 4 5 6

        1 2 3 4 5 6 7 : L - > easy, unsorted -> first item
        2 3 4 5 6 7 1 : R -> if first val is less than mid -> check right
        3 4 5 6 7 1 2 : R
        4 5 6 7 1 2 3 : R
        5 6 7 1 2 3 4 : Mid
        6 7 1 2 3 4 5 : L -> if first val is greater than mid -> check left

        Ex case 2
        0 1 2 3 4 5 6

        4 5 6 7 0 1 2 : R => 
                0 1 2 : init is answer

        if the last value is less than first value, it is rotated

        if first value is less than midpoint, check right side, otherwise, check left side

        base case
        if you check the midpoint, and value before it is greater, then you found the min!

        establish l and r
        find mid

        check mid against first value to determine if you check right side,
        or left side

        """
        # check unsorted case
        if nums[0] < nums[-1]:
            return nums[0]

        def helper(l, r):
            mid = (r + l) // 2
            # print('mid', mid)
            # print('l:', l)
            # print('r:', r)
            # print(nums[mid-1]> nums[mid])

            # base case
            if nums[mid-1] > nums[mid]:
                # print('here')
                # print(nums, nums[mid], mid)
                return nums[mid]

            
            if nums[l] < nums[r]:
                # print('here 2')
                # print(nums, nums[l], l)
                return nums[l]

            # check right side if initial val smaller than mid 
            if nums[l] < nums[mid]:
                # check right side
                helper(mid +1, r)
            
            # check left side
            if nums[l] > nums[mid]:
                helper(l, mid)
        
        return helper(0, len(nums)-1)


        

# --- TEST ---
b = [3, 4, 5, 1, 2]
a = Solution()
a.findMin(b)


# --- ALT SOLN by others ---
