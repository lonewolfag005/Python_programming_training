num = (input("enter number: "))
inc = True
dec = True
for i in range(len(num)-1):
    if int(num[i+1])!=int(num[i])+1:
        inc = False
    if int(num[i+1])!=int(num[i])-1:
        dec = False
if inc:
    print("inc fancy")
elif dec:
    print("dec fancy")
else:
    print("not fancy")
    