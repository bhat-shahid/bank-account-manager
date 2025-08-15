def factorial(n):
    if n==1:
        return 1
    else:
        num=n*factorial(n-1)
        return num
x=factorial(5)
print(x)

