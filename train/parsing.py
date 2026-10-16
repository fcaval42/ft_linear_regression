import csv


def load_data(file_name: str) -> tuple[list[float], list[float]]:
    try:
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)  # Lit la première ligne (en-têtes)
            if header != ["km", "price"]:
                raise ValueError(f"Invalid header: {header}. Expected: "
                                 "['km', 'price']")

            km, price = [], []
            for i, row in enumerate(reader, start=2):
                if len(row) != 2:
                    raise ValueError(f"Line {i} has {len(row)} columns, "
                                     f"expected 2: {row}")

                try:
                    k = float(row[0])
                    p = float(row[1])
                except (TypeError, ValueError):
                    raise ValueError(f"Line {i} invalid: {row}")

                if k < 0 or p < 0:
                    raise ValueError(f"Values cannot be negative at "
                                     f"line {i}: {row}")

                km.append(k)
                price.append(p)

            if len(km) < 2:
                raise ValueError("Need at least 2 data points for "
                                 "regression.")
            return km, price

    except FileNotFoundError:
        raise ValueError(f"File not found: {file_name}")
