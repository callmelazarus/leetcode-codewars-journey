"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/

1/23/2022
stack

--- PROMPT ---
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---


        starting from beginning.
        reading values, when you see operation, pop the last two items from stack and apply that operation
        the '-' and '/' operations are trickier, and require you to recognize that the second popped item is the 'leading' value that you do the operation with.

        Time: O(N)
        Space: O(N)



"""
# --- MY SOLUTION ---
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for c in tokens:
            if c == '+':
                sum = stack.pop() + stack.pop()
                stack.append(sum)
            elif c == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                diff = v2-v1
                stack.append(diff)
            elif c == '*':
                mult = stack.pop()*stack.pop()
                stack.append(mult)
            elif c == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                # round to zero using int
                diff = int(v2/v1)
                stack.append(diff)
                # if number, add to stack
            else:
                stack.append(int(c))
        # recognize that at the end, your soln should just be the singular element in the stack
        return stack[0]


# --- TEST ---


# --- ALT SOLN by others ---
