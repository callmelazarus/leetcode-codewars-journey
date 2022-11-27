"""
https://leetcode.com/problems/two-sum/

11/18/2022

- hash map / dictionary

--- PROMPT ---
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



--- LESSONS ---
Hash map - creating one will cost space complexity of O(n)

--- QUESTIONS ---

"""


# --- MY SOLUTION ---
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: nums(list); target(int)

        # output -> list of indices, that note two unique numbers that add to target
        
        prevDict = {} # value: index

        for i, element in enumerate(nums): # enumerate produces index, and element in tuple
            diff = target - element  # as you loop thru the list, the difference between target and element is the difference we need to find in the list
            if diff in prevDict: # if difference already exists inside the dictionary
                return [prevDict[diff], i] # return that array
            prevDict[element] = i # otherwise, keep progressing thru list, building the dictionary


# --- PSUEDOCODE ---
"""
loop thru the list.
create a dictionary -> key: value is number: index

Check to see if difference between tareget and iterand exist inside the dictionary
if it exists, return the indexes

if not, keep building the dictionary.

Bc you are guarenteed an answer, looping thru the entire list, you will reach a solution


"""
# --- TEST ---



# --- ALT SOLN by others ---
