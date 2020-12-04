from enum import Enum

class NumbersApiType(Enum):
    TRIVIA = 'trivia'
    MATH = 'math'
    DATE = 'date'
    YEAR = 'year'



class BaseResponse():
    def __init__(self, text: str = None, number: int = None, found: bool = False, type: str = None):
        self.text = str(text)
        self.number = int(number)
        self.found = bool(found)
        try:
            self.type = NumbersApiType(type)
        except ValueError:
            raise Exception("Wrong type")
        

class DateResponse(BaseResponse):
    def __init__(self, text: str = None, year: int = None, number: int = None, found: bool = False, type: str = None):
        self.year = int(year)
        super().__init__(text=text, number=number, found=found, type=type)
    