"""
https://leetcode.com/problems/add-binary/description/

10/12/2023

--- PROMPT ---

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


--- LESSONS ---
I do feel like reading code is a little bit easier, 2 months into the job. I had a general intuition on how to solve the problem, but still needed gpt to help me out


--- QUESTIONS ---

--- PSEUDOCODE ---

        Starting from the rightmost side, add the values
        then going from right to left, adjust values
        if the value is 0, leave it alone
        if value is 1, leave it alone
        if value is 2 - turn that into a 0, and add 1 to the left value


"""
# --- MY SOLUTION ---
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        Starting from the rightmost side, add the values
        then going from right to left, adjust values
        if the value is 0, leave it alone
        if value is 1, leave it alone
        if value is 2 - turn that into a 0, and add 1 to the left value

        """

        i = len(a) - 1 # pointers to traverse string (match index, so reduce by 1)
        j = len(b) - 1 # pointers to traverse string (match index, so reduce by 1)
        carry = 0  # to store carry for each step of the addition

        result = []  # List to store the result, will convert to string at the end

        # Loop as long as there are characters left in either string or a carry is left
        while i >= 0 or j >= 0 or carry:
            # Sum of two bits + any carry from the previous step
            sum_val = carry
            if i >= 0:
                # add the a's value to sum_val (and if there is any carry)
                sum_val += int(a[i])
                i -= 1
            if j >= 0:
                # add the b's value to sum_val (and if there is any carry)
                sum_val += int(b[j])
                j -= 1

            # Append the current bit to the result 
            # alt to % and // - could use conditional statements

            # if sum val is 2, add 0
            # if sum val is 1, add 1
            # if sum val is 0, add 0
            result.append(str(sum_val % 2))

            # Update the carry
            carry = sum_val // 2

        # Since we've been adding bits to the result in reverse order, we need to reverse the order of list [::-1], and turn that list into a string (.join)
        return ''.join(result[::-1])



# --- TEST ---


# --- ALT SOLN by others ---
