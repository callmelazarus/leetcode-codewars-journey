"""
https://leetcode.com/problems/is-subsequence/description/

12/20/2022
2 POINTER
array

--- PROMPT ---
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---



"""
# --- MY SOLUTION ---
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        pointer for s and t
        advance the pointer on t, if there isn't a match
        if you get to the end of t, but don't get to the end of s, return false
        """
        if len(s)==0:
            return True

        s_pointer = 0
        t_pointer = 0

        # advance the t pointer until we get to the end of the t
        # need to ensure that we don't get out of range on the s list
        while t_pointer < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            # keep advancing the t_pointer if a match doesn't occur
            else:
                t_pointer += 1
        
        # if the s pointer gets to the end of the array
        if s_pointer == len(s):
            return True
        return False

# --- TEST ---


# --- ALT SOLN by others ---
