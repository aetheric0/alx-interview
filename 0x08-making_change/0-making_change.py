#!/usr/bin/python3
""" Determines the fewest number of coins needed
to meet a given amount of total
"""


def makeChange(coins, total):
    """ Calculates the fewest number of coins
    needed to meet a total and returns result
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else - 1
