"""
https://leetcode.com/problems/ransom-note/description/
11/19/2022

TYPE: Hashmap

--- PROMPT ---
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

--- LESSONS ---
Talking thru the problem and slowing down will help me when I am discouraged


--- QUESTIONS ---

"""


# --- MY SOLUTION ---
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = self.dictmaker(ransomNote)
        mag = self.dictmaker(magazine)
        print('note:', note, 'mag:', mag)

        for key, value in note.items():
            if mag.get(key) < value:
                return False
        return True
        # if ransome note can be constructed using letters from mag -> True
        # build dict with note and mag, with key:value -> char: # occurances
        # compare the dict -> if the value associated with the key in mag < value in ransomnote -> return False

    def dictmaker(self, s):
        soln_dict = {}
        for letter in s:
            if letter in soln_dict:
                soln_dict[letter] += 1
            else:
                soln_dict[letter] = 1
        return soln_dict

    


# --- PSUEDOCODE ---
"""




"""
# --- TEST ---



# --- ALT SOLN by others ---
