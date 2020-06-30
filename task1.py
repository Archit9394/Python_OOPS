# 1.	Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
from math import sqrt
def square_root(D):
    C=50
    H=30
    return sqrt(2*C*D/H)

D=int(input("Enter a D value:"))
print (square_root(D))
