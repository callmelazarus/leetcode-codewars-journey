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

*** REQUIRES understanding of Linked lists

--- LESSONS ---
Recognize that there is a hint above concerning the singly linked list above.

"""


# --- MY SOLUTION ---

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
    def mergeTwoLists(list1, list2):
        # check if any of the lists are empty. if so, the other list would be the solution list
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        # ------- SECTION 1 ----------
        # start the new linked list, with the head that is smaller of the head of list1 or list2
        if list1.val < list2.val:
            # setup both a temp and the soln_head, the soln_head is actually the head we are returning. 
            # the 'temp' is the node that is going to be adjusted as we loop later on.
            temp = soln_head = ListNode(list1.val)
            # replace the head of list1 with the next node of list1 (since we are 'done' sorting that head)
            list1 = list1.next
        else:
            # if list2 is smaller
            temp = soln_head = ListNode(list2.val)
            # replace the head of list2 with the next node of list2 (since we are 'done' sorting that head)
            list2 = list2.next
        # ------- SECTION 2 ----------
        # meaty section of algo where we are looping thru the linked lists
        # loop thru the list until the list becomes empty
        while list1 is not None and list2 is not None:
            # checks to see which value is smaller
            if list1.val < list2.val:

    # setup the temp's next pointer to the value of the smallest linked list value
                temp.next = ListNode(list1.val)
                # 'advance' the current node to the the next node (thus removing the smallest number in list1)
                list1 = list1.next
            else:
                # same process, if list2's value is the smaller of the two
                temp.next = ListNode(list2.val)
                list2 = list2.next
            # we now 'advance' the temp's pointer, and keep 'while loopin' until the lists are empty
            # i dont' understand this ???????????????????
            temp = temp.next
        # ------- SECTION 3 ----------
        # clean up loops, by checking unsorted elements
        while list1 is not None:
            # point the next temp value to the value in list1
            temp.next = ListNode(list1.val)
            # advance the list1 node
            list1 = list1.next
            # advance the temp node
            temp = temp.next
        #same cleanup as while list1 a few lines above
        while list2 is not None:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next

        # return solution
        # why return solution head, versus temp ???????????????????
        return soln_head

# --- PSUEDOCODE ---
"""
On potential solution:
https://redquark.org/leetcode/0021-merge-two-sorted-lists/
Check if any of the lists is empty.
First we need to determine the head of the resultant list. This head will be smaller of the heads of the given lists.
Loop through each node of the lists until one of the lists get traversed completely.
While traversing the lists, identify smaller of the nodes of the lists and add it to the resultant list.
Once the loop is complete, there may be a case where a list has nodes remaining. We will add those remaining nodes to the resultant list.

This process will traverse list1 and list2 and reduce sorted values, as they are inserted into temp

3 main sections
1. setup the initial head of solution
2. create a loop with a (while loop) CONDITION - which will result in created the sorted solution list, but also reduce the length of list1 and list2
3. cleanup the remaining portions of list1 and list2, and fill the solution list with remainders


QUESTIONS's: Still unsure how the soln_head is generating a solution

"""
# --- TEST ---
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
# print('node2.val (should be 8): ', node4.val)


# --- ALT SOLN by others ---
