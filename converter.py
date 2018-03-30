def converter(x, y):
    if x == 2:
        converted = round(y / 60, 2)
        return converted
    if x == 1:
        converted = round(y / 57, 2)
        return converted