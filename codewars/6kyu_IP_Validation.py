"""
https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

8/4/2022

LESSONS 
pattern -> for loop to check thru each item in the list
if you have a conditional within that for loop - and you are trying to check for a false/flag -> return FALSE inside that loop
recognize the indentation of the return True on line 23 below... 
think about your indentations, and recognize where you are trying to return 

"""

# MY SOLUTION---

def is_valid_IP(strng):
    list = strng.split(".")
    if len(list) == 4: # checks to see if string is made up of four sections
        for item in list: 
            if item.isdigit() == False: # checking if item is not a number
                return False
            elif item[0] == '0': # checking leading 0 flag
                if len(item) > 1: 
                    return False
            elif int(item) > 255 or int(item) < 0: # check for number range
                return False
        return True
    return False



# TEST---

# print(is_valid_IP('12.255.56.1') )
# print(is_valid_IP('')             )
# print(is_valid_IP('abc.def.ghi.jkl'))
# print(is_valid_IP('123.456.789.0') )
# print(is_valid_IP('12.34.56')     )
# print(is_valid_IP('12.34.56 .1') )
# print(is_valid_IP('12.34.56.-1')  )
print(is_valid_IP('123.045.067.089'))
# print(is_valid_IP('127.1.1.0')     )
# print(is_valid_IP('0.0.0.0')     )
# print(is_valid_IP('0.34.82.53')   )
print(is_valid_IP('192.168.1.300') )




# ALT SOLN by others----

def is_valid_IP_list_comprehension(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))


# ---

def is_valid_IP_similar(strng):
    if len(strng.split(".")) != 4:
        return False
    
    for group in strng.split("."):
        if not group.isdigit() or group != str(int(group)) or not 0 <= int(group) <= 255:
            return False
    
    return True


