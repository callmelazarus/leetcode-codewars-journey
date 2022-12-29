"""
https://leetcode.com/problems/coin-change-ii/

12/29/2022

--- PROMPT ---
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

        output is the total number of combinations of coins to match the amount
        coins can be used multiple times each


        amt = 5
        coins
        1 2 5
        
        time: O(coins * amount)
        space: O(amount)



        # coins: [1, 2, 5]
        # amt: 5

        # ways you can reach an amount, as noted by its index
        # [1, 1, 2, 2, 3, 4]
        # corresponding amount, is the index
        # [0, 1, 2, 3, 4, 5]

        the way list is built:
           indexes indicate target amounts
           1  2  3  4  5  6
('way: ', [1, 1, 0, 0, 0, 0], 'coin: ', 1, 'i: ', 0, 'j:', 1)
('way: ', [1, 1, 1, 0, 0, 0], 'coin: ', 1, 'i: ', 0, 'j:', 2)
('way: ', [1, 1, 1, 1, 0, 0], 'coin: ', 1, 'i: ', 0, 'j:', 3)
('way: ', [1, 1, 1, 1, 1, 0], 'coin: ', 1, 'i: ', 0, 'j:', 4)
('way: ', [1, 1, 1, 1, 1, 1], 'coin: ', 1, 'i: ', 0, 'j:', 5)
('way: ', [1, 1, 2, 1, 1, 1], 'coin: ', 2, 'i: ', 1, 'j:', 2)
('way: ', [1, 1, 2, 2, 1, 1], 'coin: ', 2, 'i: ', 1, 'j:', 3)
('way: ', [1, 1, 2, 2, 3, 1], 'coin: ', 2, 'i: ', 1, 'j:', 4) ** <- DP 
('way: ', [1, 1, 2, 2, 3, 3], 'coin: ', 2, 'i: ', 1, 'j:', 5)
('way: ', [1, 1, 2, 2, 3, 4], 'coin: ', 5, 'i: ', 2, 'j:', 5)

        ** DP in action
        this is the 4th index, corresponding with the 4th amount.
        ways[j - coins[i]]
        ways[4 - 2] = ways[2]
    
        to get the answer to 4 target amount, we look to what it takes to 
        get to target-coin in question

"""
# --- MY SOLUTION ---

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int

        """


        # initialize the number of ways we can solve each amount
        ways = [0] * (amount+1)

        # 0th amount takes 1 way to sum to 0
        ways[0] = 1

        # loop thru each coin
        for i in range(len(coins)):
            # loop thru the specific elements in the ways array
            for j in range(len(ways)):
                # so long as the coin value, is less than the ways index/amount, update the amount.
                # in other words - if the coin can fit in the target amt
                if coins[i] <= j:
                    # replace the ways amount, with the ways
                    ways[j] += ways[j-coins[i]]
                    print('way: ', ways, 'coin: ', coins[i], 'i: ', i, 'j:', j)

        print(ways)
        return ways[amount]
# --- TEST ---


# --- ALT SOLN by others ---
