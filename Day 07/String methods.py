L1 = '_'
L2 = '_'
L3 = '_'
L4 = '_'
L5 = '_'

print("Guess the word: _ _ _ _ _")

while True:
    a = input("Guess the character: ")

    if a == 'g':
        L1 = 'g'
    elif a == 'e':
        L2 = 'e'
        L3 = 'e'
    elif a == 'k':
        L4 = 'k'
    elif a == 's':
        L5 = 's'
    else:
        print("Wrong character")

    print(L1, L2, L3, L4, L5)

    if L1 == 'g' and L2 == 'e' and L3 == 'e' and L4 == 'k' and L5 == 's':
        print("Congrats! The word is GEEKS")
        break




#.strip(),.len(),.lower(),.upper(),.split()

a=input('Enter something:')
print(a.strip())

print(len(a))

print(a.lower())

print(a.upper())

print(a.split())
