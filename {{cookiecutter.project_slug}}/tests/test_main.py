import pytest
from app.main import myabs


def test_myabs():
    assert myabs(0.1) == 0.1
    assert myabs(-10.5) == 10.5
    assert myabs(5) == 5
    assert myabs(-123) == 123
    assert myabs(0) == 0
    assert myabs(0.0) == 0.0

    with pytest.raises(AssertionError):
        myabs('aaa')
