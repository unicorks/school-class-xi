# wap to reverse a string
y = input("Enter a string to check if its a palindrome: ")
length = len(y)
reversed_string = []
for i in range(-1, -(length+1), -1): # length+1 because it doesn't include last index
    reversed_string.append(y[i])
x = ''.join(reversed_string)
if x == y:
    print("palindrome")
else:
    print('nah')
