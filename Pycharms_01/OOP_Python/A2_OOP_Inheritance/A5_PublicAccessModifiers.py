# Access Modifiers
# Public: class member defined as public can be accessed from anywhee
# Protected: can be accessed in same class or child class
# Private: same class only

from A1_OOP_BASICS.Car3 import Car

if __name__ == '__main__':
    car = Car("Tesla")
    print(car.name)
    car.name = "Ferrari"
    print(car.name)



from A2_OOP_Inheritance.A1_SingleInheritance import Employee

if __name__ == '__main__':
