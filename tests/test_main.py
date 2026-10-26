import unittest
from main import check_name, division

class NameTest(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(check_name('Никита'),True,'Неправильное имя')


    def test_incorrect(self):
        self.assertEqual(check_name('Иван2'),False, 'Правильное имя ')


class NumberTest(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(division(2,2), 1)


    def test_value_error(self):
        pass


if __name__ == '__main__':
    unittest.main()
