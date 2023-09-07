/*
https://leetcode.com/problems/move-zeroes/description/

12/21/2022
2 pointers
clever - think of another way to cleverly solve the problem. 
move all non-zeros to the beginning of list (same question, asked differently)


--- PROMPT ---
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        

        bubble up the zero by pushing non-zeros to left side, this will result in a list with zeros on the right end
        swap elements if non zero value is found (this pushes non-zero val to beginning of list)
        if zero is seen, don't swap it

        time: O(n)
        space: sorted list in place


        */
// --- MY SOLUTION ---
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    /*
     must do this operation in place, without making copy of array
     input: int array list
     output: int array list - with zero's moved to end of list

     need to iterate thru the int list
     
     Think I'm going to need to use pointers
     look for non-zero value, when you find it, flip with the next value in the list.

     create two pointers, the first pointer will increment one step for every iteration. the next pointer will seek a non-zero value.
     when a non-zero value is found, make a switch
*/

        let left = 0;
        let right = 0;
        let length = nums.length

    while (right < length) {

        // if the right element is non-zero
        if (nums[right] !== 0) {
            // Swap nums[left] and nums[right]
            let temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;

            // Move left to the next position
            left++;
        }
        // Always move right pointer forward
        // this is especially important when right is ZERO
        // when right is ZERO, the pointer will continue, until it hits a case where Right is Non-Zero
        right++;
    }
}


// --- TEST ---


// --- ALT SOLN by others ---
