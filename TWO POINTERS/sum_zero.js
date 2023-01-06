/*
udemy - colt steele class

1/5/2022
2 pointers

--- PROMPT ---
return two values that sum to 0 in a list

--- LESSONS ---


--- QUESTIONS ---


--- PSEUDOCODE ---
time: O(N)
space: O(1)

set pointers to left and right


*/
// --- MY SOLUTION ---

function sumZero(arr){
  let left = 0
  let right = arr.length -1
  // cannot be left < = right. The = sign would result in the possiblity of summing 0's, which would work
  while(left < right){
    // intialize sum to be the sum of the left value and right value
    let sum = arr[left] + arr[right]
    // if sum - we found the sum
    if (sum === 0) {
      return [arr[left], arr[right]]
    }
    // if the sum is too big, the positive/right value is too large. we need to reduce the right
    else if(sum > 0){
      right--
    }
    // if the sum is too small, the neg/left value is too negative. we need to increase the negative val
    else {
      left++
    }
  }
}



// --- TEST ---

// --- ALT SOLN by others ---

// nested loop example
function sumZeroNaive(arr){
  for(let i = 0; i < arr.length; i++){
      for(let j = i+1; j < arr.length; j++){
          if(arr[i] + arr[j] === 0){
              return [arr[i], arr[j]];
          }
      }
  }
}


sumZero([-4,-3,-2,-1,0,1,2,5])
