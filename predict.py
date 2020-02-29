import sys
from utils import eprint

def estimate_price(mileage, theta0, theta1):
    return float(theta0 + (theta1 * mileage));

def read_thetas():
    return (0.0, 0.0)

def receive_mileage_input():
    try:
        mileage = int(input("Please, enter the car mileage, km: "))
        if (mileage < 0):
            eprint("The value inputted must be greater than 0")
    except(ValueError):
        eprint("The value inputted must be an integer")
    return mileage


if __name__=="__main__":
    mileage = receive_mileage_input()
    theta0, theta1 = read_thetas()
    print("using theta0=%i, theta1=%i" % (theta0, theta1))
    print("estimated price is %i" % estimate_price(mileage, theta0, theta1))
