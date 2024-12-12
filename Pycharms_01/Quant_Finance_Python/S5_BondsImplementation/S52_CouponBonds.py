
class CouponBond:

    def __init__(self, principal, rate, maturity, mar_intrest_rate):
        self.principal = principal
        self.rate = rate
        self.maturity = maturity
        self.mar_interest_rate = mar_intrest_rate

    def present_value(self, x, n):
        return x / (1+self.mar_interest_rate)**n

    def calculate_price(self):
        #discount coupon payment one by one
        price = 0
        for t in range(1, self.maturity+1):
            price = price + self.present_value(self.principal * self.rate, t)
            print(price)
        #discount principal amount
        # print(price)
        price = price + self.present_value(self.principal, self.maturity)
        return price


if __name__ == '__main__':

    bond = CouponBond(1000, 0.10, 3, 0.04)
    print(bond.calculate_price())