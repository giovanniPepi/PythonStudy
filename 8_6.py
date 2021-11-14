def get_city (c_name, c_country):
    """Returns a netaly formatted city name and country"""
    city_info = f"{c_name.title()}, {c_country.title()}"
    return(city_info)

city_info = get_city('santiago', 'chile')
print(city_info)

city_info = get_city('campinas', 'brasil')
print(city_info)

city_info = get_city('sumaré', 'brasil')
print(city_info)
