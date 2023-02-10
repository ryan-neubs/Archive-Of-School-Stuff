# test_date.py

import unittest
from date import Date

class TestDate(unittest.TestCase):

    def test_25december2010_is_saturday(self):
        date = Date(2010, 12, 25)
        self.assertEqual(date.day_of_week(), Date.Weekday.SATURDAY)

    def test_27september2022_is_tuesday(self):
        date = Date(2022, 9, 27)
        self.assertEqual(date.day_of_week(), Date.Weekday.TUESDAY)

if __name__ == '__main__':
    unittest.main()