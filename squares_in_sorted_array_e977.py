"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/

1/12/2022

--- PROMPT ---
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



--- LESSONS ---
refresher on list comprehension

--- QUESTIONS ---

--- PSEUDOCODE ---




"""
# --- MY SOLUTION ---
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        """
        brute force is:
        loop thru the list, squaring each element
        Then sorting the subsequent list

        That would be O(N*Log(N)) worst case

        """
        sqrd = [x**2 for x in nums]
        sqrd.sort()
        return sqrd
# --- TEST ---


# --- ALT SOLN by others ---
