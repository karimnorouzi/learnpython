# ============================================================
# Python Basics – Functions
# ============================================================


# --- Simple function ---
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"


print(greet("Alice"))


# --- Default arguments ---
def power(base, exponent=2):
    """Return base raised to exponent (default: square)."""
    return base ** exponent


print(power(3))       # 9
print(power(2, 10))   # 1024


# --- *args: variable positional arguments ---
def total(*numbers):
    """Return the sum of all provided numbers."""
    return sum(numbers)


print(total(1, 2, 3, 4))   # 10


# --- **kwargs: variable keyword arguments ---
def describe(**attributes):
    """Print each attribute as key: value."""
    for key, value in attributes.items():
        print(f"  {key}: {value}")


describe(name="Bob", age=30, city="Tehran")


# --- Lambda (anonymous) functions ---
square = lambda x: x ** 2
print(square(7))   # 49


# --- Higher-order functions ---
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))
print("Evens:", evens)
print("Doubled:", doubled)


# --- Recursive function ---
def factorial(n):
    """Return n! using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


for i in range(6):
    print(f"  {i}! = {factorial(i)}")
