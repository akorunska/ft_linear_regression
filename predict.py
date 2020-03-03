import sys
from utils import eprint, estimate_price, read_thetas_from_file

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
    theta0, theta1 = read_thetas_from_file()
    print("using theta0=%i, theta1=%i" % (theta0, theta1))
    print("estimated price is %i" % estimate_price(mileage, theta0, theta1))
