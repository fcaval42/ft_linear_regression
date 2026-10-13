def load_thetas(path: str) -> tuple[int, int]:
    try:
        with open(path) as f:
            theta0 = float(f.readline()) # ligne 1
            theta1 = float(f.readline()) # ligne 2
    except (FileNotFoundError, ValueError):
        return 0.0, 0.0

    return theta0, theta1


def estimate_price(theta0, theta1, mileage):
    return theta0 + theta1 * mileage

