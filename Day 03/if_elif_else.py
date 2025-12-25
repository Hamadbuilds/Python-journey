# Day 3: if / elif / else

height=input('Input height:')

if int(height)>3:
    print("Not allowed")
elif int(height)<1:
    print("not allowed")
else:
        print("You can ride")

age=input('Input  your age:')

if int(age)>16:
    print("you are older than 16")
elif int(age)==16:
    print("You are 16")
else:
        print("You are younger than 16")
