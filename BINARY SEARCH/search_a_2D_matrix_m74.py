"""
https://leetcode.com/problems/search-a-2d-matrix/description/

1/11/2022
binary search x2

--- PROMPT ---
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



--- LESSONS ---
You can create pointers for a matrix, using the len of the matrix, and the len of a particular entry in that matrix

Interesting looping breaking scheme. We have else: break. To check if that did not fire, we do a conditional 
of the loop conditional using
' if not (top <= bot) ' -> which will be 'if not False' -> 'if True'
Because top <= bot is no longer true -> which is why we broke out of the while loop


        # if we never broke out of loop, and we have never been able to find the target value
        # if we didn't break out of loop in the else statment, then top <= bot if FALSE
        # therefore, note that for it to return true, you write
        # if not (top <= bot) -> which will return TRUE if we didn't 'break out' using else

        if not (top <= bot): -> this will be ' if not False'
            print(top <= bot)
            return False

--- QUESTIONS ---

--- PSEUDOCODE ---

        SLOW METHOD: O(m * n) -> if we just sort each sub array in the matrix

        Binary search to find the row. 
        Recognize that the target may not be in the rows, and write condition for that case
        Then binary search the row itself O(log m + log n)

        time: O(log m + log n)


"""
# --- MY SOLUTION ---
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # figure out num of rows and columns, this will setup the pointers for the rows
        rows, cols = len(matrix), len(matrix[0])

        # setup pointers for the 'top' and 'bottom' rows
        top, bot = 0, rows -1

        while top <= bot:
            mid_row = (top + bot) // 2

            # if target value is great than the last item in this row
            if target > matrix[mid_row][-1]:
                top = mid_row + 1

            # if target value is less than the first item in the row, 
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1

            # you've found the correct row with target val, let's break out of loop!
            else:
                break

        # if we never broke out of loop, and we have never been able to find the target value
        # if we didn't break out of loop in the else statment, then top <= bot if FALSE
        # therefore, note that for it to return true, you write
        # if not (top <= bot) -> which will return TRUE if we didn't 'break out' using else
        if not (top <= bot):
            print(top <= bot)
            return False

        # create list of just the correct row
        row = matrix[mid_row]
        print(row, matrix[mid_row])

        l = 0
        r = len(row)

        while l <= r:
            mid = (l + r) //2

            # if we found our target value
            if target == row[mid]:
                return True
            
            # if target is larger than mid, shift left pointer
            if target > row[mid]:
                l = mid + 1

            # if target is smaller than mid, shift right pointer
            if target < row[mid]:
                r = mid -1

        return False

        


# --- TEST ---


# --- ALT SOLN by others ---
