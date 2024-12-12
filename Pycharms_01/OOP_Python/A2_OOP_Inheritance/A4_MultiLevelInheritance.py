# class Employee:
#     print("Employee")
#     pass
#
# class Programmer:
#     print("Programmer")
#     pass
#
# class JuniorProgrammer(Employee, Programmer):
#     print("JuniorProgrammer")
#     pass


class Employee:
    company_name = "Mark Inc"

    def mark_attendance(self):
        print("Marked attendance for {}".format(self.company_name))


class Programmer(Employee):
    def __init__(self, bonus_percentage):
        self.bonus_percentage = bonus_percentage

    def calculate_bonuses(self):
        print("Bonus calculation:{}, company name: {}".format(self.bonus_percentage, self.company_name))

class JuniorProgrammer(Programmer):
    def __init__(self, bonus_percentage):
        self.bonus_percentage = bonus_percentage

    def print_JuniorProgrammer(self):
        print("Bonus calculation:{}, company name: {}".format(self.bonus_percentage, self.company_name))


if __name__ == '__main__':
    john_programmer = JuniorProgrammer(10)
    # print(dir(john_programmer))
    john_programmer.calculate_bonuses()
    john_programmer.mark_attendance()