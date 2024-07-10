# '''Factorial of a non-negative integer, is multiplication of 
# all integers smaller than or equal to n. For example factorial 
# of 5 is 5*4*3*2*1 which is 120'''

# def factorial(num):
#     return 1 if (num == 1 or num == 0) else num * factorial(num-1)

# num = int(input("Enter the no : "))
# print(factorial(num))

# ------------------------Play with strings-------------------

# x = "immortals world"
# y = "always"

# print(x)
# print(x[2])
# print(x[-2])
# print(x[0:3])
# print(x.split(" "))
# print(x.startswith("i"))
# print(x.startswith("x"))
# print(x.endswith("s"))
# print(x.replace("i","ee"))
# print(x.upper())

# -------------------can you check now3a----area of circle-------------------
def area_of_circle(ip):
    area =  3.14 * ip * ip
    return area

ip = float(input("Enter the radius :"))
print(area_of_circle(ip))

