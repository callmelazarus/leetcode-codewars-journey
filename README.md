# Problems to work thru

https://www.techinterviewhandbook.org/grind75?hours=12&weeks=8

Needcode - blind 75
https://neetcode.io/practice

# Goal:

MIN: 1 a day // results in roughly 39 total by Jan 1, 2023
Goal: 3 a day // results in roughly 117 total by Jan 1, 2023

Off on Sundays

# Why:

Be ready when my name is called in an interview.
Grow as a developer.
Have fun solving problems.

---

## Dec 1

**Today I worked on:**
**Reflection:**
**Lesson:**

---

## Dec 12, 2022 - Mon

**Today I worked on:**
1. Product of array except self


**Reflection:**
**Lesson:**



## Dec 10, 2022 - Sat

**Today I worked on:**
1. Top K frequent elements

**Reflection:**
Started using Akideck to build out flashcards that may present useful information that I learn.

**Lesson:**
Super cool way of counting elements:
```
    count = {}
    # build the counter dict
    for n in nums:
        # this is how we count how many times something occurs
        count[n] = 1 + count.get(n, 0)
```

## Dec 9, 2022 - Fri

**Today I worked on:**
1. binary search - JS
2. search a 2d matrix


**Reflection:**
Don't forget about while loops!

**Lesson:**


## Dec 8, 2022 - Thur

**Today I worked on:**
1. combination sum - cont.
2. Max length of a concat string with unique characters! Solved without help!!!

Tried to restore gitlab remote connection

**Reflection:**
Continuing to grok combination sum
It seems like I am able to push to both gitLab and github now. I will just add/commit a message. And do a `git push`. and then a `git push gitlab main` to push to both repo's.

**Lesson:**
I can figure these things out, but some of these things take time... and also noticing the little 'trick' that will get me there


## Dec 7, 2022 - Wed

**Today I worked on:**
1. combination sum

**Reflection:**
DFS, backtracking, recursive problems still hard...
didnt have the gusto in me today to do 2 problems...

**Lesson:**


## Dec 6, 2022 - Tues

**Today I worked on:**

- 3 LC style problems for Telsa codility challenge
- Maximum Length of a Concatenated String with Unique Characters

**Reflection:**

- for tech questions, just need to take your time as you go thru the problem

**Lesson:**
Code challenges

1. write notes as you read thru question
2. write on a piece of paper if needed
3. Challenge assumptions with reviewer
4. write pseudocode
5. start writing code
6. test code regularly

## Dec 5, 2022 - Mon

**Today I worked on:**

- longest substring without repeating character
- running sum of 1d array
- find pivot index

**Reflection:**

- sliding windows problems are just 2 pointers, but considering a subarray of a problem

**Lesson:**

- sum fxn in python is O(n) time

## Dec 3, 2022 - Sat

**Today I worked on:**

- 4Sum / array quadruplet
- conatiner with most water
- pramp technical interview -> contains duplicates

**Reflection:**

- 4Sum is no joke... don't know how I would solve this on my own....
- reviewing it with kyle was fun
- solving my problem - contains duplicates was fun as well.

**Lesson:**

- constant space complexity is when you have a condition where you have a set size that you are saving something
- take your time to think thru things, you will be nervous as you think thru problems
- think of conditionals that will determine WHEN you move the pointer

## Dec 2, 2022 - Fri

**Today I worked on:**

- REVISIT: 2 sum
- 2 Sum 2
- 3 sum

**Reflection:**

- these little tricks to these problems that I doubt I would figure out on the spot in an interview... 2 sum 2 and 3 sum are no joke....

**Lesson:**

- using 2 pointers for these problems is helpful
- sort method in python is O(nlogn) time complexity
- sort() mutates the list, and is implemented as list.sort()

## DEC 1, 2022 - Thur

**Today I worked on:**

1. Subtree of another Tree (extension to same_tree)
2. invert binary tree (another time from memory!!)
3. backspace string compare (easy - first one in a while I solved on my own, in less than 10 min!)

**Reflection:**

- this was the first LC problem that was actually enjoyable, even tho I didn't quite get the solution. I think the general logic was in my head, but writing the code out, especially the recursive nature of the code is uncertain to me
- I was on the right path in thinking about using a helper function
- the recursion is still challenging to me
- got practice with list comprehension, try/except, and helper functions today

