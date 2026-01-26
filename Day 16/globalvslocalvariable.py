var=9
loop=True
newVar=23
def func(x):
    global loop
    loop=7
    newVar=7
    print(var)
    if x==5:
        return newVar
func(2)
def otherFunc():
    newVar=5
    print(newVar)
otherFunc()
print(loop)
