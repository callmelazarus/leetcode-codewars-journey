"""
https://leetcode.com/problems/subtree-of-another-tree/

12/1/2022

helper function simlar to same_tree.
recursion

--- PROMPT ---
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists 
of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

--- LESSONS ---


--- QUESTIONS ---


--- PSEUDOCODE ---
traverse the root, to see if the node matches, the subroot's root
if a match occurs:
- traversing the tree

I would call a function to check to see if the subroot is the same as the subsequent nodes
in the root
- making the comparison

if no match occurs -> return true
"""


# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        # solution is O(root * subRoot) 

        # base case: 
        # if subRoot is empty, then return True
        if not subRoot:
            return True

        # if root is empty, return False:
        if not root:
            return False

        # if we find the same_tree, as we traverse the two trees
        if self.findmatch(root, subRoot):
            return True
        
        # if either the left OR right of the root matches with subroot,
        # return True. We don't need BOTH to return true, thus use 'or' operator
        
        # this recursive call will allow us to go deeper into the subtree's
        # depth first search?? or breadth first search?
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
        


    # this fxn is similar to LC same_tree problem
    def findmatch(self, root, subroot):
        
        # base case, if both trees are empty
        if not root and not subroot:
            return True

        # check both are non-empty AND the values are the same
        if root and subroot and root.val == subroot.val:
            # check if left/right subtrees are the same
            # if they BOTH return True, we will return TRUE
            return (
            self.findmatch(root.left, subroot.left) and 
            self.findmatch(root.right, subroot.right)
            )

        # if one tree is empty, and the other is non empty:
        return False



    # my first attempt
    # this was fun!

    #     # traverse to find matching roots
    #     self.findmatch(root, subRoot)

    #     # break case
    #     if (root and subRoot) == None:
    #         return True

    #     if root.left == subRoot.left:
    #         left = isSubtree(root.left, subRoot.left)
    #     elif root.right == subRoot.right:
    #         right = isSubtree(root.right, subRoot.right)


    # # traversing root to find match
    # def findmatch(self, root, subRoot):

    #     # base case:
    #     if root == None:
    #         return
        
    #     if root.val == subRoot.val:
    #         return root, subRoot

    #     elif root.val != subRoot.val:
    #         root = root.left
    #         self.findmatch(root, subRoot)
    #     elif root.val != subRoot.val:
    #         root = root.right
    #         self.findmatch(root.right, subRoot)

# --- TEST ---


# --- ALT SOLN by others ---
