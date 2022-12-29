"""
https://leetcode.com/problems/coin-change/description/

12/28/2022
dynamic programming / cache
depth first search / bottom up

--- PROMPT ---
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


--- LESSONS ---
If decisions are being made, try to solve the problem using a decision tree. When you think of 'tree' - you can think of DFS, BFS.

--- QUESTIONS ---

--- PSEUDOCODE ---

        return an int, that describes the min amount of coins needed to reach amount
        if you can't find solution, return -1
        if amount = 0, return 0
        

        when you recognize that repeated subproblems occur, Dynamic programming can be used

        consider bottom up approach - consider solution for every amount value, starting from 0, all the way to the amount value given

        Create a solution array, where the index is related to the amount value, and the value is the actual min combination to get to that amount

        recognize the recurrence relationship, which is the meat of any DP solution:
        solution is the minimum of (amount + 1, or 1 + cache[a-c])




        Ex: [ 1, 3, 4, 5 ]

        DP[0] = 0
        DP[1] = 1 + DP[0]
        DP[2] = 1 + DP [1]
        DP[3] = 1
        ...


        time: O(amount * len(coins))
        space: O(amount)


"""
# --- MY SOLUTION ---
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # cache - ways to get to the amount
        # [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
        # index - reflect the goal amount
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        # we are going to build a list
        # index is related to amount value
        # value of list is min combinations to get to amount value
        cache = [amount + 1] * (amount + 1) # [[amount+1],[amount+1], ... amount+1]

        # if amt is 0, return 0
        cache[0] = 0
        print('init cahce', cache)
        # bottom up approach, from 1 to amount
        # build a solution for every possible amount, from 1, to the amount given
        for a in range(1, amount + 1):
            # iterate thru all coins
            for c in coins:
                # if the diff between the amount and coin is positive
                if a - c >= 0:
                    # recurrance relationship (meat of solution)
                    # cache[a-c] is the DP part of this problem
                    cache[a] = min(cache[a],1 + cache[a-c])



        # return the cache value associated with amount
        if cache[amount] != amount + 1:
            return cache[amount]
        
        # if the amount = amount + 1, then we are returning the default value, meaning we didn't have a soln, return -1
        else:
            return -1
                    # ex:
                    # coin = 4
                    # a = 7
                    # cache[7] = 1 + cache[7-4]





# --- TEST ---


# --- ALT SOLN by others ---

        """
        --- GREEDY SOLN --- doesn't always work
        GREEDY algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit


        max_v = max(coins)
        mult = amount // max_v
        remain = amount % max_v

        for n in coins:
            if remain == 0:
                return mult
            if remain == n:
                return mult + 1
            return -1
        
        return 0
        """