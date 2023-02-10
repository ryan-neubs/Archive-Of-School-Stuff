# test_integration.py

import unittest


from paystation.domain import (PayStation,
                               linear_rate_strategy,
                               progressive_rate_strategy
                               )


class TestAlphaTownIntegration(unittest.TestCase):

    def test_paystation_linear_rate(self):
        ps = PayStation(linear_rate_strategy)
        ps.add_payment(25)
        self.assertEqual(25//5*2, ps.read_display())


class TestBetaTownIntegration(unittest.TestCase):

    def _insert_coins(self, ps, coins):
        for coin in coins:
            ps.add_payment(coin)

    def test_paystation_progressive_rate(self):
        ps = PayStation(progressive_rate_strategy)
        self._insert_coins(ps, [25, 25, 25, 25, 25, 25])
        self.assertEqual(150//5*2, ps.read_display())
        self._insert_coins(ps, [25, 25, 25, 25, 25, 25, 25, 25])
        self.assertEqual(150//5*2+200//5*1.5, ps.read_display())
        self._insert_coins(ps, [25])
        self.assertEqual(150//5*2 + 200//5*1.5 + 25//5, ps.read_display())

class TestTripoliTownIntegration(unittest.TestCase):

    def test_paystation_linear_rate(self):
        ps = PayStation(linear_rate_strategy(200))
        ps.add_payment(25)
        self.assertEqual(ps.read_display(), (150//5*2)+(200//5*1.5)+(300//5))
        
