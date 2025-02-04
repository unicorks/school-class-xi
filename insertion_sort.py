# insertion sort
alist = [10, 7, 5, 1, 4, 9]
print("Original list:", alist)
n = len(alist)
for i in range(1,n):
    key = alist[i]
    print("Key: " ,key)
    j = i - 1
    while j >= 0 and alist[j]>key:
        print(alist)
        alist[j+1]=alist[j]
        print(alist)
        j = j-1
    alist[j+1]=key
    print(alist)
print("Sorted list is, ", alist)
