#Given three integers, print the smallest value.

a = int(input('First Integer: '))
b = int(input('Second Integer: '))
c = int(input('Third Integer: '))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)