"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

12/15/2022

breadth first search, queue FIFOb

--- PROMPT ---
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

--- LESSONS ---
breadth first search will use queues
you can initialize queues in python using collections.deque()
The largest possible/worst case level of a tree is n/2, where n is the # of nodes in a binary tree

--- QUESTIONS ---
I really don't think I could ever figure this out on my own...
it is hard to think about how to reach conditions where the 

--- PSEUDOCODE ---
personal attempt:
left to right, level by level
seems like a breadth first search

create solution list
append root

level solution fxn
create level_solution_list
if left exists, append left into level_solution_list
if right exists, append right into level_solution_list

check out left node
call level solution fxn

neetcode:
build a queue of children -> pop elements into sublist -> add childrens to queue

time: O(n)
mem: O(n) (queue could have up to n / 2 elements - max binary tree length is n/2)
"""


# --- MY SOLUTION ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        """
        # initialize results list
        res = []

        # initialie queue that will build the values
        queue = collections.deque()

        # add the root to the queue to start things off
        queue.append(root)

        # BFS algo
        # while queue is not empty (queue will contain each level's values)
        while queue:
            # get current size of queue, which we will then loop thru
            # this will allow us to iterate, just 1 level at a time 
            qLen = len(queue)

            # contains values for that level
            level = []

            # loops thru nodes in that level (popping)
            for i in range(qLen):
                # pop element from node (FIFO)
                node = queue.popleft() 
                    
                # need to add to levels list, and add any children (if node exists)
                if node:
                    # add the value of node to level list
                    level.append(node.val)
                    # add children of nodes to queue, if they exist
                    queue.append(node.left)
                    queue.append(node.right)

            # we then append the values at that level into res list (if level is non-empty)
            if level:
                res.append(level)

        return res


# --- TEST ---


# --- ALT SOLN by others ---
