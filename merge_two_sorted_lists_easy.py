"""
https://leetcode.com/problems/merge-two-sorted-lists/

11/3/2022

--- PROMPT ---
You are given the heads of two sorted linked lists list1 and list2.

LINKED LIST!!!

Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the HEAD of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

--- LESSONS ---
Recognize that there is a hint above concerning the singly linked list above...

"""


# --- MY SOLUTION ---

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    pass


# --- PSUEDOCODE ---
    """
    https://redquark.org/leetcode/0021-merge-two-sorted-lists/
Check if any of the lists is empty.
First we need to determine the head of the resultant list. This head will be smaller of the heads of the given lists.
Loop through each node of the lists until one of the lists get traversed completely.
While traversing the lists, identify smaller of the nodes of the lists and add it to the resultant list.
Once the loop is complete, there may be a case where a list has nodes remaining. We will add those remaining nodes to the resultant list.



    """
# --- TEST ---
node1 = ListNode
node2 = ListNode
node3 = ListNode
node4 = ListNode

node1.val = 2
node1.next = node2

node2.val = 8 # undesirable response, where the value of all nodes are updated to the 'latest' value
node2.next = node3

node3.val = 16
node3.next = node4




print('node1.val (should be 2): ', node1.val)
print('node1.next: ', node1.next)
print('node2.val: ', node2.val)


# --- ALT SOLN by others ---
