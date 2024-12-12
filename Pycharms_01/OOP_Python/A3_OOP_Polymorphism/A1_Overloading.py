# Overloading - operators
# Overriding - methods

# Operator Overloading
# one operator exhibiting multiple forms


class Employee:
    def __init__(self, salary):
        self.salary = salary

    # for overloading operator
    def __add__(self, other):
        return self.salary+other.salary


if __name__ == '__main__':
    emp1 = Employee(1000)
    emp2 = Employee(2000)
    print(emp1+emp2)

