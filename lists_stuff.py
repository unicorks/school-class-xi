# wap to find out the no of occurences of an element. element is given by user from the list
a = [1, 1, 3, 4,2, 5, 3, 3, 2, 9]
print(a)
e = int(input("Enter the no whose occurences you wanna count:"))
print(a.count(e))
# wap to insert an element at 0th location and 4th location of a list.
f = input("which element u wanna insert at 0th position: ")
a.insert(0, f)
g = input("which element u wanna insert at 4th position: ")
a.insert(4, g)
print("After insertion: ", a)
# wap to delete an element from the list at a given index no.index no should be user input
h = int(input("enter index whose element you wanna delete"))
a.pop(h)
print(a)

