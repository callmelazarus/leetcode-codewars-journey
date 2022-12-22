"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

12/22/2022
cur node / pointer
while loop

--- PROMPT ---
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
understanding the problem
        Every value is unique
        if one node is to the left of root, and the other node is to the right of root
        if one of the nodes is a parent, than the soln is parent
        if one of the nodes is root, return root


        process:
        think thru how characteristics of solutions for this problem.
        This will give you the conditional statements for a solution.

        psueudocode:
        continue to progress down the tree, recognizing if p or q are both on the right or left side of the BST.
        If it is on one side, keep updating the current node to the new child node
        Once you recognize that p and q are on either side of the current node - the current node, must be the lowest common ancestor. Therefore return the cur value.


        time: O(log n) - we aren't visiting every node, we are 'splitting' the solution set in half everytime
        space: O(1) - no new memory needed


"""
# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode


        """
        # set the current node, as the root. This will update as you search thru the BST.
        # recognize that we will likely be returning this cur node, as that will hold the solution.
        cur = root

        # run until we find result
        while cur:
            # both p and q are greater than root
            if p.val > cur.val and q.val > cur.val:
                # update the current node to the right child 
                cur = cur.right

            # if both p and q are less than root
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # return the cur value (if we find that the nodes p > cur and q < cur or vice versa)
            # this covers the edge case as well, if p or q is the cur node (notice previous statements aren't >= or <=, just > or <)
            else:
                return cur

# --- TEST ---


# --- ALT SOLN by others ---
