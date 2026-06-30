nm = input("name plz: ")
mid = len(nm)//2
first = nm[:mid]
second = nm[mid:]
revf = first[::-1]
revs = second[::-1]
name = revf + revs
print(name)