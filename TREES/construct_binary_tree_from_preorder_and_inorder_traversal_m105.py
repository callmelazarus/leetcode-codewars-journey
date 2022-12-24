"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

12/23/2022
binary search tree
inorder and preorder list traversals have significant information that is conveyed to you 

--- PROMPT ---
Given two integer arrays preorder and inorder where preorder is the preorder 
traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

--- LESSONS ---
Traversing a binary Tre
Inorder => Left, Root, Right.
Preorder => Root, Left, Right.
Post order => Left, Right, Root.


--- QUESTIONS ---

--- PSEUDOCODE ---

First value of (preorder) will determine the root
This will help us distinguish what the left and right subtrees are (inorder)


Recognize the facts you get about the problem from preorder and inorder

You establish the root node with the 0th index of preorder
Denote the index within inorder array, to be used for future preorder/inorder arguments

Recursive solution, you continue to build 'root' nodes, until you have empty inorder/preorder lists.
Base case is empty pre/inorder lists, which you then return a 'null' node
You build the left and right subtrees, using the buildTree function, which will take variations of the pre/in-order lists that have been sliced, based on where the root is located within the arrays


"""
# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode

        """
        # base case - if either arrays are empty, then return the None node
        if not preorder or not inorder:
            return None

        # define root, which is always the first val of preorder
        root = TreeNode(val=preorder[0]) 
        # find the index for the root within inorder
        rootindex = inorder.index(preorder[0])

        # build left tree, think about how the preorder is being setup, and how the list is setup
        # the reason why the preorder starts at 1, is that 0 index is the root
        root.left = self.buildTree(preorder[1:rootindex+1],inorder[:rootindex])
        root.right = self.buildTree(preorder[rootindex+1:],inorder[rootindex+1:])
        return root


# --- TEST ---


# --- ALT SOLN by others ---
