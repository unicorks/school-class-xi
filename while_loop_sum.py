# sum of natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of natural numbers:"))
i = 1
while i <= n:
    s += i
    i += 1
print(s)

# sum of odd natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of odd natural numbers:"))
i = 1
while i <= n:
    s += i
    i += 2
print(s)

# sum of even natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of even natural numbers:"))
i = 0
while i <= n:
    s += i
    i += 2
print(s)

# sum of square of natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of square of natural numbers:"))
i = 1
while i <= n:
    s += (i**2)
    i += 1
print(s)

# sum of square of odd natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of square of odd numbers:"))
i = 1
while i <= n:
    s += (i**2)
    i += 2
print(s)

# sum of square of even natural numbers
s = 0
n = int(input("Enter the number till where you want the sum of square of even numbers:"))
i = 0
while i <= n:
    s += (i**2)
    i += 2
print(s)

