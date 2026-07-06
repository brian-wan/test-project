def add(a: float, b: float) -> float:
    return a + b


def parse_number(text: str) -> float:
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a valid number")
