/*
udemy - colt steele class

1/5/2022
2 pointers

--- PROMPT ---
count how many unique values exist within a array

the values are ascending
--- LESSONS ---


--- QUESTIONS ---


--- PSEUDOCODE ---
time: O(N)


*/
// --- MY SOLUTION ---
function countUniqueValues(values){
  // add whatever parameters you deem necessary - good luck!
  
  if (values.length === 0){
      return 0
  }
  let i = 0
  let j = 1

let n = values.length 

/*
   i 
 1 2 1 2 3 4 4 5
         j     
         
          i
-2 -1  0  1 -1 -1  0  1 
                      j
If i and j are the same, increase j

I will result with the total number of unique values

if they are different:
Append the j's value ahead of i.
increase i by 1
increase j by 2
*/
while (j <= n){
    n = values.length
    if (values[j] === values[i]){
        j++
    }
    else{
        values.splice(i+1, 0,values[j])
        i++
        j+=2
        console.log('i, j: ', i, j)
    }
}
console.log(values)
return i+1
}


// --- TEST ---

// --- ALT SOLN by others ---

