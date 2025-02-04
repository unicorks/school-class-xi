# 1+(1+2)+(1+2+3).....
s = 0
n = int(input("Enter range till where you want sum of sum of natural numbers: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        s +=j
print(s)
