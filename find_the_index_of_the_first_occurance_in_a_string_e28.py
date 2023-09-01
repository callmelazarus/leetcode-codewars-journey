"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

8/31/2023

--- PROMPT ---
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.ß
ß
--- LESSONS ---
- did use chatgpt for assistance here
- writing things out in notes did help
- recognizing that I need to stay in bounds during the iteration was key

--- QUESTIONS ---

--- PSEUDOCODE ---


"""
# --- MY SOLUTION ---
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        
        input - 2 arguments - haystack (string) and needle (string)

        output - index of needle within haystack / -1 if needle isn't inside haystack. return first occurance of match.

        brute force:
        store index 

        iterate thru each char in haystack
        if match with first index in needle, move to next char for both haystack and needle
        check next var if matches
        if match, keep progressing
        if you get to the end of needle, return stored index

        if a mismatch occurs, update the stored index 
        and start iteration thru needle again

        feeling like it could be high time complexity

        """
        # needle_length = len(needle)
        # hay_length = len(haystack)
        # # loop thru the char in the word

        # exploring iterating thru the needle, instead of the haystack

        # for i in range(needle_length):
        #     count = 0
        #     for j in range(hay_length):
        #         if needle[i] == haystack[j]:
        #             count += 1
        #             continue
        #         elif count == needle_length:
        #             return j
        #         else:
        #             break
            
        # return index

        # time: O((n-m+1) * m) where m is needle length - polynomial
        # space: O(n) constant

        needle_length = len(needle)
        hay_length = len(haystack)
        # iterate thru HACKSTACK - but not going out of bounds when searching needdle
        for i in range(hay_length - needle_length + 1):
            found = True
            # iterate thru NEEDLE, checking to see if the 
            for j in range(needle_length):
                # if MISMATCH is found
                if haystack[i + j] != needle[j]:
                    found = False
                    break
            # if found == true, return i
            if found:
                # 'i' retains the position in haystack
                return i
        
        return -1  # Return -1 if needle is not found


# --- TEST ---


# --- ALT SOLN by others ---
