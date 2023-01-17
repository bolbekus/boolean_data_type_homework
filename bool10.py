from math import sqrt


def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    a0 = int(sqrt(a))
    return a0 ** 2 == a

print(main(15))