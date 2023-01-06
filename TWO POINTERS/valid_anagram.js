/*
https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/learn/quiz/4410604#questions/7860030

1/5/2022
hashmap
frequency counter

--- PROMPT ---
write a function that will return if the two words are anagrams of eachother

--- LESSONS ---


--- QUESTIONS ---


--- PSEUDOCODE ---
build counter dictionaries that count how many times a letter occurs within a word

loop thru one word
see if the counters match as you loop the the word

*/
// --- MY SOLUTION ---
function validAnagram(word1, word2){
  // add whatever parameters you deem necessary - good luck!
  let counter1 = {}
  let counter2 = {}
    for (let letter of word1){
        if (letter in counter1){
            counter1[letter]++
        }
        else {
            counter1[letter] = 1
        }
    }
        for (let letter of word2){
        if (letter in counter2){
            counter2[letter]++
        }
        else {
            counter2[letter] = 1
        }
    }
    for (let letter of word1){
    if (counter1[letter] != counter2[letter]){
        return false
    }        
    }
    return true
}

// --- TEST ---

// --- ALT SOLN by others ---
