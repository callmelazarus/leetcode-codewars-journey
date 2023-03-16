"""
https://leetcode.com/problems/two-sum/

11/18/2022

- hash map / dictionary

--- PROMPT ---
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

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

        # time: O(n) 
        # mem: O(n) bc we might create a hash that is the entire size of the array, worst case

        prevDict = {} # value: index

        for i, element in enumerate(nums): # enumerate produces index, and element in tuple
            diff = target - element  # as you loop thru the list, the difference between target and element is the difference we need to find in the list
            if diff in prevDict: # if difference exists inside the dictionary
                return [prevDict[diff], i] # return that array
            
            # we add to the dictionary AFTER we do our conditional check. This ensures we use unique values
            prevDict[element] = i # otherwise, keep progressing thru list, building the dictionary


# --- PSUEDOCODE ---
"""
loop thru the list.
create a dictionary -> key: value is number: index

Check to see if difference between tareget and iterand exist inside the dictionary
if it exists, return the indexes

if not, keep building the dictionary.

Bc you are guarenteed an answer, looping thru the entire list, you will reach a solution

Time and space do have a inverse relationship many times.

"""
# --- TEST ---



# --- ALT SOLN by others ---
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # compiles values you've passed, with their index
        history = {}

        # loop thru the list of nums
        for i in range(len(nums)):
            
            # set the current nums value
            cur = nums[i]

            # recognize that the leftover value is the target minus current val
            leftover = target - cur

            # if leftover is in history!!! Return those indices
            if leftover in history:
                return [i, history[leftover]]
            # otherwise...
            # insert that number into your history (val:index pairs)
            history[nums[i]] = i




        # ideal Big O Complexity
        ## Time - O(N)
        ## Space - O(N)

            
