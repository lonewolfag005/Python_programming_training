D=input("day:")
A=int(input("attendees:"))
FW=( "MON" , "TUE" , "WED" , "THU" )
LW=( "FRI" , "SAT" , "SUN" )
if D in FW:
    if A>=700 and A<=1000:
        print("successful")
    else:
        print("Unsuccessful")
elif D in LW:
    if A>=1500:
        print("successful")
    else:
        print("Unsuccessful")
else:
    print("invalid")