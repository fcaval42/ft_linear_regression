# on ramène les kilométrages dans [0, 1] pour éviter la divergence
def normalize(km: list[float]) -> tuple[list[float], float, float]:
    km_min: float = min(km)
    km_max: float = max(km)
    km_norm: list[float] = [(k - km_min) / (km_max - km_min) for k in km]
    return km_norm, km_min, km_max


def denormalize_thetas(
    theta0: float, theta1: float, km_min: float, km_max: float
) -> tuple[float, float]:
    theta1_real: float = theta1 / (km_max - km_min)
    theta0_real: float = theta0 - theta1_real * km_min
    return theta0_real, theta1_real
