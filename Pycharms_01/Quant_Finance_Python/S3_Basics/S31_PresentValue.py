from math import exp

def future_discrete_value(x , r, n):
    return x*(1+r)**n

def present_discrete_value(x , r, n):
    # 1/x**2 = x**-2
    return x*(1+r)**-n


def future_continuous_value(x , r, t):
    return x*exp(r*t)

def present_continuous_value(x , r, t):
    return x*exp(-r*t)

if __name__ == '__main__':
    # value of investment in dollars
    x = 100
    # interest rate
    r = 0.05
    # duration 5 years
    n = 5


    print("future discrete"    ,future_discrete_value(x, r, n))
    print("present discrete"    ,present_discrete_value(x, r, n))
    print("future continuous"   ,future_continuous_value(x, r, n))
    print("present continuous"  ,present_continuous_value(x, r, n))