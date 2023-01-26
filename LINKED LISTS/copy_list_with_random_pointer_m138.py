"""
https://leetcode.com/problems/copy-list-with-random-pointer/
assist.video
1/21/2022
linked list
hashmap

--- PROMPT ---
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

--- LESSONS ---
when you pop something in the stack, you return that value. 
this is perfect for being able to then use that value to run the operation that you come across when you iterate

--- QUESTIONS ---

--- PSEUDOCODE ---
        Create a deep copy with two passes
        first pass, is just the creation of the nodes, and hashmap from copy to original nodes
        second pass

        time: O(2*N)
        space: O(N)

"""
# --- MY SOLUTION ---
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # intialize hashmap that stores Node info
        # initialize None: None such that None nodes would point to None
        oldToCopy = {None: None}

        cur = head
        # first pass, copy the nodes
        while cur:
            copy = Node(cur.val)
            # establish the hapmap curNode: copy of Node
            oldToCopy[cur] = copy
            # advance cur
            cur = cur.next
        print(oldToCopy)

        cur = head
        # second pass, set the pointers
        while cur:
            # assign copy to the COPIED node
            copy = oldToCopy[cur]
            # assign the pointers
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            # advance the node
            cur = cur.next
        
        return oldToCopy[head]

# --- TEST ---


# --- ALT SOLN by others ---
