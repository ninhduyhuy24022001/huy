def get_formatted_name(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

def city(name_city, name_country):
    city_info = f"{name_city}, {name_country}"
    return city_info.title()
