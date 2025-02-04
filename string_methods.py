# wap to count how many uppercase, lowercase, digit, words are in a string
s = input('Enter a string: ')
u = l = d = 0
w = len(s.split(' '))
for ch in s:
    if ch.isupper():
        u += 1
    elif ch.islower():
        l += 1
    elif ch.isdigit():
        d += 1
print("No of uppercase: ", u)
print("No of lowercase: ", l)
print("No of digits: ", d)
print("No of words: ", w)
