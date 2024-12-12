
class ZeroCouponBonds:

    def __init__(self, principal, maturity, mar_int_rate):
        self.principal = principal
        self.maturity = maturity
        self.mar_int_rate = mar_int_rate

    def present_value(self, x, n):
        return x / ((1+self.mar_int_rate)** n)

    def calculate_price(self):
        return self.present_value(self.principal, self.maturity)

if __name__ == '__main__':

    ZCB = ZeroCouponBonds(1000, 2, 0.04)
    print(ZCB.calculate_price())
