# bubble sort
L = [21, 8, 15, 27, 2, 80, 1]
n = len(L)
no_of_comps = 0
for i in range(n):
    for j in range(n-1-i):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print("###SORTED LIST###")
print(L)

