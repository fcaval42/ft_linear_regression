from utils.global_variables import Global_variables
from predict.predict import estimate_price


def train(km_norm: list[float], price: list[float]) -> tuple[float, float]:
    m: int = len(price)
    theta0: float = 0.0
    theta1: float = 0.0

    for epoch in range(Global_variables.EPOCH):
        sum0: float = 0.0
        sum1: float = 0.0
        for i in range(m):
            erreur: float = estimate_price(theta0, theta1,
                                           km_norm[i]) - price[i]
            sum0 += erreur
            sum1 += erreur * km_norm[i]

        tmp0: float = Global_variables.LEARNING_RATE * (1 / m) * sum0
        tmp1: float = Global_variables.LEARNING_RATE * (1 / m) * sum1

        theta0 -= tmp0
        theta1 -= tmp1

        if epoch % 1000 == 0:
            print(f"epoch {epoch:5d} | average error = {sum0 / m:10.2f}")

    return theta0, theta1
