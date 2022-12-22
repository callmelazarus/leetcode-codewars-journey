"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

12/20/2022
go backwards!

--- PROMPT ---
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



--- LESSONS ---
insert function allows you to add to the beginning of a lit

--- QUESTIONS ---

--- PSEUDOCODE ---

Loop thru the problem, starting with the back
keep track of the max value that you've seen in the past, and update it as you need to
insert the max into the beginning of the array, greating the solution array

"""
# --- MY SOLUTION ---
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]

        """
        # intiailze solution with the -1 at the end
        soln = [-1]

        # keep track of max
        max_val = 0
        # go backwards in array - we don't actually need to go to the first index, since it's size is never checked. This results in the second parameter being 0.
        for i in range(len(arr)-1, 0, -1):
            # calc the max value. If the value we see is the max
            max_val = max(arr[i],max_val)
            # insert the max value in the beginning of list
            soln.insert(0,max_val)

        return soln


# --- TEST ---


# --- ALT SOLN by others ---
