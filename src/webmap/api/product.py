from fastapi import APIRouter, Depends, Query
from ..repositories.product import ProductRepository
from .depends import get_main_repository
from ..models.product import TypeProductOut, KindType, KindLvL, ValueOut, DateIn, CommonProdItemsIn, CommonTimeItemsIn

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
        date: DateIn = Depends(DateIn),
        repo: ProductRepository = Depends(get_main_repository)
):
    return await repo.get_all_time_coord(date.date)


@router.get('/type')
async def get_type_by_date(
        data: CommonTimeItemsIn = Depends(CommonTimeItemsIn),
        repo: ProductRepository = Depends(get_main_repository)
):
    return await repo.get_type(data)




@router.get('/value')
async def get_by_lon_lat(
        data: CommonProdItemsIn = Depends(CommonProdItemsIn),
        repo: ProductRepository = Depends(get_main_repository)
):
    return await repo.get_value_by_lon_lat(data)
