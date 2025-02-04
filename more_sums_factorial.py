s = 0
n = int(input("Enter range till where you want sum of sum of odd natural numbers: "))
for i in range(1, n+1, 2):
    for j in range(1, i+1, 2):
        s +=j
print(s)

s = 0
n = int(input("Enter range till where you want sum of sum of even natural numbers: "))
for i in range(2, n+1, 2):
    for j in range(2, i+1, 2):
        s +=j
print(s)

s = 0
n = int(input("Enter range till where you want sum of factorial of natural numbers: "))
for i in range(1, n+1):
    m = 1
    for j in range(1, i+1):
        m *= j
    s += m
print(s)
