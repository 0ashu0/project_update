class Car:

    # constructor in python
    # assigning value to name will make it default but replacable
    def __init__(self, name = "BrandName"):
        self.name = name

    def accelerate(self):
        color = "red"
        print("car {} with color {}".format(self.name, color))

    # @ a decorator, decorators are function that take
    # another functions and extend their functionality
    @staticmethod
    def repair_car():
        print("repairing car")

if __name__ == '__main__':
    ferrari = Car("ferrari") # need to specify the name for constructor
    print(ferrari.name)
    ferrari.accelerate()

    audi = Car("Audi")
    print(audi.name)

    tata = Car()
    print(tata.name)
    tata.accelerate()

    # no need an instance to call staticmethod
    Car.repair_car()