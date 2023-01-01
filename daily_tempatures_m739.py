"""
https://leetcode.com/problems/daily-temperatures/

12/31/2022
stack

--- PROMPT ---
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---


        monotonic decreasing stack problem (decreasing stack order)

        output is a list of int, with differences between larger values and the value at the index initially

        the position of the output matches the day's temperature
        that value is the difference between that day's index, and the future index of a higher value.
        
        if no value ahead of it is larger, the output array should not 0



"""
# --- MY SOLUTION ---
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]

        """
        output = [0] * len(temperatures)
        # create a stack (which is a pair of temp, and index) 
        # this stack will hold temp info
        stack = [] 
        # index and temperatures
        for i, t in enumerate(temperatures):
            # is our stack empty, and is the temp greater than the last item in stack (we care if the temperature has increased)
            while stack and t > stack[-1][0]:
                # we pop from the stack (both temp and index)
                # we don't use the popped temp
                stackT, stackInd = stack.pop()
                # in result, fill that index in the output, with the diff bewteen the stackInd and i
                output[stackInd] = (i - stackInd) # calc the num of days diff
            stack.append([t, i])
        return output
            

# --- TEST ---


# --- ALT SOLN by others ---

# brute force O(n^2) time solution
class Solution_slow(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        soln = []
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    soln.append(j-i)
                    break
                if temperatures[j] == temperatures[i]:
                    soln.append(0)
                    break
                if j == n-1:
                    if temperatures[j] < temperatures[i]:
                        soln.append(0)
                    else:
                        soln.append(j-i)
        soln.append(0)
        return soln
