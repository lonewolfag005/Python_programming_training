tuple_list=eval(input("enter "))
k = int(input("enter column"))
m = 1
for tup in tuple_list:
    product = product*tup[k]
print(f"Product of values: {k}: {product}")
