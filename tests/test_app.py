from my_app.app import add, add_new_func


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(5, 5) == 10

def test2_add():
    assert add(1, 1, 1) == 2
    assert add(2, 2 ,2) == 8
    assert add(-1, 0, 5) == -5