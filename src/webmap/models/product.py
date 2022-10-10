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


class DateIn:
    def __init__(
            self,
            date: str = Query(regex='^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$')
    ):
        self.date = date

class CommonTimeItemsIn(DateIn):
    def __init__(
            self,
            level: KindLvL,
            date: str,
            time: str = Query(regex='^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$')
    ):
        super().__init__(date)
        self.time = time
        self.level = level


class CommonProdItemsIn(CommonTimeItemsIn):
    def __init__(
            self,
            level: KindLvL,
            tp: KindType,
            lon: float,
            lat: float,
            date: str,
            time: str,
    ):
        super().__init__(date=date, time=time, level=level)
        self.tp = tp
        self.lon = self.round_coord(lon)
        self.lat = self.round_coord(lat)

    @classmethod
    def round_coord(cls, value):
        return round(round(value * 2) / 2, 1)


class TypeProductOut(BaseModel):
    name: str
    description: str


class ValueOut(BaseModel):
    lvl_value: float
