from enum import Enum

from pydantic import BaseModel

from fastapi import Query


class KindLvL(str, Enum):
    lvl_100 = '100'
    lvl_200 = '200'
    lvl_300 = '300'
    lvl_400 = '400'
    lvl_500 = '500'
    lvl_700 = '700'
    lvl_850 = '850'
    lvl_925 = '925'
    lvl_1000 = '1000'


class KindType(str, Enum):
    TMP = 'TMP'
    GMP = 'GMP'
    VMP = 'VMP'


class DateIn(str):
    date: str = Query(regex='^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$')


class TimeIn(str):
    time: str = Query(regex='^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$')


class TypeProductOut(BaseModel):
    name: str
    description: str


class ValueOut(BaseModel):
    lvl_value: float
