"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

12/20/2022
left, mid, right pointers
recursion
recognize that the array given is already sorted

--- PROMPT ---
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
Vocab:
height balanced binary search tree - is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

BST - left subtree is LESS than node. Right subtree is GREATER than node

Process
convert a LIST - convert it into a height balanced binary search tree
will need to loop thru the sorted array, and start to build the tree

using left, right, and mid pointers
        time: O(n)
        mem: O(log n) (log n is the height of this height balanced tree)


"""
# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode

"""
        # create helper function that recursively creates the nodes of the tree
        # pass in the pointers, left and right. It already has access to nums
        def helper(l,r):
            # base case
            # if my pointers are invalid (left > right...), return a None Node
            if l > r:
                return None

            # calculate the mid index pointer
            mid = (l + r) // 2 # calc mid

            # setup root of tree with the mid - initializing the root node
            # setup the root as the mid index
            root = TreeNode(nums[mid])

            # setup left node
            # the right pointer will be just 'left' of mid (mid -1)
            root.left = helper(l, mid-1)

            # setup right node
            root.right = helper(mid + 1, r)
            # return the root
            return root

        # call helper
        return helper(0, len(nums)-1)


# --- TEST ---


# --- ALT SOLN by others ---
