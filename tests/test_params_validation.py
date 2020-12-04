from numbersapi import NumbersApi
from numbersapi.exceptions import WrongNumber
import pytest
from faker import Faker

fake = Faker()

def test_trivia_random():
    na = NumbersApi()
    res = na.trivia()
    assert isinstance(res.number, int)

def test_trivia_wrong():
    na = NumbersApi()
    with pytest.raises(WrongNumber):
        na.trivia(fake.pystr())

def test_math_random():
    na = NumbersApi()
    res = na.math()
    assert isinstance(res.number, int)

def test_math_wrong():
    na = NumbersApi()
    with pytest.raises(WrongNumber):
        na.math(fake.pystr())

def test_year_random():
    na = NumbersApi()
    res = na.year()
    assert isinstance(res.number, int)

def test_year_wrong():
    na = NumbersApi()
    with pytest.raises(WrongNumber):
        na.year(fake.pystr())

def test_date_random():
    na = NumbersApi()
    res = na.date()
    assert isinstance(res.text, str)

def test_date_wrong_day():
    na = NumbersApi()
    with pytest.raises(WrongNumber):
        na.date(month=fake.pyint(), day=fake.pystr())

def test_date_wrong_month():
    na = NumbersApi()
    with pytest.raises(WrongNumber):
        na.date(month=fake.pystr(), day=fake.pyint())

def test_date_wrong():
    na = NumbersApi()
    with pytest.raises(WrongNumber):
        na.date(month=fake.pystr(), day=fake.pystr())