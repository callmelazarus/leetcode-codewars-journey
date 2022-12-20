"""
https://leetcode.com/problems/path-sum/description/

https://www.youtube.com/watch?v=LSKQyOz_P8I

12/19/2022

in order depth first search - recursion

--- PROMPT ---
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

--- LESSONS ---

True or False returns True

--- QUESTIONS ---


--- PSEUDOCODE ---
You accumulate the path sum as you traverse from root to node (DFS), checking to see if the current sum matches target sum
if they match, return a T. Otherwise, when you reach a Leaf, return a False


"""

# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool

        root to leaf path, to match sum value
        go from bottom up (from leaf) to root. If the sum = target, return True
        recursion
        what am I returning -> the running sum 

        time: O(n)
        mem: O(n) worst case - height of tree
        """



        def dfs(node, curSum):
            # base case:
            # if empty tree
            if not node:
                return False
            
            # if not null:
            # start keeping track of summation
            curSum += node.val
            
            # if node has no kids
            if not node.left and not node.right:
                # return T/F if curSum == targetSum
                return curSum == targetSum
            
            # if not leaf node, lets run dfs recursively
            # we just need to return either true or false 
            # if there happens to be one True, this line will return T (T or F -> T. F or F -> F)
            return dfs(node.left, curSum) or dfs(node.right, curSum)

        return dfs(root,0)

# --- TEST ---


# --- ALT SOLN by others ---
