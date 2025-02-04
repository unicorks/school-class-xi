print("---QUADRATIC EQUATION SOLVER---")
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant term: "))

print("Your equation is: ", a, "x^2 + ", b, "x + ", c)
print("Solution: ")
print((-b + ((b**2)-(4*a*c))**0.5)/2*a)
print((-b - ((b**2)-(4*a*c))**0.5)/2*a)
