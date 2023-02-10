# This program tests the Date class of date_obj.py
# By Ryan Neubauer with help from Gavin Roy

import unittest
from date_obj import Date

class TestDate(unittest.TestCase):

        def setUp(self):
            self.date1 = Date('09/25/2001')
            self.date2 = Date('10/25/2000')
            self.date3 = Date('09/25/2020')
            self.date4 = Date('09/25/1900')
            self.date5 = Date('02/29/2000')

        def test_validation(self):
            self.assertEqual(self.date1._is_valid_date(), True)
            self.assertEqual(self.date2._is_valid_date(), True)
            self.assertEqual(self.date3._is_valid_date(), True)
            self.assertEqual(self.date4._is_valid_date(), True)
            self.assertEqual(self.date5._is_valid_date(), True)

        def test__str__(self):
            self.assertEqual(self.date1.__str__(), '9/25/2001')
            self.assertEqual(self.date5.__str__(), '2/29/2000')

        def test_day_num(self):
            self.assertEqual(self.date1.day_number(), 268)
            self.assertEqual(self.date2.day_number(), 299)

        def test__sub__(self):
            self.assertEqual(self.date1.__sub__(Date('9/29/2001')), 4)
            self.assertEqual(self.date2.__sub__(Date('12/27/2001')), 428)
            self.assertEqual(self.date3.__sub__(Date('11/24/2021')), 425)
            self.assertEqual(self.date4.__sub__(Date('8/15/1920')), 7264)


if __name__ == "__main__":
    unittest.main()
            
            
