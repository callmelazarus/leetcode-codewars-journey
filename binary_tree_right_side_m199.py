"""
https://leetcode.com/problems/binary-tree-right-side-view/description/

1/16/2022
binary search

--- PROMPT ---
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        Need to visualize the array before writing code. 
        Recognize the patterns that are present

        This algo uses binary search, and addresses the problem with not knowing which side of the mid index to search by comparing the target with the nums[mid] and the nums[l], nums[r].

        Recognizing that pattern allows you to recognize which side to search.

"""
# --- MY SOLUTION ---
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        """
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l + r) //2
            
            #base case
            if target == nums[mid]:
                return mid
            # 2 example cases, notice how the left and right sorted sides 
            # are with respect to either the left or right num

            # [4, 5, 6, 7, 1, 2, 3]
            # [7, 1, 2, 3, 4, 5, 6]

          # check if in left sorted portion

            if nums[l] <= nums[mid]:
                
                # check right side
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1

            # target is less than middle, but greater the left. search the left portion
                else:
                    r = mid -1
            
            # check right sorted portion
            else:
                # check left side
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    # just search right portion
                    l = mid + 1
        return -1

# --- TEST ---


# --- ALT SOLN by others ---
