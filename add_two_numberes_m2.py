"""
https://leetcode.com/problems/add-two-numbers/

1/19/2022
linked lists

--- PROMPT ---
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---




"""
# --- MY SOLUTION ---

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
        two integers are stored in LL form.
        Output is a LL that contains the sum of the integers...

        why o why would someone ever build a DS in this fashion for summing integers....

        prev node
        cur node

        need to check the lengths of the linked lists

        brute force solution: build integers with the LL

        sum the values

        build a LL with those values

        """
        
        list1 = []
        list2 = []
        while True:
            if l1 is not None:
                list1.append(l1.val)
                l1 = l1.next
            elif l2 is not None:
                list2.append(l2.val)
                l2 = l2.next
            else:
                break
        sl1 = [str(num) for num in list1]
        sl1.reverse()
        stringl1 = "".join(sl1)

        sl2 = [str(num) for num in list2]
        sl2.reverse()
        stringl2 = "".join(sl2)


        total = int(stringl1)+int(stringl2)

        res_list = [letter for letter in str(total)]
        res_list.reverse()
        n = len(res_list)
        cur = ListNode(res_list[0])
        soln = cur

        # loop thru the list, building a LL
        for i in range(n):
            # consider cases outside of the last element
            # 8 0 7
            # 0 1 2
            # 0 1
            if i < n-1:
                # initialize the new node, which will be next
                next = ListNode(res_list[i+1])
                cur.next = next
                # need to update current
                cur = next
            else:
                cur.next = None

        return soln

        

        

# --- TEST ---


# --- ALT SOLN by others ---
