import csv

def load_data(file_name: str) -> list[str]:
    try:
        with open(file_name, newline='') as f:
        # DictReader = lit fichier CSV et convertit chaque ligne en un dico.
        # Les clés correspondent aux en-têtes (la première ligne du fichier)
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        raise ValueError(f"File not found : {file_name}")

    km, price = [], []
    # start=2 -> première ligne = clés
    for i, row in enumerate(rows, start=2):
        try:
            k = float(row["km"])
            p = float(row["price"])
        except (KeyError, TypeError, ValueError):
            raise ValueError(f"Line value {i} invalid : {row}")

        if k < 0 or p < 0:
            raise ValueError(f"The values cannot be negative: {row}")

        km.append(k)
        price.append(p)

    if len(km) < 2:
        raise ValueError(f"You need at least two kilometer values to perform "
                         "a regression analysis.")

    return km, price


