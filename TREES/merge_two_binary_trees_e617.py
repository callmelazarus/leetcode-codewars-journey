"""
https://leetcode.com/problems/merge-two-binary-trees/description/

12/19/2022
recursion
stacks

--- PROMPT ---
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.



--- LESSONS ---
this is a great recursive problem


call stack - we'll see how long this short video stays uploaded (12/19/22)
https://recordit.co/HfELWKxefI

--- QUESTIONS ---

It was hard recognizing what needed to be returned in the recursive call

--- PSEUDOCODE ---

"""


# --- MY SOLUTION ---

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode

        recursion will be required
        what do we want our recursive call to return??? we are returning the nodes
        time: O(n) - we will traverse every node to sum them
        space: O(n) - we build the soln with the largest tree
        """

        # base case
        # we recognize the smallest problem is when we hit a case with a null node. If one node is empty, we will return the other node (non empty)
        if root1 == None:
            return root2
        if root2 == None:
            return root1

        # if both nodes are non empty
        # update the value with the sum of the values
        root1.val = root1.val + root2.val

        # call the function, returning the operation above (the sum of the two values)
        # depth first search, uses stack, which is applied in recursive operation
        root1.left = self.mergeTrees(root1.left, root2.left)

        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1






# --- TEST ---
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]


# root 1
a = TreeNode(val=5)
b = TreeNode(val=3, left=a)
c = TreeNode(val=2)
root1 = TreeNode(val=1, left=b, right=c)

# root 2
f = TreeNode(val=7)
g = TreeNode(val=4)
h = TreeNode(val=3, right=f)
i = TreeNode(val=1, right=g)
root2 = TreeNode(val=2, left=i, right=h)

soln = Solution().mergeTrees(root1,root2)



# --- ALT SOLN by others ---
