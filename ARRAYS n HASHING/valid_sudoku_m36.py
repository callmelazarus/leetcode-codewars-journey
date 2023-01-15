"""
https://leetcode.com/problems/valid-sudoku/description/

1/14/2022
hashset
hashmap
arrays

--- PROMPT ---

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

--- LESSONS ---
- collections default dict is VERY similar to a dict, BUT will never raise a keyerror if a value doesn't exist
- default dict is a subdivision of the dict class

- the defaultdict can have values as hashset's which is so cool. The value is now a hashset, which you can add to

--- QUESTIONS ---

--- PSEUDOCODE ---

        Three conditions must be met

1. Each row must contain the digits 1-9 without repetition.
    loop thru each row, create a hashmap that counts the number of numbers
2. Each column must contain the digits 1-9 without repetition.
    loop thru the index values of the rows, to build a hashmap counter
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    build logic that checks the 3x3 subboxes
        - this is the tricky part.
        - NC uses a hashset, and has this crazy trick of 'zooming' out of the subbox, establishing each subbox with it's own index. He realized the fact that if you take the row# or col# and // 3 -> you will get the associated index with that subbox. Something like: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

    Time: O(9^2)
    Space: O(9^2)
    


"""
# --- MY SOLUTION ---

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check just the rows for valid entries
        # instead of hashmap, we could use hashset
        for i in range(len(board)):
            hash1 = {}
            for j in board[i]:
                if j not in hash1 and j != '.':
                     hash1[j] = 1
                elif j in hash1:
                    return False
        
        # access the same index within each sublist
        # start with 0th sublist, 0th index
        # then 1th sublist, 0th index
        # ...
        for i in range(len(board)):
            hash2 = {}
            # iterate thru each row, looking at the index 'i'
            for row in board:
                if row[i] not in hash2 and row[i] != '.':
                    hash2[row[i]] = 1
                elif row[i] in hash2:
                    return False

        """
        checking subbox - this section is from Neetcode
        consider the sub-box with indeces to represent them (zoom out)
        build this by recognizing the rows // 3 -> gives us that index
            no way I would figure this out.... [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
            key (r/3, c/3)

        use a defaultdict (very similar to a typical dict, but never raises a key error)

        this hashmap will have key:value pairs with key (position of subboxes), and values, which note the numbers inside

Example of what the hashset will look like:
        defaultdict(<class 'set'>, {(0, 0): {'8', '6', '5', '3', '9'}, (0, 1): {'9', '7', '5', '1'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'8', '2', '6', '3'}, (1, 2): {'1', '3', '6'}, (2, 0): {'6'}, (2, 2): {'8', '2', '7', '5', '9'}, (2, 1): {'8', '9', '1', '4'}})

        """
        squares = collections.defaultdict(set) # key = r // 3, c // 3

        for r in range(9):
            for c in range(9):
                # if you find empty, keep going
                if board[r][c] == '.':
                    continue
                # if you find duplicate, return false
                if board[r][c] in squares[(r//3, c//3)]:
                    return False
                # ADD to HASHSET (which is the value of key:value pair) otherwise
                squares[(r//3, c//3)].add(board[r][c])
    
        return True
# --- TEST ---


# --- ALT SOLN by others ---
