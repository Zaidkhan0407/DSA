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

def prefixcheck(s,prefix):
	if len(prefix)==0:
		return True
	if len(s)==0:
	    return False
	if s[0]!=prefix[0]:
		return False
	return prefixcheck(s[1:],prefix[1:])
s=""
prefix="a"
print(prefixcheck(s,prefix))

def computesum(arr):
	if len(arr)<=0:
		return 0
	return arr[0]+computesum(arr[1:])
arr=[]
print(computesum(arr))
		
def countk(s,k):
    if k<=0:
        return ""
    return s+countk(s,k-1)
print(countk("abc",3))


def RSC(s,sub):
    if len(s)<=0 and len(sub)<=0:
        return True
    if len(s)<=0:
        return False
    if s[0]!=sub[0]:
        return RSC(s[1:],sub)
    return RSC(s[1:],sub[1:])
s="axc"
sub="ahbg"
print(RSC(s,sub))	