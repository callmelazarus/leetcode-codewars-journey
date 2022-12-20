"""
https://leetcode.com/problems/diameter-of-binary-tree/
12/19/2022

dfs
work from bottom up
height of tree
max height = 1 + max(left, right)
diameter of tree = 2 + left + right
--- PROMPT ---
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

--- LESSONS ---
height of tree leaf is -1

--- QUESTIONS ---

--- PSEUDOCODE ---
Measuring the max depths from each side of a subtree.
DFS
brute force: find the diameter from every single node. O(N^2)... sheesh

Trick - start from the bottom

height of a leaf is 0
height of a null node is -1
height = 1 + max(left, right)
* +1 to account for the fact that a leaf is height of 1
* height is returned to higher subtrees
diameter = L_height + R_height + 2
* +2 to account for null nodes, which are -1 height (I think)


"""
# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int



        time: O(n) 
        """
        # global result value
        res = [0]

        # depth first search
        def dfs(root):
            # base case
            # if root is null, return height of null tree (-1)
            if not root:
                return -1
            
            # use recursion to repeatedly call the fxn to retrieve height (see return)
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            # calc the max dia (2 + L + R), and store it in result
            res[0] = max(res[0], 2 + left_height + right_height)

            # this recursive function ultimately returns the height of the tree
            # height is calculated with 1 + max(left_heights,right_heights)
            return 1 + max(left_height, right_height)

    # call function
        dfs(root)
    # return the max height
        return res[0]






# --- TEST ---


# --- ALT SOLN by others ---
