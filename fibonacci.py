# Function for nth Fibonacci number


def fibonacci(n):
    if n < 0:
        print('Incorrect input')
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(input('Write number to calculate Fibonacci number: ')))
