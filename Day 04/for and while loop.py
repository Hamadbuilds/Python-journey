for x in range(0,10,2): #start,stop,step
    print(x)

loop=True
while loop:
    name=input('Insert something:')
    if name=='stop':
        loop=False
        break
