n = 5
def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fac(n-1)*n

print(fac(5))
    
