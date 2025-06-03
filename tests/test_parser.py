from my_app import parser
from my_app.app import add, add_new_func


def test_parse_input():
    s = "John:100,Anna:200,Tom:150"
    expected = {"John": 100, "Anna": 200, "Tom": 150}
    assert parser.parse_input(s) == expected


def test_total_amount():
    d = {"John": 100, "Anna": 200, "Tom": 150}
    assert parser.total_amount(d) == 450


def test_max_person():
    d = {"John": 100, "Anna": 200, "Tom": 150}
    assert parser.max_person(d) == "Anna"


def test_min_person():
    d = {"John": 100, "Anna": 200, "Tom": 150}
    assert parser.min_person(d) == "John"


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(5, 5) == 10
    assert add(1, 1) == 2


def test_add_new_func():
    assert add_new_func(1, 1, 1) == 2
    assert add_new_func(2, 2, 2) == 8
    assert add_new_func(-1, 0, 5) == -5
    assert add_new_func(0, 0, 0) == 0
    assert add_new_func(1, 2, 1) == 3
