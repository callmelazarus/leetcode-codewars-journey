"""
https://leetcode.com/problems/valid-palindrome/

11/4/2022, finished 11/5
Revisited: 11/19/22

PATTERN: 2 pointer

Roughly took 2 hours (including time to complete first try - trying to figure out regex was most of the time)


--- PROMPT ---
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


--- LESSONS ---
Received intial exposure to RE-gex libary, a string manipulation library. Knowing the correct methods will unlock the ability to do amazing things with strings

ord() method in python will return the unicode value. You can check to see if an ASCI character is a letter or number, cased on a comparison of the ord() value of the characters

"""

import re
    # remove alpha-numeric values
    # c = re.sub(r'[^\w\s]','',a)

# --- MY SOLUTION ---

import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

    # input -  string
    # turn to lowercase
    # remove all non-alphanumeric values
    # check if letters reaad the same both ways
    # if they do - return TRUE
        if s == " ":
            return True
        lower = s.lower()
        # remove non-alphanumeric values from string
        pruned = re.findall('[a-z0-9]', lower)
        # print('pruned:', pruned)
        # joint into one continguous string
        final = "".join(pruned)
        # print('final:', final)

        # num loops = len(string) // 2
        num_loops = len(final)//2
        
        for i in range(num_loops):
            if i == 0:
                if final[0] != final[-1]:
                    return False
            else:
              if final[i] != final[-1*i-1]:
                  return False
        return True
      
    def isAlphaNum(self, c):
      return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))


    def isPalindrome_2(self, s):
      # initialize left and right
      l, r = 0, len(s) - 1

      while l < r:
        # check if left character is not alphanumeric
        while l < r and not self.isAlphaNum(s[l]):
          l += 1
        # check if right characters is not alphanumeric
        while l < r and not self.isAlphaNum(s[r]):
          r -= 1
        # check to see if the values are NOT equal
        if s[l].lower() != s[r].lower():
          return False
        l += 1
        r -= 1
      return True


def isPalindrome_first(s: str) -> bool:
    if s == " ":
        return True
    #lower case values, lower returns a string
    lowered_case= s.lower()
    # Select ONLY letters and numbers
    # https://docs.python.org/3/library/re.html
    # c = re.compile(r'[^\w\s]','',a) `# first attempt
    only_letters_list = re.findall(r'[a-z0-9]',lowered_case) 

    # join items in list to encoded string
    encoded_string = ''.join(only_letters_list)


    # main logic that can check mirror
    # this will only work for even numbered strings
    n = len(encoded_string)
    
    mid_point = n/2
    for i in range(int(mid_point)):
      # first check
      if i== 0 and encoded_string[0] == encoded_string[-1]:
        continue
      elif encoded_string[i] != encoded_string[-1*i+-1]:
            return False
    return True


# --- PSUEDOCODE ---
"""

Cleaning up string...
convert values to lowercase letters <- .lower (returns something)
remove all non-alpha/numeric values <- ???
remove whitespace <- string.split(), and then ''.join(split_string)

Main logic of the palindrome:
if the string is the same forward and backwards -> true
else -> false
My thought process was, do a range from 0 to midpoint
loop through the first half, comparing it to the corresponding other half. 
If they don't match, return False.


"""
# --- TEST ---
s = "A man, a plan, a canal: Panama"
last = "ab_$a"

# print('test for s:', isPalindrome(s))
a = Solution()
jeff = a.isPalindrome_2(s)
print('test for last:', jeff)




# --- ALT SOLN by others ---
