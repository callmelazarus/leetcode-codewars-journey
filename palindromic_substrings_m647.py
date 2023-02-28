"""
https://leetcode.com/problems/palindromic-substrings/

2/27/2023
dynamic programming

--- PROMPT ---
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        need to cover even and odd cases

        brute force: O N^3
        ON^2 to search all substrings. and then another O(N) to check if palindromi - thus - O (N^3)

        More efficient is O N^2:
        (considers odd length palindroms 1, 3, 5, etc)when at a char, consider how many substrings invovle that as the middle of the substring, and 'go outward'. A char on its own will always be a palindromic substring (eg. 'a' is a palindrome)

        (consider even length palindroms 2, 4, 6, etc). Observe two chars at a time, and then grow outward.




"""
# --- MY SOLUTION ---
class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        # run this operation for each char of the string
        for i in range(len(s)):
            l = r = i
            # cover odd length palindromes. If it is a palindrome, and the pointers are in bound
            while l >= 0 and r < len(s) and s[l]==s[r]:
                res += 1
                l -= 1
                r += 1
        
            # cover even length palindromes
            # l and right pointers are now at 2 neighboring values
            l = i
            r = i + 1
            # again, checking if pointers are in bound, and if they are palindromic
            while l >= 0 and r < len(s) and s[l]==s[r]:
                res += 1
                l -= 1
                r += 1

        return res


# --- TEST ---


# --- ALT SOLN by others ---
