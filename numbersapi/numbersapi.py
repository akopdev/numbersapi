from typing import Any, Dict
import requests
from .responses import BaseResponse, DateResponse


class NumbersApi():
    def __init__(self) -> None:
        pass

    def _request(self, number: str, type: str = 'trivia') -> Dict[str, Any]:
        try:
            response = requests.get(
                "http://numbersapi.com/{0}/{1}?json".format(number, type), timeout=30)
            response.raise_for_status()
            result = response.json()
        except requests.exceptions.HTTPError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        return result

    def trivia(self, number: int = None) -> BaseResponse:
        result = self._request(number)
        return BaseResponse(**result)

    def math(self, number: int = None) -> BaseResponse:
        result = self._request(number, type='math')
        return BaseResponse(**result)

    def date(self, month: int = None, day: int = None) -> DateResponse:
        date = "{0}/{1}".format(month, day)
        result = self._request(date, type='date')
        return DateResponse(**result)

    def year(self, number: int = None) -> BaseResponse:
        result = self._request(number, type='year')
        return BaseResponse(**result)
