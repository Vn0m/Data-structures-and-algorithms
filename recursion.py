# Recursive function to calculate the factorial of a number.
# The function calls itself until the base case (x == 1) is reached.

def factorial(x):
    # Base case: if x is 1, return 1
    if x == 1:
        return 1
    else:
        # Recursive case: multiply x with the factorial of (x - 1)
        return x * factorial(x - 1)

print(factorial(5))

