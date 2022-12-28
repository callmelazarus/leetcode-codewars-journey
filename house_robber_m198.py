"""
https://leetcode.com/problems/house-robber/description/

12/27/2022
Dynamic programming
looping

--- PROMPT ---


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        :type nums: List[int]
        :rtype: int

        return the max sum, where you cannot select adjacent values
                 
        Returning just the odd's and evens, and taking the max is one approach... but that will leave out cases like

        0 0 0 4 4 0 9 9 1 0 0 

        9 1 1 9 8

        consider the sub-problems, which is the remaining subarray after you skip 
        

        This is the recurrance relationship: 
        rob = max ( arr[0] + rob[2:n], rob[1:n])
        

        ----- EXAMPLE -----

        [1, 2, 3, 1]

        loop explanation:

        n = 1
        temp = max(1+0, 0) = 1
        rob1 = 0 (rob2)
        rob2 = 1 (temp)

        n = 2
        temp = max(2+0, 1) = 2
        rob1 = 1 (rob2)
        rob2 = 2 (temp)

        n = 3
        temp = max(3+1, 2) = 4
        rob1 = 2 (rob2)
        rob2 = 4 (temp)

        n = 1 (last value)
        temp = max(1+2, 4) = 4
        rob1 = 4 (rob2)
        rob2 = 4 (temp)

        notice how the n + rob1 creates the adjacent summation
        rob2 is just keeping track of the max (between the adjacent sums, and the previous rob2)
        

"""
# --- MY SOLUTION ---
class Solution(object):
    def rob(self, nums):

        # dynamic programming initializing
        rob1 = 0
        rob2 = 0

        # [rob1, rob2, n, n + 1, ...]

        for n in nums:
            # max you can rob up until the value 'n'
            # n + rob1 reflects the gap
            temp = max(n + rob1, rob2)

            # update rob1 and rob2 values as you progress thru nums list

            # update rob1 to rob2
            rob1 = rob2

            # update rob2 to the max(temp) that we just computed
            rob2 = temp

        # return rob2 (which will equal the last max value)
        return rob2

# --- TEST ---


# --- ALT SOLN by others ---
