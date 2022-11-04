"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

Date: 8/4/2022

--- PROMPT ---
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

--- LESSONS ---
easier than I thought... 
did not apply array knowledge

"""


# --- MY SOLUTION ---
def move_zeros(lst):
    non_zero = []
    zero = []
    for num in lst:
        if num == 0:
            zero.append(num)
        else:
            non_zero.append(num)
    final = non_zero
    final.extend(zero)
    return final



# --- PSUEDOCODE ---
    """
preserving order...
takes a list -> and is able to move all 0's to the end of the list...

seems almost simple...

potential challenges
need to be able to handle multiple lists

    """
# --- TEST ---
# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),[1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# print(move_zeros([0, 0]), [0, 0])
# print(move_zeros([0]), [0])
# print(move_zeros([]), [])


# --- ALT SOLN by others ---
