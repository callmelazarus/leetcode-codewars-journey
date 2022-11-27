"""
https://leetcode.com/problems/linked-list-cycle/

11/26/2022

- two pointers
- think of 2 runners running on a track at different rates

--- PROMPT ---
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

--- LESSONS ---
is not vs !=
`==` is an equality check
`is` is a idendity check, to see if the objects are exactly the same. 
You would use the `is` check with `None`.

--- QUESTIONS ---
I don't think this would work if the linked list just had a looping portion to it



--- PSEUDOCODE ---
We want to see if there is a node that will point to an existing node

return TRUE if there is a cycle in the SLL. Otherwise, return False.

I remember that there are solutions where there are two pointers.

I want to say - if we get to the end of the list, if there is a node that points to NONE, than there is no cycle.

If the track is 100m long, your speed is 10m/s, your friend's speed is 5m/s. Then after 20s, you've run 200m, your friend has run 100m. But because the track is circular, so you will be at the same place with your friend since the difference between your distances is exactly 100m.

How about we change another track, change the speed of you and your friend? As long as your speeds are not the same, the faster person will always catch up with the slower person again.

"""


# --- MY SOLUTION ---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# the logic is, if one pointer is running faster than the other, 
# eventually, the faster pointer will reach the same 'value' as the 'slow' pointer
# if there is a loop

# think of a racetrack, and a faster running, eventually meeting the slower person
# in the same loop.

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # we create two pointers, a slow and fast.
        # initialize pointers, slow and fast pointer
        slow = head
        fast = head
        # while fast and fast.next are NOT NONE. Basically, if either are NONE -> return False immediately -> this linked list will end
        while fast is not None and fast.next is not None:
            # increment the slower pointer by one
            slow = slow.next
            # increment the faster pointer by 2
            fast = fast.next.next
            # if the fast == slow, then we know we are cycling, return T
            if fast == slow:
                return True
        # eventually, if we hit a none, then we will return F, it is a closed loop
        return False

# --- TEST ---


# --- ALT SOLN by others ---

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # we create two pointers, a slow and fast. 
        # imagine running a lap, at different paces
        try:
            slow = head
            fast = head.next

            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        # if error occurs, then
        except: 
            return False




# https://leetcode.com/problems/linked-list-cycle/solutions/1829489/c-easy-to-understand-2-pointer-fast-slow/