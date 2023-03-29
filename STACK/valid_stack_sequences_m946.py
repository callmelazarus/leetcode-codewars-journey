"""
https://leetcode.com/problems/validate-stack-sequences/

2/6/2022
stacks

--- PROMPT ---
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.



--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---




"""
# --- MY SOLUTION ---
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Actually using a stack to solve this problem
        pointer on push

        while pu and po pointers are both not equal to the lenght of list
        if pop doesn't equal push, push to stack, and advance pointer

        if pop equals last value in stack, pop from stack, and advance pointer


Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
                   ^                   ^
stack = [1

push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

when pointer reaches the end of the push and pop or the stack is empty, return true
else return false

        """
        n = len(pushed)
        pu = 1
        po = 0
        stack = []
        stack.append(pushed[0])
        while pu +1 <= n or po+1 <= n:
            # push to stack
            if stack[-1] == popped[po]:
                stack.pop()
                po += 1
                print('pu: ', pu)
                print('po: ', po)
                print('stack: ', stack)
                if pu == n and po == n and stack == []:
                    return True
            else:
                stack.append(pushed[pu])
                pu += 1
                if pu == n and po == n and stack == []:
                    return True
        return False

# --- TEST ---


# --- ALT SOLN by others ---