**Lesson:**

- recursion solutions - simply define your edge cases/ return statements as the base case
- you likely will be returning something in the recursive call

## Nov 30, 2022 - Wednesday

**Today I worked on:**
transfer repo from gitlab to github.

1. same tree e100
2. invert binary tree in JS

**Reflection:**

- the reqmt for recursion is starting to get easier to spot. Writing it seems to still start with the base case, and then moving forward.

**Lesson:**

- in an `if` conditional, nothing something as `if not value` is the way to test if a node is is None/empty. If it is empty, than that statement will return `True`
- setting a new remote - github. use command `git remote add origin REPO_URL`. I think that is the process
- Trying to figure out my process here. May need to do this again with another repo that I am trying to trasnfer to GH. History:
  1. commit - 'transfer to github'
  2. git remote add origin
  3. commit 'test push to github'
  4. git remote set-rul 'url'
  5. commit - 'test push to github'
  6. git push --set-upstream origin main
  7. commit - 'fixed filename for invert binary tree JS'

## Nov 29, 2022 - Tuesday

**Today I worked on:**

1. Maximum Depth of Binary Tree

**Reflection:**

- Would not have figured out on my own, the need to keep track of the counter of the depth of the tree using the +1

**Lesson:**

## Nov 28, 2022 - Monday

**Today I worked on:**

1. merge two sorted list in JS

**Reflection:**

- I was focusing on doing work that makes and impact. Even if I'm going slowly, I am doing better than my old self. For this reason, I am happy with the 1.5 hours I spent on merge two sorted list. It did help though, that I had seen this problem before... but even still, I consider this a win.

**Lesson:**

- dummy nodes are typically created in SLL in order to allow you to keep track of the head of your solution SLL

## Nov 26, 2022 - Saturday

**Today I worked on:**
linked list cycle

**Reflection:**

- This was actually a bit more fun. Did this at the end of the day.
  To solve this problem, we used 2 pointers again, that advance at different rates. Genius.
- It isn't the amount of time I spend, it is the impact I make in the time I have

**Lesson:**
is not vs !=
`==` is an equality check
`is` is a idendity check, to see if the objects are exactly the same.
You would use the `is` check with `None`.
In Markdown, if you want to keep your bullets and index in check, make sure you create a new line after a bulleted object

## Nov 25, 2022 - Friday

**Today I worked on:**

- reverse linked list

**Reflection:**

- these LC problems are hard. They aren't meant to be easy

**Lesson:**

## Nov 22, 2022 - Tuesday

**Today I worked on:**
longest common prefix
**Reflection:**
Today, worked with Andrew this morning which was cool. got to see some nodejs. Unfortuantely, he told me later that his wife tested postive for covid.... he was ok, and I spent all my time with him, but I am just hoping I am ok...
Dealing with just strange edge cases in longest common prefix. annoying..
**Lesson:**

## Nov 21, 2022 - Monday

**Today I worked on:**
best time to buy and sell stock

**Reflection:**
Leetcode is still very challenging, but understanding the solution is definitely more tolerable than coming up with the solution (captain obvious)

**Lesson:**
Sliding window can be dynamic, it saves on time complexity (O(n) vs O(n^2)).
Sliding window, using the two pointers will help me compare two values within a list, to calc a max difference

## Nov 19, 2022 - Saturday

**Today I worked on:**

- valid palindrome (two pointers type)
- ransom note (Hashmap done for fun, from grind 75)
  **Reflection:**
- If I slow down to think about these problems, I can figure it out
  **Lesson:**
- making helper functions can be helpful!
- ord() method in python will return the unicode value associated with a character

## Nov 18 - Friday

**Today I worked on:**

- Contains duplicate (< 5 min - hashmap type)
- re-did - valid anagram (10 min - hashmap type)
- Two Sum (hashmap type)
- group anagrams (my first med!! Hashmap type)

**Reflection:**

- looked into neetcode vs educative's grokking

**Lesson:**

