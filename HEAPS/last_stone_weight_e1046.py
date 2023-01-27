"""
https://leetcode.com/problems/last-stone-weight/description/

1/26/2022

heap (max heap) python has a minheap built into it  (LC - python3 tab)

OR

Sorting/iterating (LC - python tab)

--- PROMPT ---
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

--- LESSONS ---
use a maxHeap (takes O(N) time)
Python doesn't have maxheap built in, so we will massage the minHeap by multiplying numbers by negative (super clever)
Getting the max is a O(log N) operation

"""
# --- HEAP SOLUTION -- NC

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        

Input is an array of values

Output: weight of last remaining stone (if exists). 
        If no stones exist, return 0

--- NOTES ON HEAPS ---
use a maxHeap (takes O(N) time)
*** Python doesn't have maxheap built in, so we will massage the minHeap by multiplying numbers by negative (super clever)
Getting the max is a O(log N) operation

time: N*Log(N) because we will run the find Max operation N times (N times Log N)

Process:
Compare the two max values. 
Smash them together:
- if values are the same, smash both
- if values differ, small smaller, and replace larger with difference

return the last stone , or 0 if no stoes remain

        """
        # turn values into negative. to allow max heap to turn into a minheap
        stones = [-s for s in stones]

        # turn list into heap - O(N) time:
        heapq.heapify(stones)

        # [-8, -7, -4, -1, -2, 1]
        while len(stones) > 1:
            # pop the smallest 2 elements
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            # remember, these values are negative
            if largest < second_largest:
                diff = largest - second_largest
                heapq.heappush(stones,diff)
            else: # this else is actually not necessary bc this would never fire
                diff = second_largest - largest
                heapq.heappush(stones,diff)

        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])
        

# --- MY SOLUTION ---
"""
-- SORTING METHOD - my solution --
Sort the elements in ascending order
The last two elements are the largest values, with the LAST element being the very largest element
Take the difference of the last two elements, pop off the last element, and then replace the last element with the difference.
Continue to loop thru this until one element is left (or no elements exist)
This process should lead one to use a heap (as that is essentially what we are doing), which is built into python .Check out Neetcode's solution for that soln:

Complexity
Time complexity:
Iterate thru the entire stones list O(N)
Sort method: O(N Log N)
Total: O(N^2 * Log N)

Space complexity:
O(1) - built in sort method sorts the stones in place
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
  
        stones.sort()
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
                stones.sort()
            elif stones[-1] > stones[-2]:
                diff = stones[-1] - stones[-2]
                stones.pop()
                stones[-1] = diff
                stones.sort()
            else:
                diff = stones[-2] - stones[-1]
                stones.pop()
                stones[-1] = diff
                stones.sort()
                
        if len(stones) == 0:
            return 0
        else:
            return stones[0]


