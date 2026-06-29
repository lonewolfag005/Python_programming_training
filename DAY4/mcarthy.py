def mcCarthy91(num):
    if num > 100:
        return num - 10
    else:
        return mcCarthy91(mcCarthy91(num + 11))
num=int(input("N:"))
print("Number:",mcCarthy91(num))