class Employee:
    company_name = "Mark Inc"

    def mark_attendance(self):
        print("Marked attendance for {}".format(self.company_name))

class Administrator:
    admin_name = "test admin"

    def print_admin(self):
        print(self.admin_name)



class Programmer(Employee, Administrator):
    def __init__(self, bonus_percentage):
        self.bonus_percentage = bonus_percentage

    def calculate_bonuses(self):
        print("Bonus calculation:{}, company name: {}".format(self.bonus_percentage, self.company_name))
        print(self.admin_name)


if __name__ == '__main__':
    john_programmer = Programmer(10)
    # print(vars(john_programmer))
    # print(dir(john_programmer))
    john_programmer.calculate_bonuses()
    john_programmer.mark_attendance()
    john_programmer.print_admin()
  