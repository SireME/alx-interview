#!/usr/bin/python3
"""
Module to determine winner of game based on primes
"""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes(n):
    """Generate a list of prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def isWinner(x, nums):
    """Determine the winner of each round."""
    winners = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        primes = generate_primes(nums[i])
        if len(primes) % 2 == 0:
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1
    if winners['Maria'] > winners['Ben']:
        return 'Maria'
    elif winners['Maria'] < winners['Ben']:
        return 'Ben'
    else:
        return None
