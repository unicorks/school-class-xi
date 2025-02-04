s = 0
n = int(input("Enter range till where you want sum of reciprocal of factorial of natural numbers: "))
for i in range(1, n+1):
    m = 1
    for j in range(1, i+1):
        m *= j
    s += 1/m
print(s)

s = 0
n = int(input("Enter range till where you want sum of factorial of odd natural numbers: "))
for i in range(1, n+1, 2):
    m = 1
    for j in range(1, i+1):
        m *= j
    s += m
print(s)



