/*
https://leetcode.com/problems/binary-search/description/
12/9/2022
while loop, pointers

--- PROMPT ---


--- LESSONS ---


--- QUESTIONS ---


--- PSEUDOCODE ---


*/

// --- MY SOLUTION ---
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}

 return index of where target exists, otherwise return -1

 pointers that will adjust, based on where target may be in a sorted nums lis
 */

var search = function (nums, target) {
  let l = 0;
  let r = nums.length;

  while (l < r) {
    let mid = Math.floor((l + r) / 2);

    // base case:
    if (nums[mid] === target) {
      return mid;
    } else if (target > nums[mid]) {
      // shift left pointer, inspect right side
      l = mid + 1;
    } else if (target < nums[mid]) {
      // shift right pointer, inspect left side
      r = mid;
    }
  }
  return -1;
};
// --- TEST ---

// --- ALT SOLN by others ---
