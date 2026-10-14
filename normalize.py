# on ramène les kilométrages dans [0, 1] pour éviter la divergence
def normalize(km: int) -> tuple[int, int, int]:
    km_min, km_max = min(km), max(km)
    km_norm = [(k - km_min) / (km_max - km_min) for k in km]
    return km_norm, km_min, km_max


# reconvertit les thetas dans l'échelle réelle des kilométrages
def denormalize_thetas(theta0, theta1, km_min, km_max):
    theta1_real = theta1 / (km_max - km_min)
    theta0_real = theta0 - theta1_real * km_min
    return theta0_real, theta1_real
