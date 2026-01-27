x='string'
y=23
boo=True

print(type(y))
print(x.count('1'))

def func():
    print('hello')
func()

class number:
    def __init__(self,num):
        self.var=23
    def display(self,x):
        print(x)
num=number(23)
print(num)
num.display(num.var)
