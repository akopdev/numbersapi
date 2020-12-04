import pytest
from typing import Dict
from faker import Faker

fake = Faker()


@pytest.fixture(scope="module")
def trivia() -> Dict[str, str]:
    response = {
        "text": fake.sentence(nb_words=10),
        "number": fake.pyint(),
        "found": fake.pybool(),
        "type": "trivia"
    }
    return response
