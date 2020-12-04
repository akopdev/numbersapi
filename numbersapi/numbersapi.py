from typing import Any, Dict
import requests
from .responses import BaseResponse, DateResponse
from .enums import NumbersApiType, NumbersApiNotFound
from .exceptions import ServiceResponseError, WrongNumber, OptionNotSupported


class NumbersApi():

    options = {
        'json': True
    }

    def __init__(self, fragment: bool = False, notfound: NumbersApiNotFound = None, default: str = None, min: int = None, max: int = None) -> None:
        if fragment:
            self.options.setdefault('fragment', True)

        if min is not None:
            if not isinstance(min, int):
                raise OptionNotSupported()
            self.options.setdefault('min', min)

        if max is not None:
            if not isinstance(max, int):
                raise OptionNotSupported()
            self.options.setdefault('max', max)

        if default:
            self.options.setdefault('default', default)

        if notfound:
            try:
                nf = NumbersApiNotFound(notfound)
            except ValueError:
                raise OptionNotSupported()
            else:
                self.options.setdefault('notfound', nf.value)



    def _request(self, number: str, type: NumbersApiType = NumbersApiType.TRIVIA) -> Dict[str, Any]:
        try:
            response = requests.get(
                "http://numbersapi.com/{0}/{1}".format(number, type.value), params=self.options, timeout=30)
            response.raise_for_status()
            result = response.json()
        except requests.exceptions.HTTPError as error:
            raise ServiceResponseError(error)
        except Exception as error:
            raise ServiceResponseError(error)
        return result

    def trivia(self, number: int = None) -> BaseResponse:
        if number is None:
            number = 'random'
        elif not isinstance(number, int):
            raise WrongNumber()

        result = self._request(number, type=NumbersApiType.TRIVIA)
        return BaseResponse(**result)

    def math(self, number: int = None) -> BaseResponse:
        if number is None:
            number = 'random'
        elif not isinstance(number, int):
            raise WrongNumber()

        result = self._request(number, type=NumbersApiType.MATH)
        return BaseResponse(**result)

    def date(self, month: int = None, day: int = None) -> DateResponse:
        if month is None and day is None:
            date = 'random'
        elif not isinstance(month, int) or not isinstance(day, int):
            raise WrongNumber()
        elif int(month) > 12 or int(day) > 31:
            raise WrongNumber()
        else:
            date = "{0}/{1}".format(month, day)

        result = self._request(date, type=NumbersApiType.DATE)
        return DateResponse(**result)

    def year(self, number: int = None) -> BaseResponse:
        if number is None:
            number = 'random'
        elif not isinstance(number, int):
            raise WrongNumber()
        result = self._request(number, type=NumbersApiType.YEAR)
        return BaseResponse(**result)
