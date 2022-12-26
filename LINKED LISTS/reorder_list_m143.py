"""
https://leetcode.com/problems/reorder-list/description/

12/26/2022

Linked list
2 pointers
using multiple loops (not nested)


--- PROMPT ---
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

        -----|*****
        1 2 3 4 5 6
        1 6 2 5 3 4
        -----|***
        1 2 3 4 5
        1 5 2 4 3

--- LESSONS ---
'break' list by setting node.next to None
getting the midpoint by using pointers
Versing nodes
Merging lists

--- QUESTIONS ---


--- PSEUDOCODE ---



"""
# --- MY SOLUTION ---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):

        # establish pointers for fast and slow
        # slow starts at beginnning, fast starts at next node
        slow, fast = head, head.next

        # find middle using a slow and fast pointer
        # slow.next will mark the beginning of the second half!!
        while fast and fast.next:
            # slow pointer advances one node at a time
            # fast pointer advances 2 nodes at a time
            slow = slow.next
            fast = fast.next.next

        # second marks the start of second half
        second = slow.next

        # now we split the LL into two, saying slow.next now points to None
        # prev also set to None
        prev = slow.next = None


        # reverse second portion of list...
        while second:

            temp = second.next
            second.next = prev # prev initially is None
            prev = second
            second = temp

        # start merge two halves
        # Prev is set to the last element we looked at in the last loop 
        second = prev

        # first half is easy, just starts at head
        first = head

        # merge the two lists now
        while second:
            temp1, temp2 = first.next, second.next
            # re-assign first.next to second
            first.next = second
            # re-assign second.next to temp1 now
            second.next = temp1
            first, second = temp1, temp2







# --- TEST ---


# --- ALT SOLN by others ---
