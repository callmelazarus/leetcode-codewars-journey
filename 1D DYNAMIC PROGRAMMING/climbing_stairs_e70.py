"""
https://leetcode.com/problems/climbing-stairs/description/

12/28/2022
dynamic programming

--- PROMPT ---


--- LESSONS ---
Place data structures that you will manipulate outside of any loops (or else you will reset
that data structure)

It helped to write out the various solutions to see patterns, as well as also typing out
what I anticipate the code to spit out.


--- QUESTIONS ---



--- PSEUDOCODE ---

        n = 1
        op = 1

        n = 2
        op = 2 = 1 + 1
        1 1
        2

        n = 3
        op = 3 = 2 + 1
        1 1 1
        1 2
        2 1

        n = 4
        op = 5 = 3 + 2
        1 1 1 1
        1 1 2
        1 2 1
        2 1 1
        2 2

        n = 5
        op = 8 = 5 + 3

        n = 6
        op = 13 = 8 + 5

        n = 7
        op = 21 = 13 + 8

        how does having the answer to the previous problem helpful?

        solution is the summation of the prev two answers!

        time: O(n)
        space: O(n)
"""
# --- MY SOLUTION ---
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        """

        # base conditions for n == 1 and n == 2
        if n == 1:
            return 1
                
        if n == 2:
            return 2

        # setup cache for conditions where n > 2
        cache = [1, 2]

        # setup loop that will add to cache, the running sum of previous values (only need to loop from 3 to n+1 (exclusive))
        for i in range(3,n+1):
            # add the last two elements of the cache to the cache
            running_sum = cache[-1]+cache[-2]
            cache.append(running_sum)

        # return the last item in the cache
        return cache[-1]


# --- TEST ---


# --- ALT SOLN by others ---
