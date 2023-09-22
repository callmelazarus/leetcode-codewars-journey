"""
https://leetcode.com/problems/merge-sorted-array/description/

9/21/2023

--- PROMPT ---
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.




--- LESSONS ---
struggled really with following all the pointers thru each iteration

recognizing edge cases, WITHOUT a pre-built test

interestingly, when put into gpt, I get the same solution. What is shown below is Neetcode

--- QUESTIONS ---

--- PSEUDOCODE ---
           2 arrays - nums1 and nums2 - increasing order. m notes the number of elements in nums1. n notes number of elements in num2
    merge these two arrays into 1, which will be stored into nums1 (which has length m + n, where the first m elements are numbers, and the last n elements are 0)
        
        3 pointers
        - one locating the replaced pointer
        - one locating last val of nums2
        - one locating last val of nums1

        start pointer at the end of nums 1
        place the largest value in that point
            compare the last value in nums1, and last number in nums2. place the larger value into placement



"""
# --- MY SOLUTION ---
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # nums1 -> m
        # nums2 -> n

        end_of_nums1 = m + n - 1

        # merge in reverse order, replacing the values if
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[end_of_nums1] = nums1[m-1]
                m -=1
            else: 
                nums1[end_of_nums1] = nums2[n-1]
                n-=1
            # always decrement last pointer
            end_of_nums1-=1


        # edge case: when remainder of nums2 is smaller than nums1
        # I wouldn't have even recognized this edge case...
        # fill nums1 with leftover nums2 elements, only if there are leftover elements in n
        while n > 0:
            nums1[end_of_nums1] = nums2[n-1]
            n -=1
            end_of_nums1 -=1


# --- TEST ---


# --- ALT SOLN by others ---
