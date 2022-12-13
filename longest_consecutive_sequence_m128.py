"""
https://leetcode.com/problems/longest-consecutive-sequence/

12/12/2022

- set, for and while loop
- think about what makes a consecutive list a consecutive list

--- PROMPT ---

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

"""


# --- MY SOLUTION ---
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n) (we are visiting each number at most, 2x)
        space: O(n)

input is an UNSORTED list

output is the LENGTH of longest consecutive elements

How do we determine a sequence:
- recognize the properties of a sequence
- no left neighbor for the start point

Converting a list to a set because searching a set is O(1) time.

psuedocode:
create a set of the list, this will help us search things QUICKLY
we loop thru the list, looking to see if the iterand is the starting point in list
if it is a starting point:
    increment a sequence counter (using a while loop) until we find the total length of that sequence
Update the solution length 
continue looping thru the list!

        """
        # make the nums into a set
        numSet = set(nums)

        #initialize counter variables
        longest_seq = 0
        seq_length = 0

        for n in nums:
            # check to see if value is a starting point in a sequence
            # if the iterand isn't the starting point of a sequence, move on in loop
            if n-1 not in numSet:

                # find all subsequent values by searching the set 
                while (n + seq_length) in numSet:
                    #increment length upon finding sequence's length
                    seq_length += 1

                # update longest sequence based on the largest of the two counters
                longest_seq = max(seq_length, longest_seq)
        return longest_seq
                

            

# --- TEST ---


# --- ALT SOLN by others ---
