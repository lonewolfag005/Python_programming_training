r = int(input("rain amount: "))
if r<1:
    print("no rain")
elif 1<=r<5:
    print("light rain")
elif 5<=r<10:
    print("medium rain")
else:
    print("heavy rain")