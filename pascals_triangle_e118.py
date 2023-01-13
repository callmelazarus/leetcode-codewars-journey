"""
https://leetcode.com/problems/pascals-triangle/

1/12/2022, 1/13/2022
arrays
loopin'

--- PROMPT ---
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
We will be looping 'numRows' times.
Build solutions for numRows = 1, and 2, and establish algorithm for cases greater than 2.

We utilize the last list in the results list to build the subsequent list (just like it is shown in the problem statement).

For the first and last elements of this list we are building, we will insert 1.
For cases inbetween, we utilize the add elements within the previous list (just as described in the problem statement)

Return the result list


"""
# --- MY SOLUTION ---
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = []

        # loop the number numRows times
        for iter in range(1, numRows+1):
            # construct cases for 1 and 2
            if iter == 1:
                res.append([1])
            elif iter == 2:
                res.append([1, 1])
            
            # construct cases for numRows >= 3
            else:
                # loop thru the previuos res list
                prev_list = res[-1]
                n = len(prev_list)
                # initialize new_list to hold the list we are building
                new_list = []
                for iter in range(0, n+1):

                    # add 1 to beginning of list
                    if iter == 0:
                        new_list.append(1)
                    
                    # if you are at the end of the list, append 1
                    elif iter == n:
                        new_list.append(1)

                    # otherwise - add the values of prev_list numbers
                    else:
                        sum = prev_list[iter]+prev_list[iter-1]
                        new_list.append(sum)

                # append to res, the new_list just created
                res.append(new_list)

        return res


# --- TEST ---


# --- ALT SOLN by others ---
