from global_variables import Global_variables
from predict import estimate_price

# on répète EPOCH fois jusqu'à convergence = descente de gradient
def train(km_norm, price):
    m = len(price)
    theta0, theta1 = 0.0, 0.0

    for epoch in range(Global_variables.EPOCH):
        # erreurs du modèle actuel et remplissage des deux caisses
        sum0 = 0.0
        sum1 = 0.0
        for i in range(m):
            erreur = estimate_price(theta0, theta1, km_norm[i]) - price[i]
            sum0 += erreur
            sum1 += erreur * km_norm[i]

        # corrections moyennes et freinées par le learning rate
        tmp0 = Global_variables.LEARNING_RATE * (1 / m) * sum0
        tmp1 = Global_variables.LEARNING_RATE * (1 / m) * sum1

        # maj simultanée (les tmp utilisent les anciens thetas)
        theta0 -= tmp0
        theta1 -= tmp1

        # debug
        if epoch % 1000 == 0:
            print(f"epoch {epoch:5d} | average error = {sum0 / m:10.2f}")

    return theta0, theta1