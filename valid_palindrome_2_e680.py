"""
https://leetcode.com/problems/valid-palindrome-ii/description/

12/20/2022
2 pointers

--- PROMPT ---


--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        return True if palindrome exists, where removing at most one character is acceptable

        return False otherwise

        lets use two pointers, on the outer ends, that gradually meet at the center

        the challenge, is when a mismatch occurs, which can be handled by doing a short step in the loop to check the next element to see if it matches or not. it if does, then advance the other pointer, and continue. We can have a counter or bool to indicate if we've used up the mistake already



"""
# --- MY SOLUTION ---
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        problem text case:
        "ebcbbececabbacecbbcbe"
        test case 464 / 469.... so lame...

        """

        l = 0
        r = len(s)-1
        mistake = 0

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                mistake += 1
                r -= 1
                if s[l] == s[r]:

                    continue
                r += 1
                l += 1
                if s[l] == s[r]:

                    continue
            
        if mistake <= 1:
            return True
        else: 
            return False


# --- TEST ---


# --- ALT SOLN by others ---
