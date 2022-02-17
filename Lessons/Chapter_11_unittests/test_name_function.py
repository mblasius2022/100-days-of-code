import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py' """

    def test_first_last_name(self):
        """ Do names like Mario Blasius work """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ Do names like Robert E Lee """
        formatted_name = get_formatted_name('robert', 'lee', 'e')
        self.assertEqual(formatted_name, 'Robert E Lee')

if __name__ == '__main__':
    unittest.main()