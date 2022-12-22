"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

12/21/2022
iterative with stack
or could be done recursively

https://www.youtube.com/watch?v=5LUXSvjmGCw&t=627s

--- PROMPT ---
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

in other words....
Given a BST, return the kth element of the BST if it was a 1-indexed value

--- LESSONS ---
need to use stack with iterative approach for DFS for tree problems, which means you will be appending and popping, 
and also likely using the fact that the stack is null or non-null as part of that while loop.

In this problem, the while condition is if the stack is non-null OR if the current node is non-null


--- QUESTIONS ---

--- PSEUDOCODE ---

        converting the tree into an ordered list, and take the ith element (treat array as 1-index)

        BST:
        - left nodes are all smaller than parent
        - right node value is larger than parent

        recursion or iterative 
        use stack if you use iteration
        stacks are 'built in' if recursive

        reach a value, add to stack
        when you hit null, pop out of stack (indiacates you visited element)
        after popping, check right side

"""
# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int


        """
        # define how many elements we visited. use this to match with k
        n = 0
        # initialize stack (bc iterative)
        stack = []
        # pointer to note where we are visiting
        cur = root

        # while current exists or stack exists
        while cur or stack:
            # traverse the left nodes
            while cur:
                # add current node to stack
                stack.append(cur)
                # traverse to left nodes until we hit a null curr
                cur = cur.left

            # when we hit a null curr, we remove items from stack
            # pop element out (meaning we visited node)
            cur = stack.pop()
            # increment n, indicating we visited a node
            n += 1

            # if we end up visiting the node that matches k, return the value
            if n == k:
                return cur.val

            # traverse right if we never reached n == k, and do the process again!
            cur = cur.right

# --- TEST ---


# --- ALT SOLN by others ---
