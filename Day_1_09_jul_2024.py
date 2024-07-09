'''Decorator basic code'''

def mydecorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@mydecorator
def myfunc():
    print("Hello world")


myfunc()            