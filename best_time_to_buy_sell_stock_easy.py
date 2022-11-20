"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

11/4/2022
TIME: 

TYPE: Sliding window

--- PROMPT ---
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

--- LESSONS ---

"""


# --- MY SOLUTION ---
class Solution(object):
    def maxProfit(self, prices):
      """
      :type prices: List[int]
      :rtype: int
      """
      # solution with nested loops. Slow
      # max_diff = 0
      # n = len(prices)
      # for i in range(n):
      #     for j in range(i+1, n):
      #         diff = prices[j] - prices[i]
      #         if diff > max_diff:
      #             max_diff = diff
      # if max_diff == 0:
      #     return 0
      # return max_diff

# O(n) solution

      max_profit = 0
      # initialize min stock price with first price
      min_stock = prices[0]
      # loop thru the prices
      for p in prices:
        # ensure max profit (difference). Difference is 'p - min_stock'
          max_profit = max(max_profit, p - min_stock)
        # setup a minimum stock value, by setting min as, the min of prev min_stock, and the current price
          min_stock = min(min_stock, p)
      # check condition if values always decrease
      return max_profit

# --- PSUEDOCODE ---
"""
What is the core logic? - 
Find the largest increase between two numbers in the list, and return that difference.

If the list is only descending - return 0.

Not solutions:
finding smallest value, and largest value and taking the difference. Because! the largest value can preceed the smallest value

This could be a nested loop situation: think bubble sort.
set max_diff variable
outer loop - go thru entire list
inner loop - compare the value with the index of the outer loop
replace max_diff, if difference is larger

return max_diff
"""
# --- TEST ---



# --- ALT SOLN by others ---
