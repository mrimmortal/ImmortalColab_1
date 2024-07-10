#Python: Input an integer (n) and computes the value of n+nn+nnnPython: Input an integer (n) and computes the value of n+nn+nnn

#n+nn+nnn

x = input("Input Number")
print(int("%s" % x )+int("%s%s" % (x,x))+int("%s%s%s" % (x,x,x)))

