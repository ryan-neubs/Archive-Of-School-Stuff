# test_rate_strategies.py

import unittest

from paystation.domain import linear_rate_strategy, progressive_rate_strategy


class TestLinearRate(unittest.TestCase):

    def test_correct_value_for_150_cents(self):
        lrs = linear_rate_strategy(150)
        self.assertEqual(100 // (150/60), lrs(100))

    def test_correct_value_for_240_rate(self):
        lrs = linear_rate_strategy(240)
        self.assertEqual(100//(240/60), lrs(100))


class TestProgressiveRate(unittest.TestCase):

    def setUp(self):
        self.rate = progressive_rate_strategy

    def test_correct_value_for_150_cents(self):
        self.assertEqual(150//5*2, self.rate(150))

    def test_correct_value_for_100_cents(self):
        self.assertEqual(100//5*2, self.rate(100))

    def test_correct_value_for_350_cents(self):
        self.assertEqual(150//5*2+200//5*1.5, self.rate(350))

    def test_correct_value_for_200_cents(self):
        self.assertEqual((350-200)//5*2+50//5*1.5, self.rate(200))

    def test_correct_value_for_650_cents(self):
        self.assertEqual((150)//5*2 + 200//5*1.5 + 300//5, self.rate(650))

    def test_correct_value_for_400_cents(self):
        self.assertEqual((350-200)//5*2+200//5*1.5 + 50//5, self.rate(400))

    def test_correct_value_for_700_cents(self):
        self.assertEqual((350-200)//5*2+200//5*1.5 + 350//5, self.rate(700))
