#!/usr/bin/python3
"""
this is a function that solves the prime game solution
"""


def isWinner(x, nums):
    """
    method definition to figure out the prime numbers
    plus selecting the prime numbers that exist from one to max_n
    """
    def sieve_with_prime_count(max_n):
        """
        method definition for sieve of eratosthenes method
        for counting prime numbers
        """
        if max_n < 2:
            return [0] * (max_n + 1)

        is_prime = [True] * (max_n + 1)
        prime_count = [0] * (max_n + 1)
        is_prime[0], is_prime[1] = False, False
        count = 0

        for xx in range(2, max_n + 1):
            if is_prime[xx]:
                count += 1
                for yy in range(xx * xx, max_n + 1, xx):
                    is_prime[yy] = False
            prime_count[xx] = count

        return prime_count

    if x == 0 or not nums or all(n <= 1 for n in nums):
        return None

    max_n = max(nums) if nums else 0
    prime_count = sieve_with_prime_count(max_n)

    maria_wins = 0
    ben_wins = 0

    for i in nums:
        if i <= 1:
            ben_wins += 1
        elif prime_count[i] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
