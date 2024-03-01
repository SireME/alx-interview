#!/usr/bin/python3
"""
Module for determining the fewest number of
coins needed to meet a given amount total
with a pile of coins of different values.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.

    Args:
    coins (list): A list of coin values available for making change.
    total (int): The amount for which change needs to be made.

    Returns:
    int: The minimum number of coins required to make the
      total. Returns -1 if it's not possible to make the total.
    """
    if total <= 0:
        return 0

    remaining_amount = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)

    # Iterating through coins to make change
    while remaining_amount > 0:
        if coin_idx >= n:
            return -1  # No solution possible

        # Check if current coin value can be used to make change
        if remaining_amount - sorted_coins[coin_idx] >= 0:
            remaining_amount -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count
