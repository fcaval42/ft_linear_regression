import sys
from global_variables import Global_variables

def load_thetas(path: str) -> tuple[int, int]:
    try:
        with open(path) as f:
            theta0 = float(f.readline()) # ligne 1
            theta1 = float(f.readline()) # ligne 2
        print("\n" + Global_variables.INFO + f" Loading Theta :" + "\n")
        print(f"Theta0 = {theta0}")
        print(f"Theta1 = {theta1}\n")
    except (FileNotFoundError, ValueError):
        print("Theta0 and Theta1 are set to 0 by default. " + "\n" +
              "Start the workout to get a consistent estimate")
        return 0.0, 0.0

    return theta0, theta1


def input_user() -> float:
    while True:
        try:
            mileage = float(input("Enter a mileage: "))
            if mileage < 0:
                raise ValueError("")
            return mileage
        except ValueError:
            print("\n" + Global_variables.ERROR + "The value must be "
                  "a number (positive)")


def estimate_price(theta0, theta1, mileage):
    return theta0 + theta1 * mileage


def predict():

    print("\n" + " \033[33mPREDICTION\033[0m ".center(79, "-") + "\n")

    try:
        mileage = input_user()
        theta0, theta1 = load_thetas("thetas.txt")
        price = estimate_price(theta0, theta1, mileage)

        if price < 0:
            print("\n" + Global_variables.INFO + " Your car is worthless with that many kilometers "
                  f"on it... Sorry bro (result : {price})")
        else:
            print(f"\n{Global_variables.INFO} Estimated price: {price:.2f}")
            print("\n" + "".center(79, "_") + "\n")
    except Exception as e:
        print(f"\n{Global_variables.ERROR}: {e}")
        sys.exit()
