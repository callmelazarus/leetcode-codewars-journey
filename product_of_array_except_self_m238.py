"""
https://leetcode.com/problems/product-of-array-except-self/

12/10/2022

prefix, and postfix list, the product of these elements will net your solution
video.assist

--- PROMPT ---
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

--- LESSONS ---

backwards for loop is interesting
for i in range(len(nums)-1, -1, -1)

--- QUESTIONS ---

--- PSEUDOCODE ---
Notes upon reading:
- len of answer = len of nums
- restriction here is the efficiency O(n)
  - brute force solution is simpler:
    - N^2, where you loop thru the list, and have a nested list that takes the product of all values in the list not including the initially looped value


# neetcode
Create prefix array with the products of all the prefixes
Create postfix array with the products of all the postfixes
multiply prefix and postifx to get the total product
* the indices will align.
"""


# --- MY SOLUTION ---
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

Create prefix array with the products of all the prefixes
Create postfix array with the products of all the postfixes
multiply prefix and postifx to get the total product
* the indices will align.

Two loops, one way to build prefix.
Other loop is going backwards, building the postfix, which will just multiply postfix and prefix

time: O(n)
mem: O(n)
            """

        # eg. [1, 2, 3, 4]
        # initializes an array of ones, matching the length of nums
        soln = [1]*(len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            # store prefixes in the result
            soln[i] = prefix
            # advance the prefix variable to be used in the future loop
            prefix *= nums[i]
        # eg. [1, 1, 2, 6] < - prefix list outcome

        postfix = 1
        # for loop from end, to beginning
        # 1st arg: last value in list
        # 2nd arg: one less than the index you want to stop at (stop at 0, put -1)
        # 3rd arg: increment
        for i in range(len(nums)-1, -1, -1):
            # similar to loop above, postfix will now be multiplied by the solution value. 
            # doing this directly manipulates the soln list.
            # the alt/slower way to do this, is to build another postfix list
            # and then take the product of the prefix products, and the postfix products.
            soln[i] *= postfix
            # advance the postfix variable to be used in future loops
            postfix *= nums[i]
        
        return soln




        # brute force approach below, solved in about 5 min. But O(n^2) is not efficient
        # soln = []
        # product = 1
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         if j == i:
        #             continue
        #         product = product*nums[j]
        #     soln.append(product)
        #     product = 1

        # return soln

# --- TEST ---
a = Solution()
lt = [1, 2, 3, 4, 5]
print(a.productExceptSelf(lt))

# --- ALT SOLN by others ---
