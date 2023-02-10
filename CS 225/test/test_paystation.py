# test_paystation.py

import unittest

from paystation.domain import (PayStation,
                               IllegalCoinException,
                               Receipt,
                               )


def one_to_one_rate_strategy(amount):
    return amount


class TestPayStation(unittest.TestCase):

    def setUp(self):
        self.ps = PayStation(one_to_one_rate_strategy)

    def _insert_coins(self, coins):
        for coin in coins:
            self.ps.add_payment(coin)

    def test_displays_proper_time_for_5_cents(self):
        self.ps.add_payment(5)
        self.assertEqual(5, self.ps.read_display())

    def test_displays_time_for_25_cents(self):
        self.ps.add_payment(25)
        self.assertEqual(25, self.ps.read_display())

    def test_displays_time_for_5_and_25_cents(self):
        self._insert_coins([5, 25])
        self.assertEqual(5+ 25, self.ps.read_display())   

    def test_reject_illegal_coin(self):
        with self.assertRaises(IllegalCoinException):
            self.ps.add_payment(17)

    def test_buy_gives_valid_receipt(self):
        self._insert_coins([5, 10, 25])
        receipt = self.ps.buy()
        self.assertIsInstance(receipt, Receipt)
        self.assertEqual(5+10+25, receipt.value)

    def test_receipt_stores_value(self):
        receipt = Receipt(30)
        self.assertEqual(30, receipt.value) 

    def test_correct_receipt_for_100_cents(self):
        self._insert_coins([25, 25, 25, 10, 10, 5])
        rec = self.ps.buy()
        self.assertEqual(25*3+10*2+5, rec.value)

    def test_clears_after_buy(self):
        self.ps.add_payment(25)
        self.ps.buy()
        self.assertEqual(0, self.ps.read_display())
        self._insert_coins([5, 25])
        self.assertEqual(5+25, self.ps.read_display())

    def test_clears_on_cancel(self):
        self.ps.add_payment(25)
        self.ps.cancel()
        self.assertEqual(0, self.ps.read_display())
        self._insert_coins([5, 25])
        self.assertEqual(5+25, self.ps.read_display())


if __name__ == "__main__":
    unittest.main()
