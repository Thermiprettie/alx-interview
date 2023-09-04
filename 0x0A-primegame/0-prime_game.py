#!/usr/bin/python3

""" Prime game """


def is_prime(n):
    """ Checks if a given number n is a prime number """
    for t in range(2, int(n ** 0.5) + 1):
        if not n % t:
            return False
    return True


def calculate_primes(n, primes):
    """ Calculate all primes """
    primeNos = primes[-1]
    if n > primeNos:
        for t in range(primeNos + 1, n + 1):
            if is_prime(t):
                primes.append(t)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
	x is the number of rounds and nums is an array of n
	Return: name of the player that won the most rounds    
    """

    winplay = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    calculate_primes(max(nums), primes)

    for st8 in range(x):
        to_sum = sum((t != 0 and t <= nums[st8])
                          for t in primes[:nums[st8] + 1])

        if (to_sum % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            winplay[winner] += 1

    if winplay["Maria"] > winplay["Ben"]:
        return "Maria"
    elif winplay["Ben"] > winplay["Maria"]:
        return "Ben"

    return None
