"""
https://leetcode.com/problems/longest-common-prefix/
11/22/2022

--- PROMPT ---


--- LESSONS ---

--- QUESTIONS ---

"""


# --- MY SOLUTION ---
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # input: list of strings
        # need to identify the prefixes that are common accross the same strings
        # build dictionaries with the first few letters of each element
        # return key:value pair with the largest value

        # output: string
        d_soln = {}
        if strs == [""]:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        for word in strs:
            if word[0] in d_soln:
                d_soln[word[0]] += 1
                
            if word[0] not in d_soln:
                d_soln[word[0]] = 1
                
            if word[0:2] in d_soln and len(word)> 1:
                d_soln[word[0:2]] += 1
                
            if word[0:2] not in d_soln and len(word)>1:
                d_soln[word[0:2]] = 1
                
            if word[0:3] in d_soln and len(word)>2:
                d_soln[word[0:3]] += 1
                
            if word[0:3] not in d_soln and len(word)>2:
                d_soln[word[0:3]] = 1
        print('dictionary soln:', d_soln)
        max_value = 0
        max_char = ''

        for key, value in d_soln.items():
            if value >= max_value:
                max_value = value
                max_char = key
        if max_value == 1:
            return ""
        return max_char
                


# --- PSUEDOCODE ---
"""




"""
# --- TEST ---



# --- ALT SOLN by others ---
