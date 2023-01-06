/*

https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/learn/lecture/11183952#questions/7860030

1/5/2022
sliding window


--- PROMPT ---
Find the largets sum of consecutive values

--- LESSONS ---


--- QUESTIONS ---


--- PSEUDOCODE ---
create the window
as you loop
subtract the first value, and add the last element


*/
// --- MY SOLUTION ---

// time: O(N)

function maxSubarraySum(arr, num){
  let maxSum = 0;
  let tempSum = 0;
  if (arr.length < num) return null;
  for (let i = 0; i < num; i++) {
    maxSum += arr[i];
  }
  tempSum = maxSum;
  for (let i = num; i < arr.length; i++) {
    tempSum = tempSum - arr[i - num] + arr[i];
    maxSum = Math.max(maxSum, tempSum);
  }
  return maxSum;
}

maxSubarraySum([2,6,9,2,1,8,5,6,3],3)

// --- TEST ---

// --- ALT SOLN by others ---
