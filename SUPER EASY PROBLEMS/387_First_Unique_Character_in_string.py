"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=prshgx6i

6/28/2025

--- PROMPT ---



--- LESSONS ---
- it just felt good to accomplish this one, it's been a long while since I've done some



--- QUESTIONS ---

--- PSEUDOCODE ---




"""
# --- MY SOLUTION ---

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        return -> index of first non-repeating char
                    -1 (if there is no repeating char)

        need to iterate thru entire string to see if anything is present
        create a map -> where we can see if there are any repeat characters
        iterate again - checking to see if that letter has a count of 2 -> then return the index of the next character
        if the next character does not exist - return -1

        first NON repeeating character

        leetcode (l), 0
        loveleetcode (v), 2
        """
        
        # lets create that map
        mappy = {}

        for char in s:
            if char in mappy:
                mappy[char] += 1
            else:
                mappy[char] = 1


        # for index, item in enumerate(s):
        #     if mappy[item] > 1:
        #         return index - 1

        # check if value is greater than 1
        # if so -> move on
        # if it is one, then return that index
        for index, char in enumerate(s):
            if mappy[char] > 1:
                continue
            print(index)
            print(char)
            return index

        return -1


        print(mappy)

        


# --- TEST ---


# --- ALT SOLN by others ---
