def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))

def sumSquare(n):
    if n<=0: 
        return 1
    return (n**2+sumSquare(n-1))
print(sumSquare(2))