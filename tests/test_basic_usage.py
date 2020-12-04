from numbersapi import NumbersApi

def test_trivia():
    na = NumbersApi()
    res = na.trivia(10)
    assert res.number == 10

def test_math():
    na = NumbersApi()
    res = na.math(10)
    assert res.number == 10

def test_date():
    na = NumbersApi()
    res = na.date(12, 20)
    assert isinstance(res.text, str)

def test_year():
    na = NumbersApi()
    res = na.year(2020)
    assert res.number == 2020