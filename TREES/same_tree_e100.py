"""
https://leetcode.com/problems/same-tree/

11/30/2022

- BFS, recursion
- define your conditions as the base case

--- PROMPT ---
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

--- LESSONS ---

- the reqmt for recursion is starting to get easier to spot. Writing it seems to still start with the base case, and then moving forward.

- in an `if` conditional, nothing something as `if not value` is the way to test if a node is is None/empty. If it is empty, than that statement will return `True`

--- QUESTIONS ---

--- PSEUDOCODE ---
how would I compare and contrast two elements

if nodes match, continue the recursion

break out of the recursive loop - when matches aren't met

if we traverse the entirety of the trees, than we can return a True


"""


# --- MY SOLUTION ---

# Definition for a binary tree node.
# time complexity O(p + q) - linear

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # DFS recursive solution

        # base case - means to check if the nodes are the same

        # if both are null
        if not p and not q:
            return True
        
        # if only one node is null
        if not p or not q:
            return False

        # if the values of the nodes are not equal
        if p.val != q.val:
            return False
        
        # call fxn recursively. If BOTH of these functions return TRUE, then we will return a True. Otherwise, return False
        # if there EVER is a false in this statement, ultimately, we will return a False
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))



# --- TEST ---
c = TreeNode(val=3)
b = TreeNode(val=2)
a = TreeNode(val=1, left=b, right=c)

print('a', a)

soln = Solution()

print(soln.isSameTree(a,a))



# --- ALT SOLN by others ---
