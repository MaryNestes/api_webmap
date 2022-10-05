
from fastapi import APIRouter, Depends, Query
from ..repositories.product import ProductRepository
from .depends import get_main_repository
from ..models.product import TypeProductOut, KindLvLIn, KindTypeIn, DateIn, TimeIn

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


@router.get('/type', response_model=list[TypeProductOut])
async def get_type_by_date(
        date: DateIn,
        time: TimeIn,
        repo: ProductRepository = Depends(get_main_repository)
):

    return await repo.get_type(date, time)


@router.get('/test')
async def get_by_lon_lat(
        lon: float,
        lat: float,
        type_pr: KindTypeIn,
        date: DateIn,
        time: TimeIn,
        level: KindLvLIn,
        repo: ProductRepository = Depends(get_main_repository)):

    return await repo.get_value_by_lon_lat(lon+180, lat+180, date, time, type_pr, level)
