# Python client library to work with Numbersapi.com
Simple API client for numbersapi.com
## Features

- Supports major types like `trivia`, `math`, `date`, `year`
- Supports options `fragment`, `notfound`, `default`, `Min & Max`
- Minimum number of external dependencies

## Requirements
- requests

## Quickstart


```python
from numbersapi import NumbersApi


na = NumbersApi()
res = na.trivia(10)

>>> res.text
'10 is the number of hydrogen atoms in butane, a hydrocarbon.'
>>> res.number
'10'
>>> res.type
'trivia'
```

By default, result contains object with all attributes like `text`, `number`, `type` etc. 

You also can use `print` or `str` for more code simplification:

```python
from numbersapi import NumbersApi


na = NumbersApi()
res = na.trivia(10)

>>> print(res)
'10 is the number of hydrogen atoms in butane, a hydrocarbon.'
```

## Advanced usage

Random date

```python
from numbersapi import NumbersApi

na = NumbersApi()
res = na.date()
```

Default response option

```python
from numbersapi import NumbersApi

na = NumbersApi(default="Too many units")
res = na.date(1111111111111111111111)
```

## Tests

Covered by `pytest`

```shell
python -m pytest
```