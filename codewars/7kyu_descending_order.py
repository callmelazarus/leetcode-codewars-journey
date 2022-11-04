def descending_order(num):
    list_num = list(str(num)) # turns number into a list of strings
    list_num.sort(reverse=True) # re-arrange order of number in decending order
    new_num = ''.join(list_num) # converts list to number, in string form
    return int(new_num) # returns number as an integer
    
    # re-arrange the numbers, from largest to smallest
    # working with integers here.
    # need to conver to string
    # sort string
    # turn to int


num = 123456789
print(descending_order(num))