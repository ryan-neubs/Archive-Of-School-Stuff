# test_paystation.py

import unittest
from Paystation.domain import PayStation, IllegalCoinException, Receipt

class TestPayStation(unittest.TestCase):

    def setUp(self):
        self.ps = PayStation()

    def _insert_coins(self, coins):
        for coin in coins:
            self.ps.add_payment(coin)

    def test_displays_2_mins_for_5_cents(self):
        self.ps.add_payment(5)
        self.assertEqual(2, self.ps.read_display())

    def test_displays_10_minutes_for_25_cents(self):
        self.ps.add_payment(25)
        self.assertEqual(25 // 5 * 2, self.ps.read_display())

    def test_reject_illegal_coin(self):
        with self.assertRaises(IllegalCoinException):
            self.ps.add_payment(17)

    def test_displays_12_minutes_for_5_and_25_cents(self):
        self._insert_coins([5, 25])
        self.assertEqual((5 + 25) // 5 * 2, self.ps.read_display())

    def test_buy_gives_valid_receipt(self):
        self._insert_coins([5, 10, 25])
        receipt = self.ps.buy()
        self.assertIsInstance(receipt, Receipt)
        self.assertEqual((5+10+25)//5*2, receipt.value)

    def test_receipt_stores_value(self):
        receipt = Receipt(30)
        self.assertEqual(30, receipt.value)

    def test_clears_after_buy(self):
        self.ps.add_payment(25)
        self.ps.buy()
        self.assertEqual(0, self.ps.read_display())
        self._insert_coins([5, 25])
        self.assertEqual((5+25)//5*2, self.ps.read_display())

    def test_clears_on_cancel(self):
        self.ps.add_payment(25)
        self.ps.cancel()
        self.assertEqual(0, self.ps.read_display())
        self._insert_coins([5, 25])
        self.assertEqual((5+25)//5*2, self.ps.read_display())

if __name__ == "__main__":
    unittest.main()
