# menu driven program
n = int(input("ENTER A NO: "))
choice = input("Enter 1 to check if the number is positive or negative, 2 to calculate its factorial, 3 to calculate area of triangle: ")
if choice == '1':
    if n < 0:
        print("The number is negative")
    elif n > 0:
        print("The number is positive")
    else:
        print("The number is zero")
elif choice == '2':
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print("Factorial is: ", fact)
elif choice == '3':
    # AREA OF TRIANGLE
    a = int(input("Enter side 1: "))
    b = int(input("Enter side 2: "))
    c = int(input("Enter side 3: "))
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Area is : ", area)



