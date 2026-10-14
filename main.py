import sys
from parsing import load_data
from predict import load_thetas, estimate_price
from normalize import normalize, denormalize_thetas
from train import train


def input_user() -> float:
    while True:
        try:
            mileage = float(input("Enter a mileage: "))
            if mileage < 0:
                raise ValueError("")
            return mileage
        except ValueError:
            print("The value must be a number (positive)")


def save_thetas(theta0, theta1, path="thetas.txt"):
    with open(path, "w") as f:
        f.write(f"{theta0}\n{theta1}\n")


def main():
    try:
        km, price = load_data("data.csv")
    except ValueError as e:
        print(f"Erreur : {e}")
        return

    # 1. normaliser les km (les prix restent tels quels)
    km_norm, km_min, km_max = normalize(km)

    # 2. descente de gradient
    theta0, theta1 = train(km_norm, price)

    # 3. revenir a l'echelle reelle
    theta0, theta1 = denormalize_thetas(theta0, theta1, km_min, km_max)

    # 4. sauvegarder pour predict.py
    save_thetas(theta0, theta1)
    print(f"\nEntrainement termine : theta0 = {theta0:.6f}, theta1 = {theta1:.8f}")
    print(f"Parametres sauvegardes dans 'thetas.txt'")


if __name__ == "__main__":
    main()

#if __name__ == "__main__":
#    try:
#        km, price = load_data("data.csv")
#        print(f"[INFO] KM : {km}")
#        print(f"[INFO] PRICE : {price}")
#        print()
#        mileage = input_user()
#        print(f"Mileage : {mileage}")
#        print()
#        theta0, theta1 = load_thetas("thetas.txt")
#        print(f"[INFO] 0 : {theta0}")
#        print(f"[INFO] 1 : {theta1}")
#        print()
#        price = estimate_price(theta0, theta1, mileage)
#        print(f"[INFO] Price : {price}")
#        print()
#    except Exception as e:
#        print(f"[ERROR]: {e}")
#        sys.exit()
