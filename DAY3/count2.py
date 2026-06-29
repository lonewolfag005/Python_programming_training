num = list(map(int,input("enter ").split()))
even=0
odd=0
for i in range(len(num)):
    if num[i]%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)
