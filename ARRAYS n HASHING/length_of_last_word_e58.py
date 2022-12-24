"""
https://leetcode.com/problems/length-of-last-word/description/

12/23/2022
array
not hard, likely not worth re-doing

--- PROMPT ---
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

        input - string

        need to find out last word
        find length

        split the string, with ' ' as the seperator
        Take the value of the last element in the string, and find it's length
        
        If spliting it results in empty elements in the list, loop backwards, and return the first non-empty string length
        
        output - int


"""
# --- MY SOLUTION ---
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        """

        a = s.split(" ")
        print(a)
        for i in range(len(a)-1,-1,-1):
            if len(a[i]) == 0:
                continue
            return len(a[i])


# --- TEST ---


# --- ALT SOLN by others ---
