"""
https://leetcode.com/problems/valid-anagram/description/
11/5/2022
TIME: Actually took me about 15 min..

--- PROMPT ---
        # s and t are strings.
        # return true if t is an anagram of s. Return false otherwise.
        # break string into a list of indiviual letters
        # loop letter, to see if letter is in the 't'
        
        # create dictionary of key/value pairs, with key being letter, and value being
        # number of letters
        # do this for both strings. 
        # check to see if the dictionaries match

--- LESSONS ---
You can actually check to see if one dictionary is equal to another dictionary
You can check to see if something is in a dictionary using 'in'
"""



# --- MY SOLUTION ---
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        print('s',s)
        d_s = {}
        d_t = {}
        for letter in s:
            if letter not in d_s:
                d_s[letter] = 1
            else:
                d_s[letter] += 1
        for letter in t:
            if letter not in d_t:
                d_t[letter] = 1
            else:
                d_t[letter] += 1
        if d_s == d_t:
            return True
        return False





# --- PSUEDOCODE ---
"""
        # s and t are strings.
        # return true if t is an anagram of s. Return false otherwise.
        # break string into a list of indiviual letters
        # loop letter, to see if letter is in the 't'
        
        # create dictionary of key/value pairs, with key being letter, and value being
        # number of letters
        # do this for both strings. 
        # check to see if the dictionaries match

        space = O(N) - dictionary will grow dependent on the size of the input

        time: O(N) - iterate thru each element to build dictionary


"""
# --- TEST ---



# --- ALT SOLN by others ---
