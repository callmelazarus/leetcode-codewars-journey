"""
https://leetcode.com/problems/baseball-game/description/

12/31/2022
stack

--- PROMPT ---
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

        Consider the various conditions that are presented, that will alter the stack

        initialize the stack

        loop thru the list, and evaluate what kind of str command to implement

        if int - append to stack

        if + - sum the last two scores in the stack

        if D - double the latest element

        if C - pop the last element from record

        return - sum of all elements

        time: O(n)
        space: O(n)

"""
# --- MY SOLUTION ---
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int

        """

        stack = []

        for operation in operations:
            if operation == "+":
                stack.append(stack[-1]+stack[-2])
            elif operation == "D":
                stack.append(stack[-1]*2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)

# --- TEST ---


# --- ALT SOLN by others ---
