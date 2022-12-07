"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

12/6/2022

recursive solution, recognize that selections involve either adding or not adding the next character in the list
backtracking process

--- PROMPT ---
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



--- LESSONS ---
backtracking solution:
https://www.youtube.com/watch?v=d4SPuvkaeoo

Recursive soln:
https://www.youtube.com/watch?v=inrvpFusxf8

--- QUESTIONS ---

--- PSEUDOCODE ---


# return the length of the longest length of string concat
"""


# --- MY SOLUTION ---
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """

        # the use of self.ans is still perplexing to me

        n = len(arr)
        self.ans = 0

        def recurse(s, i):

            # base case 
            if i >= n:

                # check if duplicates exist
                if len(s) == len(set(s)):
                    self.ans = max(self.ans, len(s))
                return 

            # recurse, for the next element, with no change to string
            recurse(s, i+1)

            # product new string -> string, plus the current word
            new_string = s + arr[i]

            # check if duplicates exist, to optimize soln to reduce recursive steps
            if len(new_string) == len(set(new_string)):
                # call recurse with new string
                recurse(new_string, i+1)
        
        # call recursion with empty string
        recurse("", 0)
        return self.ans


# --- TEST ---


# --- ALT SOLN by others ---
