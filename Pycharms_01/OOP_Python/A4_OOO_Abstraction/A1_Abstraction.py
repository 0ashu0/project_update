# abstraction
# hiding implementation details and highlighting services

# abstract version of all car types

from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):
    @abstractmethod
    def apply_brakes(self):
        pass


class Tesla(Car):
    def apply_brakes(self):
        print("Apply brakes in Tesla")


class Audi(Car):
    def apply_brakes(self):
        print("Apply brakes in Audi")


if __name__ == '__main__':
    tesla = Tesla()
    tesla.apply_brakes()

    audi = Audi()
    audi.apply_brakes()