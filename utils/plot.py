import matplotlib.pyplot as plt


def plot_data_with_regression(
    km: list[float],
    price: list[float],
    theta0: float,
    theta1: float,
    km_min: float,
    km_max: float
) -> None:
    plt.figure(figsize=(10, 6))
    plt.scatter(km, price, color='blue', label='Data points')

    regression_km: list[float] = [km_min, km_max]
    regression_price: list[float] = [theta0 + theta1 * km_min,
                                     theta0 + theta1 * km_max]

    plt.plot(regression_km, regression_price, color='red',
             label='Regression line')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Car Price vs Mileage - Linear Regression')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
