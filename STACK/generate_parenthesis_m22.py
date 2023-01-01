"""
https://leetcode.com/problems/generate-parentheses/description/

12/31/2022
backtracking / recursion
stack
think about the conditions that make valid parenthesis true given a specific 'n' value

--- PROMPT ---
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

--- LESSONS ---
No need to pass in parameters in nested functions

--- QUESTIONS ---

--- PSEUDOCODE ---
        building variations of valid parenthesis, given a number

        setup decision tree

        only add open paren, if open < n
        only add close paren if # close < # open
        Stop once # open = # close = n

        (
       /  \
      (    )
      /\     \
     (  )     (
     /  /\    /\
    )  (  )  (  )
    /  \  \  \  \ 
    )   )  (  (  (
   /    \   \  \  \
   )     )   )  )  ) 

   PROCESS:
   Considering what makes up a valid solution, 
   recognize that you will be working with the number of open and closed paren
   These two arguments are going to be used as conditions for the recursion
   Build out the conditional statements of when you will add open or closed brackets
   call the backtracking function, incrementing the counter
   cleanup the function
  call the backtracking function

"""
# --- MY SOLUTION ---
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]


        """
        # stack will hold our solutions
        stack = []
        # res holds all variations
        res = []

        # paremeters are theh number of openN's and closedN's
        def backtrack(openN, closedN):
            # base case
            # recognize when you arrive at a solution
            # build your solution, based on what your stack looks like
            if openN == closedN == n:
                # form your string solution into the result
                res.append("".join(stack))
                # close out of the base case
                return

            # add open paren (based on if openN is less than n)
            if openN < n:
                # start to build your stack solution
                stack.append("(")
                # keep using backtrack (incrementing open count bc we add to open)
                backtrack(openN + 1, closedN)
                # cleanup, update our stack
                stack.pop()

            # add close paren (based on closed is less than open)
            if closedN < openN:

                stack.append(")")
                # call your backtracking
                backtrack(openN, closedN + 1)

                # cleanup, updating stack
                stack.pop()

        backtrack(0, 0)
        return res




# --- TEST ---


# --- ALT SOLN by others ---
