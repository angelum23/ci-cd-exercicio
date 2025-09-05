from app import soma, multiplica


def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0


def test_multiplica():
    assert multiplica(3, 3) == 9
    assert multiplica(10, 10) == 100
    assert multiplica(100, 0) == 0
