"""
https://leetcode.com/problems/reverse-linked-list/

11/23/2022

- three pointers
- think of ways to reverse how the .next will point based on pointers

--- PROMPT ---
Given the head of a singly linked list, reverse the list, and return the reversed list.


--- LESSONS ---
multiple pointers are necessary


--- QUESTIONS ---
how does the while curr_node work?

"""


# --- MY SOLUTION ---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # print(head)
        # print('head.val:',head.val)

        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # 5 -> 4 -> 3 -> 2 -> 1 -> None

        # three pointers used here
        # time complexity -> O(n)
        # space -> O(1) - just pointers

        prev_node = None # initialize prev to None
        curr_node = next_node = head 


        # while curr_node is NOT NULL
        while curr_node:
            # next is used to advance the current node.
            # first two lines: swaps the pointers from next to previous
            
            next_node = curr_node.next

            # previous node, is set as the next node!!
            # what used to be the next node, is now the previous node
            curr_node.next = prev_node

            # current node, is set as previous node
            # update the previous node to be the current node
            prev_node = curr_node

            # next node, is set as current node
            # update the current node to be the next node
            curr_node = next_node

        # prev is the new head of the reversed list
        return prev_node

        # alt way to write this
        # while curr:
        #     next, curr.next = curr.next, prev
        #     prev, curr = curr, next
        # return prev





# --- PSUEDOCODE ---
"""
input
traverse the linked list until you get to the end, building a list with the values of the linked list

build another linked list, starting at the head, with the values from the created list I have



"""
# --- TEST ---



# --- ALT SOLN by others ---

node4 = ListNode(8)
node3 = ListNode(6, node4)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)

print('node1: ', node1)
print('node2: ', node2)
print('node3: ', node3)
print('node4: ', node4)

print('node1.val (should be 2): ', node1.val)
print('node2.val (should be 4): ', node2.val)
print('node2.val (should be 6): ', node3.val)
print('node2.val (should be 8): ', node4.val)

print('node1.next (should be 0x102643df0): ', node1.next)
print('node2.next (should be 0x102643e50): ', node2.next)
print('node2.next (should be 0x102643f70): ', node3.next)