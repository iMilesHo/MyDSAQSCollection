1. Purpose:

- fundamental building block of object-oriented programming
- encapsulate data and functions into a single entity which can be used to create objects(Instances) with attributes and methods
- enable code reusability and organization, making it easier to manage and maintain complex programs

2. Basic Syntax:

```python
class ClassName:
    def __init__(self, arg1, arg2, ...):
        self.arg1 = arg1
        self.arg2 = arg2
        ...

    def method1(self, arg1, arg2, ...):
        ...

    def method2(self, arg1, arg2, ...):
        ...
```

3. Instance vs Class Attributes:

- Instance attributes: unique to each instance of a class, defined within the `__init__` method
- Class attributes: shared by all instances of a class, defined outside the `__init__` method

```python
class ClassName:
    class_attr = value

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

obj1 = ClassName('value1')
obj2 = ClassName('value2')

print(obj1.instance_attr)  # value1
print(obj2.instance_attr)  # value2
print(obj1.class_attr)     # value
print(obj2.class_attr)     # value

ClassName.class_attr = 'new_value'
```

4. Inheritance:

- allows a class to inherit attributes and methods from another class
- Supports code reuse and implementation of polymorphism.

```python
class ParentClass:
    def method1(self):
        ...

class ChildClass(ParentClass):
    def method2(self):
        ...
```

5. Polymorphism:

- the ability of different classes to be treated as instances of the same class
- often achieved through method overriding, where a method in a subclass has the same name as a method in its superclass

```python
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Using the classes
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())
```

6. Encapsulation:

- the bundling of data and methods that operate on that data within a single unit
- Typically involves using private (prefixed with `_` or `__`) attributes and methods to restrict access from outside the class

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to the balance")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

# Using the class
account = BankAccount("John Doe")
account.deposit(100)
print(account.get_balance())  # Correct way to access the balance
account.withdraw(50)
print(account.get_balance())

# The following will raise an error because __balance is private
# print(account.__balance)
```

7. Method Types:

- Instance methods, use `self` as the first parameter and operate on instance attributes
- Class methods, use `cls` as the first parameter, decorated with `@classmethod`, and operate on class attributes
- Static methods, decorated with `@staticmethod`, do not take `self` or `cls` as parameters, and are independent of the class

```python
class MathOperations:
    pi = 3.14159  # A class variable

    def __init__(self, radius):
        self.radius = radius  # An instance variable

    # Instance method
    def area_of_circle(self):
        return self.pi * (self.radius ** 2)

    # Class method
    @classmethod
    def update_pi(cls, new_value):
        cls.pi = new_value

    # Static method
    @staticmethod
    def add_numbers(x, y):
        return x + y

# Using the class
circle = MathOperations(5)
print(circle.area_of_circle())  # Instance method, uses instance attributes

MathOperations.update_pi(3.14)  # Class method, alters class variable
print(circle.area_of_circle())  # Now uses the updated class variable

print(MathOperations.add_numbers(3, 4))  # Static method, independent of class instance
```
