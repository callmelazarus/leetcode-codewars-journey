"""
https://leetcode.com/problems/koko-eating-bananas/description/

1/11/2022
binary search

--- PROMPT ---
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

--- LESSONS ---
- if you have a sorted array that you are searching - THINK BINARY SEARCH
- on the surface, this doesn't seem like a binary search problem... it is interesting to think of how when you try to optimize for a solution by establishing a list of potential answers (k_list) which is sorted, binary search comes into play

--- QUESTIONS ---

--- PSEUDOCODE ---
        :type piles: List[int]
        :type h: int
        :rtype: int

Variables:
        n - piles of bananas
        piles[n] - # of bananas in pile 

        h - hours available

        return min integer 'k' - the eating speed for koko

breaking the problem down:

        at most, koko can only eat one pile per hour
            len(p) <= h

        max k -> max pile value
        the range of k is
            [1, 2, .... max(pile[i])]


PROCESS:

            piles = [3, 6, 7, 11]
            h = 8
            k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                 l              k                r

            We are going to do a binary search O(log maxp)thru the k list, testing out various k rates
            loop thru the piles list O(p), calculating a total time to eat all the bananas based on the specific k
            check to see if total time is less than 'h'. 
            
            If less, than update result, and then try to find a more optimized solution, by shifting right pointer to just less than k
            If the total hours exceed 'h', then you need a faster 'k', thus shift left pointer to k + 1.

        time: O(p*log maxp)

"""
# --- MY SOLUTION ---
        # create left and right pointers
        l = 1
        r = max(piles)

        # initialize with max(piles), which is the max answer that k can be
        res = max(piles)
        
        while l <= r:
            # mid k
            k = (l + r) // 2
            # calc total hours it takes to eat all bananas, based on 'k'
            totalTime = 0

            # loop thru the piles to figure out total time to eat pile, given a certain k
            for p in piles:
                # calculate how many hours it takes to eat all piles in piles array
                # p / k
                # round up the hours
                totalTime += math.ceil(p / k)

            # binary search
            # if we are able to all the bananas faster than h, at the given 'k' rate, updated the result
            if totalTime <= h:
                res = min(res, k)
                # check for a faster rate, which is a lower 'k'
                # update the r pointer
                r = k - 1
            else:
                # rate was too small, so we need a larger rate
                l = k + 1

        return res

            

# --- TEST ---


# --- ALT SOLN by others ---
