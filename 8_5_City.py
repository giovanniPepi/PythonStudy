def describe_city(city_name, country = 'Brazil'): 

    """Describes the city name and country it is located."""
    print(f"{city_name.title()} is located in {country.title()}.")

describe_city(city_name = 'Itu')
describe_city('itu')
describe_city('sumaré')
describe_city('campinas')
describe_city('nice', country='France')
