"""
https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan&id=level-1

12/12/2022

--- PROMPT ---

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
--- LESSONS ---
you can run for loops, lengths, indexes on strings@

--- QUESTIONS ---

--- PSEUDOCODE ---

"""


# --- MY SOLUTION ---
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        hash table solution apparently

Tricky solution:
manipulate one string against the other string
and then in the end, check if the two strings are the same

failing case:
s = 'badc', t = 'baba'

Hash solution

        """
        if len(s) != len(t):
            return False

        rev_t = t
        for i in range(len(t)):
            rev_t = rev_t.replace(t[i],s[i])

        rev_s = s
        for i in range(len(s)):
            rev_s = rev_s.replace(s[i],t[i])
        print(rev_s, s)


        print(rev_t, t)
        if rev_s == t and s == rev_t:
            return True
        return False

# --- TEST ---
a = Solution()
b = a.isIsomorphic('paper', 'title')
print(b)

# --- ALT SOLN by others ---
