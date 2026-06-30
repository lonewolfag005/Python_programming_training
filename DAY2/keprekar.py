n = int(input("number-->"))
sq = n*n
digits = len(str(n))
right = sq%(10**digits)
left = sq//(10**digits)
if left+right==n:
    print("keprekar")
else:
    print("not keprekar")