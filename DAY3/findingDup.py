numbers = list(map(int,input("enter enter numbers").split()))
if len(set(numbers)) == len(numbers):
    print("False")
else:
    print("True")