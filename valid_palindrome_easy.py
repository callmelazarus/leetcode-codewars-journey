"""
https://leetcode.com/problems/valid-palindrome/

11/4/2022, finished 11/5
Roughly took 2 hours (including time to complete)

--- PROMPT ---
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


--- LESSONS ---
Received intial exposure to RE-gex libary, a string manipulation library. Knowing the correct methods will unlock the ability to do amazing things with strings


"""

import re
    # remove alpha-numeric values
    # c = re.sub(r'[^\w\s]','',a)

# --- MY SOLUTION ---
def isPalindrome(s: str) -> bool:
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
print('test for last:', isPalindrome(last))




# --- ALT SOLN by others ---
