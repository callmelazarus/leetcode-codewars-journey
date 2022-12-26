"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

12/26/2022
Linked List
(did this on my own!)
using pointers and maniuplated the SLL

--- PROMPT ---
Given the head of a linked list, remove the nth node from the end of the list and return its head.



--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

        Remove the node from the end of the list (1th index)

        change the pointer from the n+1 node to the n-1 node

        Need to be able to get from the end of the LL to that nth section

        # loop thru the list when you reach the n+1 node from back

        # identify that node
        # if links is 1th index, the node we need to alter is node index (length - n)

        # when you reach he node previous, change the pointer to the .next.next
        # for the .next node -> update the pointer from that node to None

        n = 2
        0 1 2 3 4

        1 2 3 4 5
        1 2 3   5

        length = 4
        aim = 2

        n = 2

        1 2

          2

        lenght = 1
        aim = -1


"""
# --- MY SOLUTION ---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # find the length of the LL
        length = 1
        pointer = head

        while pointer.next:
            pointer = pointer.next
            length += 1

        # edge case, if length is 1, then we know the answer is None
        if length == 1:
            return None

        # change n to be 0th index
        n = n-1

        # setup a special case bool
        special_case = False


        # if we recognize that the noe we are trying to remove is the 0th index, this is a special case (turn special_case to True, and set aim to 0th index)
        # otherwise: update the aim to the correct index, counting left to right
        if n+1 == length:
            aim = 0
            special_case = True
        else:
            aim = length - n -2

        # setup the counter and pointers to the new LL
        counter = 0
        soln = curr = head

        # while counter is less = aim
        while counter <= aim:
            # consider special condition, where n points to 0th index (just return the solution, pointing to next)
            if aim == 0 and special_case == True:
                soln = curr.next
                return soln
            # when counter == aim we have found the node that we want to update the pointers for
            if counter == aim:
                # assign the curr.next to the curr.next.next
                next_next = curr.next.next
                curr.next = next_next
            
            # if we don't have an aim == counter case - we just increment the curr node, and counter
            curr = curr.next
            counter += 1
        return soln

        


# --- TEST ---


# --- ALT SOLN by others ---
