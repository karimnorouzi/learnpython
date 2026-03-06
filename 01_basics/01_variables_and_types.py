# ============================================================
# Python Basics – Variables and Data Types
# ============================================================

# --- Integers ---
age = 25
year = 2024
print("Integer:", age, type(age))

# --- Floats ---
pi = 3.14159
temperature = -7.5
print("Float:", pi, type(pi))

# --- Strings ---
name = "Alice"
greeting = f"Hello, {name}!"
print("String:", greeting, type(name))

# --- Booleans ---
is_student = True
has_passed = False
print("Boolean:", is_student, type(is_student))

# --- None ---
result = None
print("None:", result, type(result))

# --- Type conversion ---
num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
print("Converted int:", num_int, "float:", num_float)

# --- Lists ---
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print("List:", fruits)
print("First item:", fruits[0], "Last item:", fruits[-1])

# --- Tuples (immutable) ---
coordinates = (10.0, 20.0)
print("Tuple:", coordinates)

# --- Dictionaries ---
person = {"name": "Bob", "age": 30, "city": "Tehran"}
person["email"] = "bob@example.com"
print("Dict:", person)
print("Name:", person["name"])

# --- Sets ---
unique_numbers = {1, 2, 3, 2, 1}
print("Set:", unique_numbers)
