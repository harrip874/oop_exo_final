
# PART 1 OPERATOR OVERLOADING


# PROBLEM 1

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, second):
        addition = Complex(
            self.real + second.real,
            self.imaginary + second.imaginary
        )
        return addition

    def __sub__(self, second):
        subtraction = Complex(
            self.real - second.real,
            self.imaginary - second.imaginary
        )
        return subtraction

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# PROBLEM 2

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, second):
        return self.age > second.age


# PROBLEM 4

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, second):
        return (
            self.x * second.x +
            self.y * second.y +
            self.z * second.z
        )


# PROBLEM 5

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, second):
        return self.radius < second.radius

    def __gt__(self, second):
        return self.radius > second.radius

    def __eq__(self, second):
        return self.radius == second.radius

    def __ne__(self, second):
        return self.radius != second.radius

    def __ge__(self, second):
        return self.radius >= second.radius

    def __le__(self, second):
        return self.radius <= second.radius


# PROBLEM 6

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, second):
        return self.distance() < second.distance()

    def __gt__(self, second):
        return self.distance() > second.distance()

    def __eq__(self, second):
        return self.distance() == second.distance()

    def __ne__(self, second):
        return self.distance() != second.distance()

    def __ge__(self, second):
        return self.distance() >= second.distance()

    def __le__(self, second):
        return self.distance() <= second.distance()


# PROBLEM 7

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __mul__(self, second):
        rows1 = len(self.matrix)
        cols1 = len(self.matrix[0])
        rows2 = len(second.matrix)
        cols2 = len(second.matrix[0])

        if cols1 != rows2:
            raise ValueError("Matrix dimensions are incompatible")

        result = []

        for i in range(rows1):
            row = []
            for j in range(cols2):
                total = 0
                for k in range(cols1):
                    total += self.matrix[i][k] * second.matrix[k][j]
                row.append(total)
            result.append(row)

        return Matrix(result)


# PART 2 INHERITANCE


# PROBLEM 1

class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


# PROBLEM 2

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)
        self.field_of_study = field_of_study

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old and I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old and I work at {self.company}."


# PROBLEM 3

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True

    def transfer(self, destination, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        destination.balance += amount
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

    def check_balance(self):
        return self.balance
