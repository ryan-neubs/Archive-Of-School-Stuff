# dp_traceback.py
#   A couple examples showing how to implement tracing back to
#   read solutions from dynamic programming algorithms.

import functools
memoize = functools.lru_cache(maxsize=None)

import sys
sys.setrecursionlimit(10000)


class CoinRow:

    def __init__(self, coins):
        self.coins = list(coins)
        self.F = memoize(self.F)

    def F(self, n):
        c = self.coins
        if n == 0:
            return 0
        if n == 1:
            return c[0]
        return max(c[n-1] + self.F(n-2), self.F(n-1))

    def solution(self):
        n = len(self.coins)
        num_coins = self.F(n)
        taken = []
        i = n
        while i > 0:
            if self.F(i) > self.F(i-1):
                taken.append(i)
                i -= 2
            else:
                i -= 1
        taken.reverse()
        return num_coins, taken


class ChangeMaking:

    def __init__(self, denoms):
        self.coinvals = denoms
        self.F = memoize(self.F)

    def F(self, n):
        if n == 0:
            return 0
        else:
            return 1 + min(self.F(n - dj)
                           for dj in self.coinvals if n >= dj)

    def solution(self, amt):
        n = len(self.coinvals)
        mincoins = self.F(amt)
        coins_used = {d: 0 for d in self.coinvals}
        while amt > 0:
            poss_prev_amts = [amt-d for d in self.coinvals if d <= amt]
            prev_amt = min(poss_prev_amts, key=self.F)
            coins_used[amt - prev_amt] += 1
            amt = prev_amt
        return coins_used
