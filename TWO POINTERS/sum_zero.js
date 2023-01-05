/*
udemy - colt steele class

1/5/2022

--- PROMPT ---


--- LESSONS ---


--- QUESTIONS ---


--- PSEUDOCODE ---



*/
// --- MY SOLUTION ---

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
