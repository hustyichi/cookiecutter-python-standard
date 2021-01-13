import pytest
from app.main import myabs


def test_myabs():
    assert myabs(5) == 5
    assert myabs(-123) == 123
    assert myabs(0) == 0

    with pytest.raises(AssertionError):
        myabs('aaa')
