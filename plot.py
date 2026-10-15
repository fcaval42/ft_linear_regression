import matplotlib.pyplot as plt


def plot_data_with_regression(km, price, theta0, theta1, km_min, km_max):

    plt.figure(figsize=(10, 6))

    # point isolés (en nuages)
    plt.scatter(km, price, color='blue', label='Data points')

    # Calculer les points pour la ligne de régression
    regression_km = [km_min, km_max]
    regression_price = [theta0 + theta1 * km_min, theta0 + theta1 * km_max]

    # ligne de régression
    plt.plot(regression_km, regression_price, color='red',
             label='Regression line')

    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Car Price vs Mileage - Linear Regression')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
