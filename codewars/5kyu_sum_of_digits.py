def digital_root_mine2(n):
    num_to_list = list(str(n))
    root = 0
    if n == 0:
        return 0
    for num in num_to_list:
        root += int(num)
    if root >= 10:
        root = digital_root_mine2(root)
    return root



def digital_root_clever(n):
    return n%9 or n and 9 # would need to know that modulo 9 would get me there faster

def digital_root(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root(root) # I guess you can call the function within the function??
    return root

print(digital_root_mine2(16))
print(digital_root_mine2(942))
print(digital_root_mine2(100))
print(digital_root_mine2(532834277482598338))


# solution below is limited...

def digital_root_NG(n):
    num_to_list = list(str(n))
    total_num = 0
    second_iteration = 0
    third_it = 0
    for num in num_to_list:
        total_num += int(num)
    if total_num > 10:
        total_num_rev = list(str(total_num))
        for num in total_num_rev:
            second_iteration += int(num)
    if second_iteration > 10:
        total_num_rev = list(str(second_iteration))
        for num in total_num_rev:
            third_it += int(num)
    # return minimum, that isn't 0
    final_list = [total_num, second_iteration, third_it]
    root = 100
    for item in final_list:
        if item < root and item != 0:
            root = item
    return root

# this doesn't work for very large numbers.....

def digital_root_mine(n):
    num_to_list = list(str(n))
    total_num = 0
    second_iteration = 0
    third_it = 0
    for num in num_to_list:
        total_num += int(num)
    if total_num >= 10:
        total_num_rev = list(str(total_num))
        for num in total_num_rev:
            second_iteration += int(num)
    if second_iteration >= 10:
        total_num_rev = list(str(second_iteration))
        for num in total_num_rev:
            third_it += int(num)
    # return minimum, that isn't 0
    final_list = [total_num, second_iteration, third_it]
    root = 100
    for item in final_list:
        if item < root and item != 0:
            root = item
    return root