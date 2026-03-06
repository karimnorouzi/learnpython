# ============================================================
# Python Basics – Control Flow
# ============================================================

# --- if / elif / else ---
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# --- for loop ---
print("\nSquares 1–5:")
for i in range(1, 6):
    print(f"  {i}^2 = {i ** 2}")

# --- for loop over a list ---
fruits = ["apple", "banana", "cherry"]
print("\nFruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# --- while loop ---
count = 0
print("\nCounting to 4:")
while count < 5:
    print(f"  count = {count}")
    count += 1

# --- break and continue ---
print("\nSkip 3, stop at 7:")
for n in range(10):
    if n == 3:
        continue
    if n == 7:
        break
    print(f"  n = {n}")

# --- List comprehension ---
squares = [x ** 2 for x in range(1, 6)]
print("\nList comprehension – squares:", squares)

# --- Conditional expression (ternary) ---
x = 10
label = "even" if x % 2 == 0 else "odd"
print(f"\n{x} is {label}")
