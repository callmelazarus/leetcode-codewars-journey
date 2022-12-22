"""
https://leetcode.com/problems/3sum/

12/2/2022

sort values (ensure that values are unique)
2 pointers

need to do a for loop to pass thru the loop, and then use the same logic of the 2 sum 2
to check the remaining values larger than the current number you are looping thru

--- PROMPT ---
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---

"""


# --- MY SOLUTION ---

# sorting is O(nlogn) + O(n^2) => O(n^2)
# space: O(1) or O(n) dependiung on library (On is python built in sort)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # output, unique set of 3 values in the list that sum to 0
        res = []

        # sort the array
        nums.sort()

        for i, a in enumerate(nums): # i is the index, a is the number
            # avoid using the same value twice
            if i > 0 and a == nums[i-1]:
                continue # pass on to the next element

            # set up the left and right pointers (see 2 sum 2 LC problem)
            l, r = i + 1, len(nums) - 1

            # for loop, very similar to 2 sum 2
            while l < r:
                # summation of the pointers
                threeSum = a + nums[l] + nums[r]

                # if the summation is greater than 0, reduce the right pointer (you've overshot the sum)
                if threeSum > 0:
                    r -= 1

                # if the summation is less than 0, shift left pointer to right
                elif threeSum < 0:
                    l += 1

                # if threesum == 0, add the solution to the res list!
                else:
                    # we found one solution!
                    res.append([a, nums[l], nums[r]])

                    # update our pointers, to consider unique values
                    # [-2, -2, 0, 0, 2, 2]
                    l += 1

                    # keep incrementing the l pointer, if l's value is the same as the previous l
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
                

# --- TEST ---


# --- ALT SOLN by others ---
