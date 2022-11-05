"""
https://leetcode.com/problems/valid-palindrome/

11/4/2022

--- PROMPT ---
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



--- LESSONS ---

"""

import re
    # remove alpha-numeric values
    # c = re.sub(r'[^\w\s]','',a)

# --- MY SOLUTION ---
def isPalindrome(s: str) -> bool:
    if s == " ":
        return True
    #lower case values, lower returns a string
    a = s.lower()
    # remove alpha-numeric values
    # sub
    # https://docs.python.org/3/library/re.html
    c = re.sub(r'[^\w\s]','',a) # for unicode
    # a.encode("ascii", errors="ignore").decode()
    # remove space, presenting words as letters
    d = c.split()
    # join items in list
    e = ''.join(d)

    # main logic that can check mirror
    # this will only work for even numbered strings
    n = len(e)
    
    mid_point = n/2
    for i in range(int(mid_point)):
      # first check
      if i== 0 and e[0] == e[-1]:
        continue
      elif e[i] != e[-1*i+-1]:
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
