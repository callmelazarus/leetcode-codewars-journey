"""
https://leetcode.com/problems/balanced-binary-tree/

12/16/2022

trees
recursive
dfs

--- PROMPT ---


--- LESSONS ---
balanced treee -> EVERY node differs in height by no more than 1 
the difference of the height of subtrees of a node should be <=1
--- QUESTIONS ---

--- PSEUDOCODE ---
go from bottom up

check the height of each subtree

"""


# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        my pseudocode:
        check if node has children left and right

        does child on left have children?
        if no -> check to see if right child has children
        if right child has children, check if they have children. If they do - return false

        """

# returns bool, and height of subtree
        def dfs( root):
            # base case - if root is null , return True (it is balanced,) and height 0
            if not root:
                return [True, 0]
            
            # run this dfs on left and right nodes
            left, right = dfs(root.left), dfs(root.right)

            # check if balance exists at root node
            # take abs difference between heights of subtrees
            # check to see if left and right subtrees are balanced (True)
            # tree and all subtrees will need to return True for balanced to return true (see all the ands here)
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)

            # return bool if balanced, and height of subtree
            return [balanced, 1 + max(left[1], right[1])]

        # return just the bool (0th index)
        return dfs(root)[0]


# --- TEST ---


# --- ALT SOLN by others ---
