"""
https://leetcode.com/problems/add-two-numbers/

1/19/2022
linked lists
video.assist

--- PROMPT ---
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

        brute force solution: build integers with the LL

        sum the values

        build a LL with those values



"""
# --- MY SOLUTION ---

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # see alt solution below for NC solution
        
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_NC:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      """
    add the ones digit, and so on and so forth
    it is reversed, so it is already in the right order for you as you add things (you start at the ones place)


      """

      # establish dummy initial node
      dummy = ListNode()
      cur = dummy

      # initialize carry
      carry = 0

    # while l1 or l2 are not null - while they exist
      while l1 or l2 or carry:
        # set the values if they exist, otherwise, set to 0
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # create the sum
        val = v1 + v2 + carry

        # get the carry value
        carry = val // 10

        # get the ones place of val (remainder)
        val = val % 10 

        # establish the next node to be
        cur.next= ListNode(val)

        # update pointer of current, to be the next element (the new node you just created)
        cur = cur.next

        # advance the node being 'inspected'
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return cur.next