"""
https://leetcode.com/problems/unique-number-of-occurrences/

3/28/2023
arrays

adobe / amazon / google

--- PROMPT ---
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---


"""
# --- MY SOLUTION ---
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = {}
        for num in arr:
            if num in c:
                c[num] += 1
            else:
                c[num] = 1
        counts = {}
        for key, value in c.items():
            print(value, counts)
            if value not in counts:
                counts[value] = 1
            else:
                return False
        return True
            



# --- TEST ---


# --- ALT SOLN by others ---
