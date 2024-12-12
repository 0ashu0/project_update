
class Car:
    name = "Tesla" # attribute

    # variables or class attributes
    # class methods or functions

    # initializing attributes by using methods
    def set_car_name(self,name):
        self.name = name

    def accelerate(self):
        color = "red"
        print("Accelerating car {} having color {}".format(self.name, color))


if __name__ == '__main__':
    ferrari = Car()
    # this will print class declaration
    print(ferrari.name)

    # initializing attributes by using methods
    ferrari.set_car_name("ferrari by methods")
    print(ferrari.name)

    # initialization from main function
    ferrari.name = "Ferrari from Main"

    ferrari.accelerate()


    audi = Car()
    print(audi.name)



