from enum import Enum

class NumbersApiNotFound(Enum):
    DEFAULT = 'default'
    FLOOR = 'floor'
    CEIL = 'ceil'

class NumbersApiType(Enum):
    TRIVIA = 'trivia'
    MATH = 'math'
    DATE = 'date'
    YEAR = 'year'