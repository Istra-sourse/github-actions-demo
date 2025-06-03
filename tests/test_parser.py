from my_app import parser


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
