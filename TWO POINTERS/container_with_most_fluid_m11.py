"""
https://leetcode.com/problems/container-with-most-water/

12/3/2022

2 pointers
O(n) using while loop
O(n^2) for brute force

--- PROMPT ---
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints
 of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

--- LESSONS ---
think of conditionals that will determine WHEN you move the pointer

--- QUESTIONS ---

--- PSEUDOCODE ---
input is a list of heights

find two lines, that together form a container max(height x width) 
return int

can't slant container

soln that contains the max volume

iterate with 2 pointers at the outer edges, finding the smaller of the two values (dictates the height)
multiply height with the width, save to max

update max if larger max is found
"""


# --- MY SOLUTION ---
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        # initialize pointers
        l = 0
        r = n - 1

        # O(n) time solution

        soln = 0
        while l < r:
            width = r-l
            area = width*min(height[r],height[l])
            soln = max(soln, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1      
        return soln


        # works, but is too slow :(
        # time O(n^2)
        # soln = 0
        # for i in range(0, n):
        #     for j in range(i+1, n):
        #         width = j-i
        #         area = width*min(height[i], height[j])
        #         if soln < area:
        #             soln = area
        # return soln



        # first solution - passes inital test, but not all tests
        # my first pass was so close!
        # the key here, is to recognize the conditions when to increase l, and decrease r


        # loop thru the list
        
        # n = len(height)
        # # initialize pointers
        # l = 0
        # r = n - 1

        # while l <= r:
        #     width = r-l
        #     area = width*min(height[r],height[l])
        #     if soln < area:
        #         soln = area
        #     l += 1
        #     width = r-l
        #     area = width*min(height[r],height[l])
        #     if soln < area:
        #         soln = area
        #     r -= 1
        #     width = r-l
        #     area = width*min(height[r],height[l])
        #     if soln < area:
        #         soln = area           

        # return soln

# --- TEST ---


# --- ALT SOLN by others ---
