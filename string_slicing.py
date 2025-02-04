# string slicing
# str1[start:end:step]
# wap to read a string and display it in reverse order for eg if the string is python, it should display nohtyp
x = input("Enter a string to reverse: ")
print(x[::-1])
# wap to input an integer and check if it contains any zero in it
y = input("Enter the integer for which you want to check whether it contains zero or not: ")
if '0' in y:
    print("yes it does")
else:
    print('nah it doesnt')
# wap to calculate number of vowels and consonants and special characters in a string
z = input("Enter the string in which you want to count no of vowels, consonants and other characters: ")
vowels = 0
cons = 0
other = 0
for i in z:
    m = i.lower()
    if m in ['a','e','i','o','u']:
        vowels += 1
    elif ord(m) >= 97 and ord(m) <=122 and m not in ['a','e','i','o','u']:
        cons += 1
    else:
        other += 1
print('Vowels: ', vowels)
print('Consonants: ', cons)
print('Other: ', other)

