def calculate_year_of_centenary(current_year, current_age):
    if current_age == 0:
        return current_year + 100
    else:
        birth_year = current_year - current_age
        return birth_year + 100 - 1
