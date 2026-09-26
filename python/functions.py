# ==========================================
# Day 2 - Python Functions
# ==========================================

# 1. Basic Functions
def greet(name):
    return f"Hello, {name}"


print(greet("ABC"))


# 2. Parameters
def add(a, b):
    return a + b


print(add(10, 20))


# 3. Default Arguments
def welcome(name="ABC"):
    return f"Welcome, {name}"


print(welcome())
print(welcome("XYZ"))


# 4. *args
def add_numbers(*args):
    return sum(args)


print(add_numbers(1, 2, 3, 4))


# 5. **kwargs
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


show_details(name="ABC", role="Software Engineer")


# 6. Lambda
square = lambda x: x * x

print(square(5))


# 7. List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)


# 8. Dictionary Comprehension
square_dict = {x: x * x for x in numbers}

print(square_dict)


# 9. Set Comprehension
even_numbers = {x for x in numbers if x % 2 == 0}

print(even_numbers)
