def  factorial(n):
    print("factorial(", n,")" );
    if n == 1 :
        return 1
    else:
        return n * factorial(n-1)

factorial(3)
