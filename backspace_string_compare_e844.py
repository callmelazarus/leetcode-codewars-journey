"""
https://leetcode.com/problems/backspace-string-compare/description/

12/1/2022

--- PROMPT ---
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        # create lists that you eventually compare things with.
        # when you see a #, pop the last item in the list
"""


# --- MY SOLUTION ---
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # O(n), O(n) space...
        # create lists that you eventually compare things with.
        # when you see a #, pop the last item in the list

        s_final = self.cleantext(s)
        t_final = self.cleantext(t)
        if s_final == t_final:
            return True
        return False

    # cleanup text, based on #
    def cleantext(self, s):
        s_final = []
        for i in s:
            if i != '#':
                s_final.append(i)
            else:
                # catch edge case where # is first item in list
                try:
                    s_final.pop()
                except:
                    continue
        return s_final

# --- TEST ---


# --- ALT SOLN by others ---
