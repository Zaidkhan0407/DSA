#Factorial
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))
### sum of squares
def sumSquare(n):
    if n<=0: 
        return 1
    return (n**2+sumSquare(n-1))
print(sumSquare(2))

### sum of odd squares
def sum_odd_squares(n):
    if n <= 0:
        return 0  # 🛑 Base case: ends the chain here
    
    if n % 2 == 0:
        return sum_odd_squares(n - 1)  # Skips even, recurses
    
    return n * n + sum_odd_squares(n - 2)  # 💥 Actual logic for odd

def palindrome(st):
	if len(st)<=1:
		return True
	if st[0]!=st[-1]:
		return False
	return palindrome(st[1:-1])