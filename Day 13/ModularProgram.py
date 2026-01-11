#1st file
import math
print(math.pi)

import myModule
print(myModule.myFunc(6))
print(myModule.anotherFunc(2))

#2nd file
def myFunc(x):
    return x+5
def anotherFunc(x):
    return x//5
