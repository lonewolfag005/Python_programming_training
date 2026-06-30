units = int(input("usage"))
if(units<=100):
    print(units*1.5)
elif(100<units<=200):
    print((100*1.5)+((units-100)*2.5))
else:
    print((100*1.5)+(100*2.5)+((units-200)*4))