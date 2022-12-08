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


--- QUESTIONS ---

--- PSEUDOCODE ---

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

        res = []

        def dfs(i, cur, total): 
            # base case:
            # if the total matches the target, append current to results (using a copy)
            if total == target:
                # cur[:] creates a copy of a
                res.append(cur[:])
                # break out
                return
            
            # if we can't choose another candidate (i is beyond candidates)
            # or we overshoot target
            if i >= len(candidates) or total > target:
                return


            cur.append(candidates[i])

            # branch 1 of decision tree
            # call recurrsive (where we include candidate (repeat sum of same #))
            dfs(i, cur, total + candidates[i])
            # consider other solution, where we aren't considering duplicate candidate
            # first then remove that by popping the most recent addition
            cur.pop()

            # branch 2 of decision tree
            # call recursive (where we DONT include the candidate)
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res

# --- TEST ---


# --- ALT SOLN by others ---
