```python
"""
PYTHON OOP CONCEPTS
===================

Topics covered:
1. Classes and Objects
2. Constructor (__init__)
3. Instance Variables
4. Class Variables
5. Instance Methods
6. Encapsulation
7. Inheritance
8. Multilevel Inheritance
9. Multiple Inheritance
10. Polymorphism
11. Duck Typing
12. Abstraction
13. super()
14. Class Methods
15. Static Methods
16. Magic / Dunder Methods
17. Composition
18. Complete Real-World Example
"""


# ============================================================
# 1. CLASSES AND OBJECTS
# ============================================================

class Student:
    name = "Haripriya"
    age = 24


student1 = Student()

print("\n--- 1. Classes and Objects ---")
print(student1.name)
print(student1.age)


# ============================================================
# 2. CONSTRUCTOR - __init__()
# ============================================================

class StudentInfo:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = StudentInfo("Haripriya", 24)
student2 = StudentInfo("Rahul", 25)

print("\n--- 2. Constructor ---")
print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# ============================================================
# 3. INSTANCE VARIABLES AND CLASS VARIABLES
# ============================================================

class Employee:

    company = "CloudStory"  # Class variable

    def __init__(self, name, salary):
        self.name = name       # Instance variable
        self.salary = salary   # Instance variable


emp1 = Employee("Haripriya", 25000)
emp2 = Employee("Rahul", 30000)

print("\n--- 3. Instance and Class Variables ---")

print(emp1.name)
print(emp1.salary)

print(emp2.name)
print(emp2.salary)

print(emp1.company)
print(emp2.company)


# ============================================================
# 4. METHODS
# ============================================================

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


calculator = Calculator()

print("\n--- 4. Methods ---")
print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))


# ============================================================
# 5. ENCAPSULATION
# ============================================================

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Haripriya", 10000)

print("\n--- 5. Encapsulation ---")

account.deposit(5000)
account.withdraw(2000)

print("Balance:", account.get_balance())

# Private variable cannot normally be accessed directly:
# print(account.__balance)

# Name mangling can access it:
print("Private balance using name mangling:",
      account._BankAccount__balance)


# ============================================================
# 6. INHERITANCE
# ============================================================

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

print("\n--- 6. Inheritance ---")
dog.eat()
dog.bark()


# ============================================================
# 7. MULTILEVEL INHERITANCE
# ============================================================

class Grandparent:

    def property(self):
        print("Grandparent property")


class Parent(Grandparent):

    def house(self):
        print("Parent house")


class Child(Parent):

    def car(self):
        print("Child car")


child = Child()

print("\n--- 7. Multilevel Inheritance ---")
child.property()
child.house()
child.car()


# ============================================================
# 8. MULTIPLE INHERITANCE
# ============================================================

class Father:

    def father_quality(self):
        print("Father's quality")


class Mother:

    def mother_quality(self):
        print("Mother's quality")


class ChildMultiple(Father, Mother):

    def child_quality(self):
        print("Child's quality")


child_multiple = ChildMultiple()

print("\n--- 8. Multiple Inheritance ---")
child_multiple.father_quality()
child_multiple.mother_quality()
child_multiple.child_quality()


# ============================================================
# 9. POLYMORPHISM - METHOD OVERRIDING
# ============================================================

class AnimalSound:

    def sound(self):
        print("Animal makes a sound")


class DogSound(AnimalSound):

    def sound(self):
        print("Dog barks")


class CatSound(AnimalSound):

    def sound(self):
        print("Cat meows")


dog = DogSound()
cat = CatSound()

print("\n--- 9. Polymorphism ---")
dog.sound()
cat.sound()


# ============================================================
# 10. POLYMORPHISM - DUCK TYPING
# ============================================================

class DogDuck:

    def speak(self):
        print("Woof")


class CatDuck:

    def speak(self):
        print("Meow")


def make_sound(animal):
    animal.speak()


dog = DogDuck()
cat = CatDuck()

print("\n--- 10. Duck Typing ---")
make_sound(dog)
make_sound(cat)


# ============================================================
# 11. ABSTRACTION
# ============================================================

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UpiPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


credit_card = CreditCardPayment()
upi = UpiPayment()

print("\n--- 11. Abstraction ---")
credit_card.pay(1000)
upi.pay(500)

# This will produce an error because Payment is abstract:
# payment = Payment()


# ============================================================
# 12. super()
# ============================================================

class ParentClass:

    def __init__(self):
        print("Parent constructor")


class ChildClass(ParentClass):

    def __init__(self):
        super().__init__()
        print("Child constructor")


print("\n--- 12. super() ---")
child = ChildClass()


# Practical super() example

class EmployeeBase:

    def __init__(self, name):
        self.name = name


class Developer(EmployeeBase):

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


developer = Developer("Haripriya", "Python")

print(developer.name)
print(developer.language)


# ============================================================
# 13. CLASS METHOD
# ============================================================

class Company:

    company_name = "CloudStory"

    def __init__(self, employee):
        self.employee = employee

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company


company_employee = Company("Haripriya")

print("\n--- 13. Class Method ---")

print("Before:", Company.company_name)

Company.change_company("Google")

print("After:", Company.company_name)


# ============================================================
# 14. STATIC METHOD
# ============================================================

class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print("\n--- 14. Static Method ---")

print(MathOperations.add(10, 20))
print(MathOperations.multiply(10, 20))


# ============================================================
# 15. INSTANCE METHOD VS CLASS METHOD VS STATIC METHOD
# ============================================================

class MethodTypes:

    company = "CloudStory"

    def __init__(self, name):
        self.name = name

    # Instance method
    def display_name(self):
        print("Employee:", self.name)

    # Class method
    @classmethod
    def display_company(cls):
        print("Company:", cls.company)

    # Static method
    @staticmethod
    def add(a, b):
        return a + b


employee = MethodTypes("Haripriya")

print("\n--- 15. Method Types ---")

employee.display_name()
MethodTypes.display_company()
print(MethodTypes.add(5, 10))


# ============================================================
# 16. MAGIC / DUNDER METHODS
# ============================================================

class StudentDunder:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __len__(self):
        return len(self.name)


student = StudentDunder("Haripriya", 24)

print("\n--- 16. Magic / Dunder Methods ---")

print(student)
print("Length of name:", len(student))


# ============================================================
# 17. __add__() MAGIC METHOD
# ============================================================

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print("\n--- 17. __add__() ---")
print(num1 + num2)


# ============================================================
# 18. COMPOSITION
# ============================================================

class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")


car = Car()

print("\n--- 18. Composition ---")
car.start_car()


# ============================================================
# 19. IS-A VS HAS-A RELATIONSHIP
# ============================================================

# Inheritance:
# Dog IS-A Animal
#
# Composition:
# Car HAS-A Engine


class AnimalRelation:

    def eat(self):
        print("Animal eats")


class DogRelation(AnimalRelation):
    pass


class EngineRelation:

    def start(self):
        print("Engine starts")


class CarRelation:

    def __init__(self):
        self.engine = EngineRelation()


print("\n--- 19. IS-A vs HAS-A ---")

dog_relation = DogRelation()
dog_relation.eat()

car_relation = CarRelation()
car_relation.engine.start()


# ============================================================
# 20. COMPLETE REAL-WORLD OOP EXAMPLE
# ============================================================

class EmployeeRealWorld(ABC):

    company = "CloudStory"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def work(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.__salary}")
        print(f"Company: {self.company}")


class DeveloperRealWorld(EmployeeRealWorld):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        print(
            f"{self.name} is developing software "
            f"using {self.programming_language}"
        )


class TesterRealWorld(EmployeeRealWorld):

    def work(self):
        print(f"{self.name} is testing the application")


developer = DeveloperRealWorld(
    "Haripriya",
    25000,
    "Python"
)

tester = TesterRealWorld(
    "Rahul",
    30000
)

print("\n--- 20. Complete Real-World Example ---")

developer.display_info()
developer.work()

print()

tester.display_info()
tester.work()


# ============================================================
# END
# ============================================================

print("\n===================================")
print("OOP PRACTICE COMPLETED")
print("===================================")
```
