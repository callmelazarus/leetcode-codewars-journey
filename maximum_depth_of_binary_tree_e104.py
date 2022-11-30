"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

11/29/2022

- recursion
- the +1 in the return statement is the way we count the levels of the tree

--- PROMPT ---
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

--- LESSONS ---
- if I'm doing the same thing over and over and over, immediately think of recursion
- the base case is always tricky, but so far, I'm typically seeing that I am returning 0
- would not have figured out

--- QUESTIONS ---

--- PSEUDOCODE ---

My attempt 
# input -> tree

# is this a depth first search?

# counter, that increments, everytime that you enter into a new node

# recursion is going to happen I believe, where you unwind the stack, adding to the number

    # output -> int, longest path from the root node down to farthest leaf node

"""


# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # test = root.left
        # print('root', root)
        # print('root.left',test)

        # base case:
        if not root:
            return 0

        # left side
        left_search = self.maxDepth(root.left)
        right_search = self.maxDepth(root.right)
        # the +1 at the end here is the way that we are able to appropriatly 'count'
        return max(left_search, right_search) + 1

            



# --- TEST ---


# --- ALT SOLN by others ---

# great explanation here:
# https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/359949/python-recursive-and-iterative-solution/?page=2

    #      10
    #    /    \
    #  5      19
    #        /
    #      17

# explanation of the recursion:

# self. maxDepth(None) = 0 by definition

# self. maxDepth(10)
# max(self. maxDepth(5), self. maxDepth(19)) + 1 # First recursive call from node 10
# max(max(self. maxDepth(None), self. maxDepth(None)) + 1, self. maxDepth(19)) + 1  # Recursive call on node 5 and its expansion
# max(1, self. maxDepth(19)) + 1 # Replacing for self. maxDepth(None) = 0 
# max(1, max(self. maxDepth(17), self. maxDepth(None)) + 1) + 1 # Recursive call from node 19
# max(1, max(self. maxDepth(17), 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0 
# max(1, max(max(self. maxDepth(None), self. maxDepth(None)) + 1, 0) + 1) + 1 # Recursive call from node 17
# max(1, max(max(0, 0) + 1, 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0
# max(1, max(0 + 1, 0) + 1) + 1 # Replacing the inner most max
# max(1, 1 + 1) + 1 # Replacing the inner most max
# max(1, 2) + 1
# 2 + 1 # Replacing the inner most max
# 3