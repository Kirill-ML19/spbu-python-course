from typing import Generator, Tuple, List


def prine_generator() -> Generator[int, None, None]:
    """
    Prime number sequence generator function.

    Yields:
        int: The next prime number in the sequence.
    """
    primes: List[int] = []
    num = 2
    while True:
        if all(num % p != 0 for p in primes):
            primes.append(num)
            yield num
        num += 1


def prime_decorator(generator_func):
    """
    Decorator that takes a generator and returns a function that returns the k-th prime number (starting from 1).

    Args:
        generator_func (Callable): A prime number generator function.

    Returns:
        Callable[[int], int]: A function that takes an element index and returns a prime number.
    """
    primes_cache = []

    def wrapper(k: int) -> int:
        nonlocal primes_cache
        if k < 1:
            raise ValueError("Index must be greater than or equal to 1")
        while len(primes_cache) < k:
            primes_cache.append(next(generator_func()))
        return primes_cache[k - 1]

    return wrapper


@prime_decorator
def get_prime():
    """
    A generator-wrapped function that returns the k-th prime number.

    Returns:
        int: The prime number at the given index.
    """
    return prime_decorator()
