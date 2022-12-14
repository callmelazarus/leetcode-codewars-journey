"""
https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan&id=level-1

12/12/2022, 12/13/2022

--- PROMPT ---

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
--- LESSONS ---
you can run for loops, lengths, indexes on strings@

--- QUESTIONS ---

--- PSEUDOCODE ---
strings are isomorphic if they are isomorphic on both directions
Build a map that maps the changes between strings (do this as you loop thru strings)

if you notice that the character is in the map, and it DOESN'T map to the corresponding char, then you return false
otherwise, keep building your map

if you get thru the entire list without triggering the False return, then return True

"""


# --- MY SOLUTION ---
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        """
        # build the map assosications between the strings
        mapST = {}
        mapTS = {}
# you can loop thru two strings of same length at the same time using zip()
# for c1, c2 in zip(s, t)

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            # need to check if the varied mapping (returning false)
            # we need to do this check 
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False

            # the order of where you put this matters (it can't be placed before the if statement)
            mapST[c1] = c2
            mapTS[c2] = c1
        return True

"""
        My solution at first:
        Tricky solution:
        manipulate one string against the other string
        and then in the end, check if the two strings are the same

        failing case:
        s = 'badc', t = 'baba'

        my original solution... figured this out on my own, but it didnt work
        if len(s) != len(t):
            return False

        rev_t = t
        for i in range(len(t)):
            prefix_t = rev_t[:i]
            postfix_t = rev_t[i:]
            postfix_t = postfix_t.replace(t[i],s[i])
            rev_t = prefix_t + postfix_t

        rev_s = s
        for i in range(len(s)):
            prefix = rev_s[:i]
            postfix = rev_s[i:]
            postfix = postfix.replace(s[i],t[i])
            rev_s = prefix + postfix


        print(rev_s, t)
        print(rev_t, s)
        if rev_s == t and rev_t == s:
            return True
        return False
        """

# --- TEST ---
a = Solution()
b = a.isIsomorphic('paper', 'title')
print(b)

# --- ALT SOLN by others ---
