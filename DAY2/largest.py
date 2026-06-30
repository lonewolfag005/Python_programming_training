a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
if a>b and a>c and a>d:
    print(a)
elif b>c and b>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)