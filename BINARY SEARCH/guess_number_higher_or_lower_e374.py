"""
https://leetcode.com/problems/guess-number-higher-or-lower/

1/5/2022
binary search

--- PROMPT ---

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.


--- LESSONS ---
the left pointer should be mid + 1, and 
right pointer is just mid. This is because we ultimately don't 
want to include the midpoint, since midpoint is related to the 
solution condition.

--- QUESTIONS ---

--- PSEUDOCODE ---

        function will return:
        -1 -> num > pick (guess is higher)
        1 -> num < pick (guess is lower)
        0 -> num == pick

        n is the largest value possible...

        just need to set the mid condition (l + r) //2
        using the guess method to indicate if less, higher or there

        if less:
            update right to midpoint

        if higher:
            update left to midpoint

        repeat until guess returns 0

"""
# --- MY SOLUTION ---

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n

        while l <= r:
            
            mid = (l+r)//2

            res = guess(mid)

            # if guess is less, check the left side by updating r pointer
            if res == -1:
                r = mid 

            # if guess is greater, check the right side by updating l pointer
            elif res == 1:
                l = mid+1
            # last condition is if res == 0, which is a correct guess
            else:
                return mid
        




# --- TEST ---


# --- ALT SOLN by others ---
