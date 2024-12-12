
class Car:
    """This is a test car"""

    name = "Tesla" # attribute

    # variables or class attributes
    # class methods or functions

    def accelerate(self):
        color = "red"
        print("Accelerating car {} having color {}".format(self.name, color))

    # this function doesnt work
    def applybrakes(self):
        print("brake car {} having color {}".format(self.name, color))

if __name__ == '__main__':
    # print(Car.__doc__)
    # help(Car)
    ferrari = Car()
    # overriding class attribute
    ferrari.name = "ferrari"
    # print(ferrari.name)
    ferrari.accelerate()
    ferrari.applybrakes()



