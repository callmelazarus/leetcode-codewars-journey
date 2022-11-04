def words_to_marks_mine(s):
    soln = 0
    for letter in s:
        adj_letter_to_num = ord(letter)-96
        soln += adj_letter_to_num
    return soln

def words_to_marks(s):
    return sum(ord(c)-96 for c in s)

print(words_to_marks('test'))