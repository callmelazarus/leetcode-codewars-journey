"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

12/6/2022

recursive solution, recognize that selections involve either adding or not adding the next character in the list
backtracking process

--- PROMPT ---
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



--- LESSONS ---
backtracking solution:
https://www.youtube.com/watch?v=d4SPuvkaeoo

Recursive soln:
https://www.youtube.com/watch?v=inrvpFusxf8

--- QUESTIONS ---

--- PSEUDOCODE ---


# return the length of the longest length of string concat
"""


# --- MY SOLUTION ---
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """

        # the use of self.ans is still perplexing to me

        n = len(arr)
        self.ans = 0

        def recurse(s, i):

            # base case 
            if i >= n:

                # check if duplicates exist
                if len(s) == len(set(s)):
                    self.ans = max(self.ans, len(s))
                return 

            # recurse, for the next element, with no change to string
            recurse(s, i+1)

            # product new string -> string, plus the current word
            new_string = s + arr[i]

            # check if duplicates exist, to optimize soln to reduce recursive steps
            if len(new_string) == len(set(new_string)):
                # call recurse with new string
                recurse(new_string, i+1)
        
        # call recursion with empty string
        recurse("", 0)
        return self.ans


## MY SOLUTION
def solution(A):

    # pseudocode:
    
    # let's prune the list, by removing any repeat letters in substrings.
    # let's create a helper function that helps find repeat characters
    # let's create all possible concatenations - this will be the  challenge

    # loop thru the list in a fashion that will build every possible combination
    # N, ranges from 1 to 8 
    # which means, at worst case, we are going to have a large number of possible combinations 

    # with that list of concatenated strings possibilities, I will run another loop, using the 'is_repeat_char' helper function, to count how many concatenated strings will return, which have no repeat characters.
    # return the length of largest concatenated strings with no repeat characters

    A_pruned = []

    # this may not be required
    for string in A:
        if is_repeat_char(string) == 1:
            A_pruned.append(string)

    # if repeats exist within substrings, easy -> return 0
    if len(A_pruned) == 0:
        return 0

    # need to build list of possible concatenated strings using helper function
    possible_soln = {}
    n = len(A_pruned)
    cum = ""
    # print(A_pruned)
    for i in range(0, n):
        cum = cum + A_pruned[i]
        if is_repeat_char(cum) == 1:
            possible_soln[cum] = len(cum)
    return max(possible_soln.values())




# helper function that finds repeats -> returns 1 if repeat doesn't exist. Returns 0 if repeat exists
def is_repeat_char(string):
    # build string with characters 
    list_char = [char for char in string]
    n_list = len(list_char)

    set_char = set(list_char)
    n_set = len(set_char)

    # if no repeats exist, return 1
    if n_list == n_set:
        return 1
    return 0
    

# notes after reading question:
# A is an array, made up of 'N' strings

# if no string exists, function returns 0

# unique criteria:
# S is the sum of SOME of the strings from A
# every LETTER is unique (no repeats)
# - if the string inside A has repeat words, then it can't be included in solution

# N -> [1, 8] 
# all letters are lowercase
# sum of the lenghts of string A < 100

# focus on correctness! less so on efficiency


# --- TEST ---


# --- ALT SOLN by others ---