- sort fxn in python is time complexity O(nlogn)
- set function in python has a O(1) time complexity, worst case O(n), with space complexity of O(n)
- len is O(c) time complexity

## Nov 17 - Thursday

**Today I worked on:**

- more flood fill
  **Reflection:**

**Lesson:**

- work smarter not harder. Consider using courses, instead of just plowing thru leetcode
- difference between a tag and button tag
- litle steps forward are still steps
- use 'n' to interatively manage nodejs versions
- https://stackoverflow.com/questions/7718313/how-to-change-to-an-older-version-of-node-js

## Nov 16, 2022 - Wednesday

**Today I worked on:**

- Binary search [iterative approach]
- Flood Fill again

**Reflection:**

- getting back into leetcode. This past Monday was graduation, and last week was career services.
- floodfill is not easy to process
  **Lesson:**
- at 3pm, when I have low energy, I can do a walk and talk, prepare for behavorial interviews

## Nov 7, 2022 - Monday

**Today I worked on:**
continuation of Binary Search

**Reflection:**
Will return to Binary Search
Bootcamp consisted of career services. Working in Huntr and LinkedIn. Will aim to complete one Leetcode today, and for the rest of M-Thursday this week.

**Lesson:**

## Nov 5, 2022 - Saturday

**Today I worked on:**

1. valid palindrome - not hard.. but figuring out the string manipulation with regex took time (finished)
2. invert binary tree - (very challenging, could not do alone)
3. valid anagram - actually easy... (actually completed in 15 min, first try. wohoo!)
4. Binary Search - did not finish

**Reflection:**

- it is an interesting feeling of trying to meet my goal of finishing a certain number of leetcode problems, but my ignorance of certain libraries are slowing me down. The fact that the journey is the reward is hard to hold onto - as I know there is value in learning the RE library, but I need to only learn just enough to accomplish the problem.
- Some of the business logic is actually easy to figure out, but learning a new python library can be challenging. I watched YT videos while working out on REgex, and then had to do more digging.
- Grind 75 notes that this probably should only take 15 minutes. If I knew how to use Regex, I would probably finish the problem in 15 minutes.
- LC2: recursion is still challenging to wrap my head around
- I had a general idea of what to do for binary tree, didn't recognize that recursion was the way to go. Went thru the process again of getting a solution online, and running with it in hopes to understand the solution after processing it.

**Lesson:**

- RE-gex library has multiple string maniupulation methods. I used the findall method, which found a certain substring of strings, and returned a list of individual letters in the correct order (removed punctuation, and the spaces.
- You can actually check to see if one dictionary is equal to another dictionary
- You can check to see if something is in a dictionary using 'in'

## Nov 4, 2022 - Friday

**Today I worked on:**

1. merge two sorted list - needed help. hard
2. best time to buy sell stock - needed help. hard
3. valid palindrome - relatively easy (did not complete, struggling with character fixing)

**Reflection:**

- Linked lists are made up of nodes, that point to other nodes. Each node has both a value, and a pointer to the subsequent node.
- Spent over an hour simply trying to figure out the solution. Needed to go into a solution, and went thru the solution line by line.
- nearly took the entire day to really dig thru this one problem.
- Need to reform the way I prepare, establish more structure.

- Stock question: knowing algo's will help you solve these (this is similar to bubble sort). But the problem, is that it is too slow.... need to use dynamic programming to make this faster

- What I hope to learn: being able to be more calm and collected as I solve a problem.
- LC3 - removing the unicode characters is hard....

**Lesson:**

- LC: need to figure out the core logic of the problem, and what code you need to write to solve that core logic
  Trying to learn the **name** == "**main**" statement:
  https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/

- IF python interpreter is running the source file as 'main' program, it sets the **name** variable to have a value **main**.

- Encoding: assigning numbers to characters
- ASCII(american standard code for information interchange): character encoding standard for communication.
- Unicode: standard for enconding, representing, and handling texts.

## Nov 3, 2022 - Thursday

**Today I worked on:**

1. valid parenthesis - easy

**Reflection:**
Finally solved this!!! Needed the help of the online pseudocode though...
I do see value in this approach, as the solution helps close the gaps in my mind. I will make a video to accompany the solution, explaining the thought process as well.
**Lesson:**
