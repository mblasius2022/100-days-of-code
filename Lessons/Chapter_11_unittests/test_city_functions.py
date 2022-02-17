import unittest
from city_functions import get_formatted_city_country
from city_functions import get_formatted_city_country_population

class CityTestCase(unittest.TestCase):
    """ tests for 'city_functions.py' """

    def test_city_country(self):
        """ does city and country like vienna austria work """
        formatted_city = get_formatted_city_country('vienna', 'austria')
        self.assertEqual(formatted_city, 'Vienna, Austria')

    def test_city_country_population(self):
        """ does city and country like vienna austria work """
        formatted_city_info = get_formatted_city_country_population(
            'santiago', 'chile')
        self.assertEqual(formatted_city_info, 'Santiago, Chile')

        formatted_city_info = get_formatted_city_country_population(
            'santiago', 'chile', '5000000')
        self.assertEqual(formatted_city_info,
        'Santiago, Chile - Population = 5000000')


if __name__ == '__main__':
    unittest.main()