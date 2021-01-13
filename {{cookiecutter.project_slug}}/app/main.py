from typing import Union


def myabs(n:Union[int,float]):
    assert isinstance(n,(int,float))
    if n >= 0:
        return n
    return -n
