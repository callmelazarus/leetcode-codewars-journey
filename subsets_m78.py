"""
https://leetcode.com/problems/subsets/description/

1/30/2022
backtracking
recursion

--- PROMPT ---
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

--- LESSONS ---
.copy method creates a shallow copy. Without it in this solution, there is no appended values

--- QUESTIONS ---

--- PSEUDOCODE ---

        input - list of unique values (posiitve and negative)
        there is always at least one element in the list, up to 10


        if we do one loop, and then keep adding to the solution set, that would be exponential time O(N^N)...

        number of subsets -> 2 ^ n. Therefore max efficiency is O(n * 2^n)


        back tracking (brute force, but also most efficient)
        1. start by building a DECISION TREE
            You either add to the subset, or not add subset
            then from that point, we decide to add another value, or not
            You keep progressing in decision making


        Recursive call is required, where we are either adding or not adding elements
        output - list of lists, of unique combinations - no repeats. Order doesn't matter



"""
# --- MY SOLUTION ---

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        soln = []

        # use array for subsets
        subset = []

        # pass in the index that we are making decisions on
        def dfs(i):
            # setup break case, when index goes out of bound
            if i >= len(nums):
                # append the shallow copy of subset at base case
                soln.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            # increment the index
            dfs(i+1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return soln
# --- TEST ---


# --- ALT SOLN by others ---
