"""
https://leetcode.com/problems/min-stack/description/

12/29/2022
stacks
maintaining two stacks  
everything done in O(1) time

--- PROMPT ---
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

--- LESSONS ---
Read the problem carefully - the pop method will 'remove' the last element (and return it)
But the top method is there to just retrieve the last element


--- QUESTIONS ---

--- PSEUDOCODE ---

Deque

first data type added to collections module in python 2.4. Introduced to increase efficiency for .append() and .pop() methods in python lists

"""
# --- MY SOLUTION ---


from collections import deque
class MinStack(object):
# initialize the stack object
    def __init__(self):
        # initialize two stacks for each instance of a MinStack
        # this can also be done with an array
        self.stack = deque()
        self.min_stack = deque()

        # push pushes the element val onto the stack.
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # add val to top of stack
        self.stack.append(val)

        # maintain minimum value at the top of the min_stack
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

        
# pop removes the element on the top of the stack.
 
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        
# top retrieves the top element of the stack. Use, bracket notation, not pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
# getMin - retrieves min value
    def getMin(self):
        """
        :rtype: int
        """
        # the min value would be at the top of the min_stack
        return self.min_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# --- TEST ---


# --- ALT SOLN by others ---
