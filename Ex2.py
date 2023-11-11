list1 = [1, 2, 3, 2, 4, 3, 5, 6, 4]
list2 = []
for item in list1:
    if item not in list2:
        list2.append(item)
print( list2)