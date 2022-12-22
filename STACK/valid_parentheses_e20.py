"""
https://leetcode.com/problems/valid-parentheses/

Date: 8/5/2022 / revisit 11/3/2022

--- PROMPT ---
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

--- LESSONS ---
This is still such a hard problem for me...

Couldn't solve this. Searched for pseudocode answer online, and worked from there.
The correct logic itself was hard to establish


"""

# --- MY SOLUTION ---

def isValid(s: str) -> bool:
    dict_soln = {'(':')', '{':'}', '[':']'}
    open_b =['(', '{', '[']
    close_b =[')', '}', ']']
    cache = []
    for bracket in s:
        if bracket in open_b:
            cache.append(bracket)
        elif bracket in close_b:
            if cache == []:
                return False
            elif dict_soln.get(cache[-1]) == bracket:
                cache.pop()
            else:
                return False
    if cache == []:
        return True
    else:
        return False

def isValid(s: str) -> bool:
    # setup solution set of appropriate pairs
    dict_soln = {'(':')', '{':'}', '[':']'}
    open_b =['(', '{', '[']
    close_b =[')', '}', ']']
    cache = []
    for bracket in s:
        # first check if its open bracket. if yes -> add to cache
        if bracket in open_b:
            cache.append(bracket)
            
        # check if its close bracket. if yes...
        elif bracket in close_b:
            # if cache is empty, and you come accross a closed backet - you know there is no opening bracket pair preceding it. RETURN FALSE
            if cache == []:
                return False
            # if cache has stuff -> for closing bracket, check if last item in cache (which should be an open bracket), has the correct matching closing bracket.
            # if brackets match - POP the bracket out of the cache.
            elif dict_soln.get(cache[-1]) == bracket:
                cache.pop()
            # if brackets DONT match, return a FALSE, that means the pairing of brackets is NG
            else:
                return False
    # if cache is empty - all brackets are matched. Return TRUE
    if cache == []:
        return True
    # otherwise, return False!
    else:
        return False

        


# --- PSUEDOCODE ---
    """

    core logic: what makes a valid parenthesis, a valid parenthesis?

from: https://www.educative.io/answers/the-valid-parentheses-problem

Declare an empty stack.
Push an opening parenthesis on top of the stack.
In case of a closing bracket, check if the stack is empty.
If not, pop in a closing parenthesis if the top of the stack contains the corresponding opening parenthesis.
If the parentheses are valid,​ then the stack will be empty once the input string finishes.

    """
# --- TEST ---

a=isValid("{[]}") # true. works
print('a: should be true//', a)

b = isValid("(])") # false
print('b: should be false//', b)

c = isValid("({{{])") # false
print('c: should be false//', c)

d = isValid("({{}}[]())") # true
print('d: should be true//', d)

# --- ALT SOLN by others ---
