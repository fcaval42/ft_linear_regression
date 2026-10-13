import sys
from parsing import load_data
from predict import load_thetas, estimate_price


def input_user() -> float:
    while True:
        try:
            mileage = float(input("Enter a mileage: "))
            if mileage < 0:
                raise ValueError("")
            return mileage
        except ValueError:
            print("The value must be a number (positive)")


if __name__ == "__main__":
    try:
        km, price = load_data("data.csv")
        print(f"[INFO] KM : {km}")
        print(f"[INFO] PRICE : {price}")
        print()
        mileage = input_user()
        print(f"Mileage : {mileage}")
        print()
        theta0, theta1 = load_thetas("thetas.txt")
        print(f"[INFO] 0 : {theta0}")
        print(f"[INFO] 1 : {theta1}")
        print()
        price = estimate_price(theta0, theta1, mileage)
        print(f"[INFO] Price : {price}")
        print()
    except Exception as e:
        print(f"[ERROR]: {e}")
        sys.exit()
