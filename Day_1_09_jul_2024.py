# '''Decorator basic code'''

# def mydecorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper

# @mydecorator
# def myfunc():
#     print("Hello world")


# myfunc()   

# -------------------------------------------------------------------------------

# '''Basic of Inheritance'''

# class Parent_1():

#     def parent1func(self):
#         print("I am parent_1 class")

# class Parent_2():
#     def parent2func(self):
#         print("I am parent2 class")

# class Child_1(Parent_1,Parent_2):
#     def child1func(self):
#         print("I am child_1 class") 


# obj_1 = Child_1()

# obj_1.parent1func()
# obj_1.parent2func()
# obj_1.child1func()

# ------------------------------------------------------------------------------------

class A():

    def hello(self):
        print("hello A")

class B(A):
    def hello(self):
        print("hello B")
        super().hello()

class C(B):
    def hello(self):
        print("I am child_1 class") 
        super().hello()


obj_1 = C()

obj_1.hello()
