from enum import Enum

class NumbersApiNotFound(Enum):
    FLOOR = 'floor'
    CEIL = 'ceil'

class NumbersApiType(Enum):
    TRIVIA = 'trivia'
    MATH = 'math'
    DATE = 'date'
    YEAR = 'year'