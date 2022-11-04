"""
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

8/4/2022

--- PROMPT ---
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 
1666 uses each Roman symbol in descending order: MDCLXVI.

solution(1000) # should return 'M'

same symbol can't be used more than 3 times in a row

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

--- LESSONS ---
break problems into smaller conditions
face edge cases as they come

"""


# --- MY SOLUTION ---
def solution(n):
    num_list = list(str(n))
    num_list.reverse() 
    one_roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ten_roman = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hun_roman = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thou_roman = ["M", "MM", "MMM", "IV", "V", "VI", "VII", "VIII", "IX"]
    if num_list[0] != '0': # covers zero edge case
        ones_place = str(one_roman[int(num_list[0])-1]) 
    else:
        ones_place = ""
    try:
        if num_list[1] != "0":
            tens_place = ten_roman[int(num_list[1])-1]
        else:
            tens_place = ""
    except IndexError:
        tens_place = ""
    try:
        if num_list[2] != "0":
            hundreds_place = hun_roman[int(num_list[2])-1]
        else:
            hundreds_place = ""
    except IndexError:
        hundreds_place = ""
    try:
        thousands_place = thou_roman[int(num_list[3])-1]
    except IndexError:
        thousands_place = ""
    return  thousands_place + hundreds_place + tens_place + ones_place

# figure out ones place
# num = 5
# foo = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 1 - 9
# # based on a number
# print(foo[num-1])
    

# # figure out tens place
# num2 = 5 # 50 will be 5
# bar = ["X", "XX", "XXX", "LX", "L", "LX", "LXX", "LXXX", "XC"] # 10 - 90

# print(bar[num-1])

# # figure out 100s place
# num3 = 5 # 50 will be 5
# foo2 = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 100 - 900

# print(foo2[num-1])

# # figure out 1000s place
# num4 = 5 # 50 will be 5
# bar2 = ["M", "MM", "MMM"] # 1000-3000

# print(foo2[num-1])


# --- PSUEDOCODE ---
"""
need to understand HOW to turn numbers into roman numberals...

need to associate the integer with symobls somehow

Looking at number's place seems to be the key here... and just adding them together... basically the value of the string...

how about reversing string? -> starts with one digit



    """
# --- TEST ---
# print(solution(1),'I', "solution(1),'I'")
# print(solution(4),'IV', "solution(4),'IV'")
# print(solution(6),'VI', "solution(6),'VI'")
# print(solution(14),'XIV', "solution(14),'XIV")
# print(solution(21),'XXI', "solution(21),'XXI'")
# print(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
# print(solution(91),'XCI', "solution(91),'XCI'")
# print(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
print(solution(1000), 'M', 'solution(1000), M')
# print(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
# print(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")

# --- ALT SOLN by others ---
