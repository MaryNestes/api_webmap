from fastapi import APIRouter, Depends, Query
from ..repositories.product import ProductRepository
from .depends import get_main_repository
from ..models.product import TypeProductOut, DateIn, TimeIn, KindType, KindLvL, ValueOut

router = APIRouter(
    prefix='/product',
)


@router.get('/date')
async def get_all_data(
        repo: ProductRepository = Depends(get_main_repository)
):
    return await repo.get_all_data()


@router.get('/time')
async def get_all_time_coord(
        date: DateIn,
        repo: ProductRepository = Depends(get_main_repository)
):
    return await repo.get_all_time_coord(date)


@router.get('/type', response_model=TypeProductOut)
async def get_type_by_date(
        date: DateIn,
        time: TimeIn,
        level: KindLvL,
        repo: ProductRepository = Depends(get_main_repository)
):
    return await repo.get_type(date, time, level)


@router.get('/value')
async def get_by_lon_lat(
        lon: float,
        lat: float,
        date: DateIn,
        time: TimeIn,
        level: KindLvL,
        tp: KindType,
        repo: ProductRepository = Depends(get_main_repository)
):
    return await repo.get_value_by_lon_lat(lon, lat, date, time, level, tp)
