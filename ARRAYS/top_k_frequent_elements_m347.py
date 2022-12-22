"""
https://leetcode.com/problems/top-k-frequent-elements/

12/9/2022
array problem, dictionary
unique list trick, where index is repeat count, and value is the numbers associated with repetition

--- PROMPT ---
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

k is a range from 1 to the number of unique elements in the list
It is guarenteed that the answer is unique

time O(n logn) at worst

--- LESSONS ---

--- QUESTIONS ---
is the array sorted?


--- PSEUDOCODE ---
        brute force:
        loop thru list, counting occurances
        return the top 'k' repeated values

        Bucket sort, where we create a list of length 'n'.
        The index represents the count, and the value itself is a list of lists, that note the numbers associated with a specific count
        - it is length 'n' at worst case because, there is a possibility that the list consists of all the same values. 
        eg. [1, 1, 1, 1] would have a count of 4, with a value 1.

        Then you you iterate thru the array O(n) to find the maximum k repeats



      # quick summary::::::
        # build a dict with counts of the various numbers
        # build a freq_list that contains sublists that associate the count, with the numbers of that count

        # loop thru freq_list, generating a solution list of the top k frequented elements

        Time - > O(n)
        Memory complexity is O(n)
"""


# --- MY SOLUTION ---
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        

        """

        # create a count dictionary
        count = {}

        # freq list - setup list where index = count ; value = num associated with count/index
        freq_list = [[] for i in range(len(nums)+1)]

        # build the counter dict
        for n in nums:
            # this is how we count how many times something occurs
            count[n] = 1 + count.get(n, 0)

        # loop thru the count dict! Building your frequency list, based on frequency and the value
        for n, c in count.items():
            freq_list[c].append(n)


        # now that you have your freq list - let's pop out the most freq. values
        soln = []

        # starting at the end, going backwards (last argument is -1)
        for i in range(len(freq_list)-1, 0, -1):
            # looping into the sublist of freq_list, and append to soln
            for n in freq_list[i]:
                soln.append(n)
                # once the length of the solution reaches k -> we will return the n
                if len(soln) == k:
                    return soln

# --- TEST ---


# --- ALT SOLN by others ---
