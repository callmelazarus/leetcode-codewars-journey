"""
https://leetcode.com/problems/arranging-coins/description/

1/10/2022

binary search 
math
not feasible to do without some assistance (addmittadly by neetcode)

--- PROMPT ---
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.



--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        output the number of complete full rows that can be established given an integer 'n'

        1 : 1
        2 : 1

        3 : 2
        5 : 2

        6 : 3
        9 : 3

        10 : 4
        11 : 4

brute force is O(n). let's solve it with that approach first

n = value. Subract 1, then 2, then 3, and then so on, until you reach 0, or a negative value.


n = 9
9 -1 = 8 -2 = 6 -3 = 3 -4 = -1
1        2       3     

n = 10
10 -1 = 9 - 2 = 7 - 3 = 4 - 4 = 0
    1       2       3       4

n = 11
11 - 1 = 10 - 2 = 8 - 3 = 5 - 4 = 1 - 5 = -4
    1         2       3       4             


Mathmatical solution:
R is complete rows
n = is target
R/2 * (R + 1) = n
R needs to round down...

Binary search solution:
still using
n/2 * (n + 1)

time: O(log n)



"""
# --- MY SOLUTION ---
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int


        """
        l, r = 1, n
        res = 0

        while l <= r:
            # mid is the row considered. How many coins needed to complete that row
            mid = (l +r )//2
            # coins we need to complete a certain row
            coins = (mid / 2) * (mid + 1)

            # if we need more coins than we have. Then, we shift right pointer down
            if coins > n:
                r = mid - 1

            # if we have enough coins (n) to build a row
            else:
                l = mid +1
                res = max(mid, res)
        return res



# --- TEST ---


# --- ALT SOLN by others ---

# O(1) time
class Solution_math:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)