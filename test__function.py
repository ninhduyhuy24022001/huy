import unittest
from name_function import get_formatted_name, city

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadues')
        self.assertEqual(formatted_name, 'Wolfgang Amadues Mozart')

class CityInfoTest(unittest.TestCase):
    def test_city_country(self):
        city_info = city('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()