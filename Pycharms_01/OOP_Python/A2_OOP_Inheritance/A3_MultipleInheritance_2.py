class SavingAccount:

    def __init__(self):
        self.savings = 0
        self.credit = 0

    def add_balance(self, addvalue):
        self.savings = self.savings + addvalue
        print(self.savings)

    def takeOutMoney(self, outmoney):
        self.savings = self.savings - outmoney
        print(self.savings)

class FDAccount:

    def __init__(self):
        self.FD = 0

    def add_FD(self, fdamount):
        self.FD = self.FD + fdamount
        print(self.FD)

class SeniorAccount(SavingAccount, FDAccount):

    # need to explicitly call init for all parent class
    def __init__(self):
        SavingAccount.__init__(self)
        FDAccount.__init__(self)

    def Interest(self, interest):
        print(self.savings)
        self.savings = self.savings * interest
        print(self.savings)

if __name__ == '__main__':
    s = SeniorAccount()
    # print(dir(s))
    # print(vars(s))
    s.add_balance(10)
    s.add_balance(20)
    s.takeOutMoney(20)
    s.Interest(1.1)

