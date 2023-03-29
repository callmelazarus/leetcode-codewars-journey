"""
https://leetcode.com/problems/remove-element/description/

1/13/2022
arrays

--- PROMPT ---
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---


        going to iterate thru the list

        when the iterand matches the 'val'
        we need to update that element in the list to be something else
        we do that by considering hte counter, which increments at each loop, and matches the index we are on in the nums list

        reuturn int - the number of elements, unadjusted


time: O(nlogn) sort is used. A more efficient algo is below
space complexity: O(1). NO new memory shoudl be used
"""
# --- MY SOLUTION ---
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        n=len(nums)
        for i in nums:
            if i == val:
                nums[counter] = 0
                n -=1
            counter +=1
        nums.sort(reverse=True)
        return n

# --- TEST ---


# --- ALT SOLN by others ---

# NC solution
# using pointers

class Solution_NC:
    def removeElement(self, nums: List[int], val: int) -> int:
      # initialize pointer k
      k = 0

      for i in range(len(nums)):
        # if we see the val, we ignore it

        # if the don't see val, swap items (placing them in beginning of list)
        if nums[i] != val:
          # similar to partition sort
          nums[k] = nums[i]
          k += 1
      return k

