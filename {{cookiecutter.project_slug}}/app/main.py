def myabs(n: int):
    assert isinstance(n, int)
    if n >= 0:
        return n
    return -n
