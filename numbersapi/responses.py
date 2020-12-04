from .exceptions import ServiceResponseError
from .enums import NumbersApiType

class BaseResponse():

    def __str__(self) -> str:
        return self.text

    def __init__(self, text: str = None, number: int = None, found: bool = False, type: str = None):
        if not text:
            raise ServiceResponseError("Empty text response")
        
        self.text = str(text)
        self.number = int(number)
        self.found = bool(found)
        try:
            self.type = NumbersApiType(type)
        except ValueError:
            raise ServiceResponseError("Not supported type")
        

class DateResponse(BaseResponse):
    def __init__(self, text: str = None, year: int = None, number: int = None, found: bool = False, type: str = None):
        self.year = int(year)
        super().__init__(text=text, number=number, found=found, type=type)
    