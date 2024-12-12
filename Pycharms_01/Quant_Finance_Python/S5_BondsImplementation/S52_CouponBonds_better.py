
class CouponBond:

    def __init__(self, principal, rate, maturity, mar_interest_rate):
        self.principal = principal
        self.rate = rate
        self.maturity = maturity
        self.mar_interest_rate = mar_interest_rate


    def coupon_value(self, principal, rate, maturity, mar_interest_rate):
        total_coupon = 0
        current_coupon = 0
        while maturity >=1:
            current_coupon = (principal* rate) / (1 + mar_interest_rate) ** maturity
            maturity -= 1
            total_coupon = total_coupon + current_coupon
        return total_coupon

    def principal_value(self, principal, rate, maturity, mar_interest_rate):
        return principal / (1+mar_interest_rate)**maturity


if __name__ == '__main__':

    CB = CouponBond(1000, 0.10, 3, 0.04)
    couponValue = CB.coupon_value(1000, 0.10, 3, 0.04)
    principalValue = CB.principal_value(1000, 0.10, 3, 0.04)
    print("couponValue", couponValue)
    print("principalValue", principalValue)
    total_present_value = couponValue + principalValue
    print(total_present_value)