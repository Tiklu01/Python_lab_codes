def isPrime(n,i=2):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    elif i*i>n:
        return True
    else:
        return isPrime(n,i+1)
num = int(input("Enter a number = "))
if isPrime(num):
    print(f"the number {num} is prime")
else:
     print(f"the number {num} is not prime")