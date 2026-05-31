def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter N: "))
if n < 0:
    print("Not defined for negative numbers")
else:
    print(f"Factorial = {factorial(n)}")