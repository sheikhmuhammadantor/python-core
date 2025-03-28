# Function all like JS functions;
# Function 1:
def factorial(n=5):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120 (5! = 5*4*3*2*1)

# Function 2:
def fibonacci(n, memo={}):
    if n in memo:
        # print(n)
        return memo[n]
    if n <= 2:
        # print(n)
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(10))  # Output: 55 (10th Fibonacci number)

# Function 3:
def power(x, y, result=1):
    if y == 0:
        return result
    return power(x, y - 1, result * x)

print(power(2, 5))  # Output: 32 (2^5)
