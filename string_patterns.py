# string slicing
# str1[start:end:step]

#wap to print a name in pattern
n = input("Enter some name: ")
for i in range(len(n)+1):
    print(n[0:i])

# wap to print pattern
c = input("Enter a character whose pattern you want to print: ")
n = int(input("How many times? "))
pattern = ''
for i in range(n):
    pattern += c
    print(pattern)
