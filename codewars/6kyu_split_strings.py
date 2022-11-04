"""
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/javascript

8/28/22

--- PROMPT ---
Complete the solution so that it splits the string into pairs of two characters.
 If the string contains an odd number of characters then it should replace the missing
 second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']


--- LESSONS ---


"""


# --- MY SOLUTION ---
def solution(s):
    soln = []
    for i in range(0,len(s),2):
        try:
            couple = s[i] + s[i+1]
        except IndexError:
            couple = s[i] 
        if len(couple) == 2:
            soln.append(couple)
        else:
            soln.append(s[i]+'_')
    return soln

def solution2(s):
    soln = []
    if len(s)%2 == 1:
        s += '_'
    for i in range(0,len(s),2):
        couple = s[i] + s[i+1]
        soln.append(couple)
    return soln



# --- PSUEDOCODE ---
    """
return a list, with groupings of strings by two

for loop with range (step of 2) which will allow
me to iterate for every even index'd string
use range with the step


    """
# --- TEST ---
s = 'tests'

print(solution(s))

print(solution2(s))


# --- ALT SOLN by others ---
