"""
https://leetcode.com/problems/longest-palindromic-substring/

video.assist

1/20/2022
arrays
two pointer
sliding window
clever conditionals
edge cases are even and odd lengths

--- PROMPT ---
Given a string s, return the longest palindromic substring in s.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

--> Brute force. 
Scan each substring, and check if substring. 
Creating substring is time O(n^2), and checking it is O(n). Therefore, altogether, that would be O(n^3)
        
--> More efficient palindrome solution:
        time: O(n^2)
        space = O(1)

        intution is you iterate thru each char in the string.
        And you then iterate outside of that char (using a left and right pointer)
        if the left and right are the SAME (and you are in bounds), you are on your way to building a palindrome
            if the lenght of this condition (r - 1 + 1) is bigger than current resLen
                update the result and the result length
        
        There needs to be a case that covers the even and odd string lengths


"""
# --- MY SOLUTION ---
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        # loop thru each element in the list
        for i in range(len(s)):
            # check odd length palindrome

            # initalize the left and right pointers
            l, r = i, i
            # check to ensure l and r are within the boundaries, and IF they are equal
            while l >= 0 and r < len(s) and s[l] == s[r]:
            # if you find the palindrome that his larger than what you found before
                if (r - l + 1) > resLen:
                    # update the res, and resLength
                    res = s[l:r+1]
                    resLen = r - l + 1
                # increment your left and right pointers
                l -= 1
                r += 1
            # if none of these are true, we move onto the next character in the string, and repeat the process

            # check even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
            # if its the largest palindrome
                if (r -l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        return res


# --- TEST ---


# --- ALT SOLN by others ---
