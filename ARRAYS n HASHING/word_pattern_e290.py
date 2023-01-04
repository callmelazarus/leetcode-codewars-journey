"""
https://leetcode.com/problems/word-pattern/description/

1/2/2023

hashmaps
zip in for loop

--- PROMPT ---
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

--- LESSONS ---
- the data structure you setup matters (e290). pattern_letter: s_list_word is different the inverse
- using zip in your loop allows you to loop thru two iterables at the same time

--- QUESTIONS ---

--- PSEUDOCODE ---

        Needs to map in both direction

        Hashmap 

        Process:

        need to turn the s into a list of words - split

        build an association DS (hashmap)
            loop thru s and pattern
                build dictionary from s->apttern and vice versa
                Check to see if correlation exists between dict and iterand
                    return False if it doesn't
                return True otherwise


        time: O(n + m)
        space: O(n + m)



"""
# --- MY SOLUTION ---
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool

        """

        # convert the s string into a list of words, split at the ' '
        s_list = s.split(" ")

        # initalize two dictionaries to associate words and pattern character
        char_to_word = {}
        word_to_char = {}

        # check edge case where pattern length matches s list length
        if len(pattern) != len(s_list):
            return False

        # loop thru both patterns and s_list concurrently using zip fxn
        for char, word in zip(pattern, s_list):

            # build dictionaries if char or word doesn't exist
            if not char_to_word.get(char):
                char_to_word[char] = word
            if not word_to_char.get(word):
                word_to_char[word] = char

                # if there isn't a correlation between word and pattern
                # in either direction proves to be False, return False
            if char_to_word[char] != word or word_to_char[word] != char:
                return False
        return True

           


        # -- original solution - only checks one way --
        # loop thru the s_list
        # for i in range(len(s_list)):
        #     # if hash doesn't have s_list item -> add it
        #     if not hash.get(pattern[i]):
        #         # hash = {pattern_letter: s_list_word}
        #         hash[pattern[i]] = s_list[i]
        #     # if hash contains item, we need to check it
        #     else:
        #         # if we see that hash pattern doesn't match, return False
        #         if hash.get(pattern[i]) != s_list[i]:
        #             print('hi')
        #             return False
        # return True
                

# --- TEST ---


# --- ALT SOLN by others ---
