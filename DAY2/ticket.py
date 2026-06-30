t = float(input("enter number: "))
p = float(input("enter price: "))
ct = input("enter category: ")
disc = 0
if t>15:
    disc += 20
if ct == 1:
    disc += 5
if disc > 0:
    amnt = (p*t)-(p*disc/100)
    if t>15 and ct==1:
        print("max ticket and student")
    elif t>15:
        print("max ticket")
    else:
        print("student")
else:
    print("no discount")
print("Total: ",amnt)
