def is_valid(pin_code):
    is_valid_pin_code = len(pin_code) in [4, 5, 6] and pin_code.isdigit()

    return is_valid_pin_code

max_num = 0
min_num = 9

print(f"""Максимальная цифра равна: {max_num}
Минимальная цифра равна: {min_num}""")
