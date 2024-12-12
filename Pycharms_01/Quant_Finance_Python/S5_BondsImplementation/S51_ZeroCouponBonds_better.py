
# this is a better example, as I am also having class instance with optional parameters,
# but I also have methods with local parameters. so i can use the method frequently for
# simulation etc,


class ZeroCouponBonds:

    def __init__(self, principal=None, maturity=None, mar_int_rate=None):
        self.principal = principal
        self.maturity = maturity
        self.mar_int_rate = mar_int_rate

    def present_value(self, principal, maturity, mar_int_rate):
        return principal / (1+mar_int_rate)**maturity


if __name__ == '__main__':

    ZCB = ZeroCouponBonds()
    print(ZCB.present_value(1000, 2, 0.04))

