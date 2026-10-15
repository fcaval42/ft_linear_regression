from utils.global_variables import Global_variables
from train.parsing import load_data
from train.normalize import normalize, denormalize_thetas
from train.train import train
from utils.plot import plot_data_with_regression


def save_thetas(theta0, theta1, path="thetas.txt"):
    with open(path, "w") as f:
        f.write(f"{theta0}\n{theta1}\n")


def training():

    print("\n" + " \033[32mTRAINING\033[0m ".center(79, "-") + "\n")

    try:
        km, price = load_data("data.csv")
    except ValueError as e:
        print("\n" + Global_variables.ERROR + f": {e}")
        return

    # 1. normaliser les km (les prix restent tels quels)
    km_norm, km_min, km_max = normalize(km)

    # 2. descente de gradient
    theta0, theta1 = train(km_norm, price)

    # 3. revenir a l'echelle reelle
    theta0, theta1 = denormalize_thetas(theta0, theta1, km_min, km_max)

    plot_data_with_regression(km, price, theta0, theta1, km_min, km_max)

    # 4. sauvegarder pour predict.py
    save_thetas(theta0, theta1)
    print("\n" + Global_variables.INFO + f" Training Complete : "
          f"theta0 = {theta0:.6f}, theta1 = {theta1:.8f}")
    print("\n" + Global_variables.INFO + f" Backup settings saved in "
          "'thetas.txt'" + "\n")
