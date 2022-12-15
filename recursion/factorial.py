# create a function that takes the factorial of a number

def factorial(num):
  
# base case, when the num is reduced to 1, you know the factorial is just 1
  if num == 1:
    return 1

# the recursive call will decrement the value
# recognize that what you are trying to return is the number * the factorial of the number less than it
  return num * factorial(num -1) 


# num * num -1 * num - 2 .....


num = 4
# 5 * 4 * 3 * 2 * 1
res = factorial(num)

print(res)
