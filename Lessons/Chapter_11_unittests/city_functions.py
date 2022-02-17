#11.1
def get_formatted_city_country(city, country):
    """ returns a neatly formatted 'City,Country'"""
    formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()

#11.2
def get_formatted_city_country_population(city, country, population=''):
    """ returns a neatly formatted 'City,Country'"""
    if population == '':
        formatted_city_info = f"{city}, {country}"
    else:
        formatted_city_info = f"{city}, {country} - population = {population}"

    return formatted_city_info.title()
