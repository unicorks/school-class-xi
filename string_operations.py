# wap to input a string and traverse a string
x = input("Enter a string: ")
for i in x:
    print(i*3, end='')
print('\n')


# wap to reverse a string
y = input("Enter a string to reverse: ")
length = len(y)
for i in range(-1, -(length+1), -1): # length+1 because it doesn't include end value in range
    print(y[i], end='')
print("\n")


# wap to count vowels in a string
z = input("Enter a string in which you want to count vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in z:
    if i.lower() in vowels:
        count += 1
print("Total vowels are:", count)


# concatenation and replication/repetition
print("what"+" in the world") # note: u can't add no and string like 3+"what". it should be '3' + 'what'
print("mom "*3) # note: string*string is not allowed
# if u do above mentioned errors u will get invalid operand type error

