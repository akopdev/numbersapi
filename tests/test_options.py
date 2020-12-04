from numbersapi import NumbersApi
from numbersapi.exceptions import WrongNumber
import pytest
from faker import Faker

fake = Faker()

def test_default():
    default = fake.sentence(nb_words=10)
    na = NumbersApi(default=default)
    res = na.trivia(1111111111111111111)
    assert res.text == default
