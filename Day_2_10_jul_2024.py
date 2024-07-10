'''Factorial of a non-negative integer, is multiplication of 
all integers smaller than or equal to n. For example factorial 
of 5 is 5*4*3*2*1 which is 120'''

def factorial(num):
    return 1 if (num == 1 or num == 0) else num * factorial(num-1)

num = int(input("Enter the no : "))
print(factorial(num))