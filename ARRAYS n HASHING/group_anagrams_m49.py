"""
https://leetcode.com/problems/group-anagrams/
11/18/2022

hashmap solution
defaultdict
ord() - count the characters that occur

--- PROMPT ---
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

--- LESSONS ---
defaultdictionaries do not return keyerrors
ord() function will return the unicode code of a specific char

--- QUESTIONS ---

# --- PSUEDOCODE ---
we want to be able to group strings that have the same 'count' of characters together, and return that list, grouped together

we do this by creating a solution dictionary that we will fill

Then we loop thru the various words in the string list

We initialize a counting list that will eventually be a key, in the solution dict. The values will be the anagrams

We build the counting list by looping thru each word
We then insert into the solution dictionary, the words that have that specific count.
The way we avoid the edge case error of the key not existing, is using a defaultdict (instead of a regular dictionary. defaultdicts don't raise keyerrors)

we then need to return the values of the solution dictionary (which contain the anagrams in lists)
        

        time: O(m * n * 26) 
        m : total number of input strings
        n : average length of a string
        26 : the size of the count array (from a - z)
        
"""


# --- MY SOLUTION ---
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        """
        # mapping charCount to a list of anagrams
        # default dict will cover the edge case if the count doesn't exist
        # defaultdict never raises a KeyError. It provides a default value for the key that does not exists
        soln = defaultdict(list)

        # loop thru each string

        for word in strs:
            # create count for all char in a - z
            count = [0] * 26

            # loop thru each char in string, to build a counter of each char
            for char in word:
                
                # create a counter for each character in the word

                # create a value associated with the char using ord()
                # ord takes a character, and returns unicode code for char
                # index is a char, value is the count/occurance
                count[ord(char)- ord("a")] += 1

            # add to dictionary, the word associated with the count list
            # group all similar annagrams together in the dict's values (list of strings)

            # tuples are non-mutable, and can uses as a key in a dictionary (lists can't)
            # placing a list as a key, will result in an 'unhashable type' error
            # this tupli'ing may not be required in all languages 
            soln[tuple(count)].append(word)

        print('count:',count)
        print('soln:', soln) # 
        
        # return just the values
        return soln.values()










# first attempt

        # need to identify what elements are anagrams, and then group them

        # output -> list of lists, of various anagrams

        # loop, creating a list of dictionaries with the corresponding the index.
        # recognizing the indexes -> loop thru to create another dictionry 
        # dictionary: key is the 

        # list_dict_words = []

        # for word in strs:
        #     word_dict = {}
        #     for letter in word:
        #         if letter in word_dict:
        #             word_dict[letter] += 1
        #         else:
        #             word_dict[letter] = 1
        #     list_dict_words.append(word_dict)
        # print('list of dictionaries:',list_dict_words)
        # soln = []
        # for i in range(len(list_dict_words)):
        #     single_ana = []
        #     for j in range(i+1, len(list_dict_words)):
        #         if list_dict_words[i] == list_dict_words[j]:
        #             single_ana.append(list_dict_words[j])
        # print('list_dict:', list_dict_words)
        # print soln




# --- TEST ---



# --- ALT SOLN by others ---
