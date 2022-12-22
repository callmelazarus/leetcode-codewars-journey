"""
https://leetcode.com/problems/combination-sum/description/

12/7/2022

depth first search, backtracking
recursion

--- PROMPT ---
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

--- LESSONS ---
Backtracking
Lessons:
https://www.youtube.com/watch?v=Zq4upTEaQyM

- choices - what is the core choice being made?
- constraints
- converge to goal

--- QUESTIONS ---

--- PSEUDOCODE ---
Consider your decision trees
1. one path considers using one value in the list
2. the other path does NOT use the value in the list (this will prevent duplicates)
"""


# --- MY SOLUTION ---
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        consider decision trees
        the challenge when thinking of brute force, there are cases of permutations of solutions, which is not desirabel [2, 2, 3] = [2, 3 ,2]


        Time compelxity = O(2^t) (two choices -> two) (height of tree = target size, t)
        """
        # global solution list
        soln = []

        # i: index that points to candidate (this will continue to iterate/loop thru the list of candidates in the dfs recursive)
        # curr: list of all current combinations, single [2, 2, 3]
        # total: what is the total sum of the current

        def dfs(i, cur, total): 

            # base case:
            # this is where we HAVE A SUCCESSFUL CANDIDATE
            # if the total matches the target (possible soln), append current to soln (using a copy)
            if total == target:
                # cur[:] creates a copy of a current, since we are going to keep using it for future combinations
                soln.append(cur[:])
                # break out
                return
            
            # if we can't choose another candidate (i is out of the bounds/index of the list of candidates)
            # or we overshoot target
            if i >= len(candidates) or total > target:
                return

            # add the candidates list to the cur combination list
            cur.append(candidates[i])

            # --1-- BRANCH ONE of decision tree
            # call recurrsive (where we include candidate (repeat sum of same #))
            dfs(i, cur, total + candidates[i])

            # consider other solution, where we aren't considering duplicate candidate
            # first then remove that by popping the most recent addition (cleanup)
            cur.pop()

            # --2-- BRANCH TWO of decision tree
            # call recursive (where we DONT include the candidate)
            dfs(i + 1, cur, total)

        # start with 0th index, an empty curr list, and a 0 total
        dfs(0, [], 0)
        return soln

# --- TEST ---


# --- ALT SOLN by others ---
