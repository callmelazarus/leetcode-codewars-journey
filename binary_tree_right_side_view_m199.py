"""
- https://leetcode.com/problems/binary-tree-right-side-view/description/

1/25/2022
Binary Tree
BFS - Queues

NOT straightforward at all...
--- PROMPT ---
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



--- LESSONS ---
this solution is out of the box thinking with a BFS, instead of DFS

--- QUESTIONS ---

--- PSEUDOCODE ---

        DFS is possible, but NT does BFS
        keep entering into the right side of the BT, and append to list
        Return the list

        BFS - level order traversal
        Looking at the just the right side of each level

        Build a QUEUE
        Result array

        Add levels to queue (left and then right)
        Take the right most value, and add to result.
        Pop the left value, and add its children to the queue

"""
# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            # rightSide will hold the right sided values we want to keep
            rightSide = None

            # qLen holds the length fo the queue which we are going to iterate thru until it is empty
            qLen = len(q)

            # iterate thru just the elements in that level
            for i in range(qLen):
                # pop elements from left (add to the right)
                node = q.popleft()
                if node:
                    # update right side with node (last node in cur level of queue)
                    rightSide = node
                    # add nodes to the right
                    q.append(node.left)
                    q.append(node.right)
            # if rightSide holds values, append value to results list
            if rightSide:
                res.append(rightSide.val)
        return res






# --- TEST ---


# --- ALT SOLN by others ---
