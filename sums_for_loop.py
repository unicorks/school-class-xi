# sum of natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of natural numbers:"))
for i in range(1, n+1):
    s += i
print(s)

# sum of square of natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of square of natural numbers:"))
for i in range(1, n+1):
    s += (i**2)
print(s)

# sum of square of odd natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of square of odd numbers:"))
for i in range(1, n+1, 2):
    s += (i**2)
print(s)

# sum of square of even natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of square of even numbers:"))
for i in range(0, n+1, 2):
    s += (i**2)
print(s)

