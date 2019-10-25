def sorta_sum(a: int, b: int) -> int:
    """given 2 positive ints, a and b, return their sum. 
    However, sums in the range 10..19 inclusive, are forbidden, so in that case 
    just return 20.
    
    Arguments:
        a {int} -- positive integer
        b {int} -- positive integer
    
    Returns:
        int -- computed sum
    """
    assert a >= 0 and b >= 0

    total = a + b
    if 10 <= total <= 19:
        return 20
    else:
        return total


# validate function
assert sorta_sum(3, 4) == 7
assert sorta_sum(9, 4) == 20
assert sorta_sum(10, 11) == 21