"""
https://leetcode.com/problems/binary-search/

11/5/2022

--- PROMPT ---
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


--- LESSONS ---


--- QUESTIONS ---
Trick is - how do I return the INDEX of the targeted number


"""


# --- MY SOLUTION ---






class Solution(object):

    # iterative solution
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # initialize 2 pointers
        left = 0
        right = len(nums) - 1

        # setup loop - left and right will be adjusted within the loop
        while left <= right:
            mid = (left + right) //2

            # eventually the target will match the nums[mid]. Return the index
            if nums[mid] == target:
                return mid
            
            # if target is on 'left side' -> adjust right to be just 'left of mid'
            elif target < nums[mid]:
                right = mid - 1

            # if target is on 'right side' -> adjust left to be 'right of mid'
            else:
                left = mid + 1
        
        # if target is not in the list -> return -1
        return -1


# solution with Kirk
    def search_kirk(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = len(nums)//2
        # edge case - when target not in nums
        if len(nums) == 1:
            if nums[mid] == target:
                return 0
            else:
                return -1
    
        if len(nums) == 0:
            return -1

        if target >= nums[mid]:
            blah = self.search_kirk(nums[mid:], target) 
            if blah == -1:
                return -1
            return mid + blah
            
        if target < nums[mid]:
            blee = self.search_kirk(nums[:mid], target)
            if blee == -1:
                return -1
            return blee 






    def search_recursion(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # this doesn't work....
        # initialize bounds
        left = 0
        right = len(nums) - 1

        if left > right:
            return -1
            
        mid_index = (left + right)//2

        if nums[mid_index] < target:
            return self.search_recursion(nums[mid_index+1:right], target) + mid_index
        elif nums[mid_index] > target:
            return self.search_recursion(nums[left:mid_index], target) 
        else:
            return mid_index


# --- PSUEDOCODE ---
"""
# taking in list, and a target value (int).
# return index of the value. 
# return -1 if the value is not in the list

quick check, if target not in list -> return -1

establish middle, and check if target is in right or left

if in right -> find another middle and check if target is in right or left

end of the line - if if you are left with 1 element. on left or right


:: video explanation without recursion ::
https://www.youtube.com/watch?v=6ysjqCUv3K4

:: CODE FROM LEARN ::
def binary_search(values, target, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(values) - 1

    # Base case: did not find item
    if left > right:
        return -1

    # Recursive case
    middle = (left + right) // 2
    if values[middle] < target:
        return binary_search(values, target, middle + 1, right)
    elif values[middle] > target:
        return binary_search(values, target, left, middle - 1)
    else:
      return middle

Resource:
https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

"""
# --- TEST ---

nums = [-1,0,3,5,9,12]
target = 837
# -1 -> 2
# 3 -> 0

# -1, 3 don't work

s = Solution()

print(s.search_recursion(nums, target))



# --- ALT SOLN by others ---
