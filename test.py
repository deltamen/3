from app import addition

def test_addition():
    assert add(2, 3) == 5

def test_negative_numbers():
    assert add(-1, -1) == -2

def test_mixed_numbers():
    assert add(5, -3) == 2