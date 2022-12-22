"""
https://leetcode.com/problems/validate-binary-search-tree/description/

12/21/2022
boundaries setup
recursion

--- PROMPT ---
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

        establishing if something is a valid binary tree:
        conditions:
        - left node is less than node's key
        - right node is larger than node's key
        - there is no more than two children node of a parent node
        
        consider a depth first search, ensuring that the left node is less than key's node
        the key here, is recognizing that the comparison boundaries are actually the parent node's value. Incorporating these boundaries requires a helper function with new arguments.
        return true / false

        time O(2n)


"""
# --- MY SOLUTION ---

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        """
        def helper(node, left_bound, right_bound):
            # when you hit the null condition
            if not node:
                return True
            
            # need to see if the values are within the boundaries
            if not (node.val < right_bound and node.val > left_bound):
                return False

            # recursive call - check left nodes
            # the right boundary, needs to be less than the parents val
            # if both return true, then return true, if one returns false, return false
            return helper(node.left, left_bound, node.val) and helper(node.right, node.val, right_bound)

        # return either true or false, which is the result of the helper function
        # arguments here are negative and postiive infinity
        return helper(root, float("-inf"), float("inf"))



# --- TEST ---


# --- ALT SOLN by others ---
