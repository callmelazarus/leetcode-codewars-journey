"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

12/5/2022

sliding window - (2 pointers in a sense)

--- PROMPT ---
Given a string s, find the length of the longest 
substring without repeating characters.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
Think about how the window/range slides accross the array

process is building a set as you loop thru the string
if there is a duplicate, than we remove the values from the leftmost pointer
if no duplicates, we just keep advancing, and building the set
the solution is the length between pointers (right - left + 1).
why the plus one? -> if you have two letters in set (a, b)-> you should have 2,
but if you only had right - left, that would be 1 - 0 -> resulting in 1.
if you have three letters in set (a, b, c) -> 2 index - 0 index -> results in 2

"""


# --- MY SOLUTION ---

# O(n) time
# O(n) space - bc of set we are creating a set

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # initialize new set (no duplicates), which will hold the substring
        charSet = set()
        
        #setup pointers for sliding window
        # left pointer is here
        # right pointer, in for loop
        l = 0
        soln = 0 

        for r in range(len(s)):
            # if the char we are looping thru, exists within the charSet (duplicate exists) 
            # we are doing a while loop, since we are going to keep doing a loop based on if a certain conditions is met (pushing left pointer if duplicates are found)
            while s[r] in charSet:
                #remove leftmost char, which holds the duplicate
                charSet.remove(s[l])
                # increase the left pointer by one 
                l += 1
            # add the char associated with right pointer, to Char Set
            charSet.add(s[r])
            # update the solution, which is the max of the soln, and (sliding window length)
            # this will keep track of the largest set that we may have passed
            soln = max(soln, r-l+1)
        print('charset:', charSet)
        return soln

# --- TEST ---
a = Solution()
s = "abcabcbb"
soln = a.lengthOfLongestSubstring(s)
print(soln)

# --- ALT SOLN by others ---
