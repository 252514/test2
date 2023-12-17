def check_price(price_str: str) -> bool:
    float(price_str.replace(",", "."))
    if "." in price_str:
        decimal_places = len(price_str.split(".")[1])
        if decimal_places > 2:
            raise ValueError("must have two digits")
    return True


def convert_price_string_int100(price: str) -> int:
    return int(float(price) * 100)


def convert_price_int100_string(price: int) -> str:
    return f"{price/100}"
