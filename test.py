list1 = set(int(i) for i in input().split() )
list1 = list(list1)
list1.sort(reverse = True)
try:
    print(list1[1])
except:
    print("NULL")