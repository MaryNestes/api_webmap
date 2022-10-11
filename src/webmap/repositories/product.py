from .base import BaseRepository
from ..database.tables import DeteCoord
from ..models.product import TypeProductOut, CommonProdItemsIn, CommonTimeItemsIn


class ProductRepository(BaseRepository):

    async def get_all_data(self):
        query = "SELECT DISTINCT dt_time::date from date_coord;"
        return await self.database.fetch_all(query=query)

    async def get_all_time_coord(self, date: str):
        return await self.database.fetch_all(
            query=f"SELECT dt_time::time, coord from date_coord where dt_time::date = date '{date}'; ")

    async def get_value_by_lon_lat(self, data: CommonProdItemsIn):
        # return {'lon': data.lon, 'lat': data.lat}
        return await self.database.fetch_all(
            query=f'''select lvl_{data.level}[check_index({data.lon}, {data.lat},'{data.date} {data.time}')] as lvl_value
                from products inner join type_prod on type_prod.id=products.type_id
    		  inner join value_lvls on value_lvls.id=products.value_id
            where  name = '{data.tp}' and lvl_{data.level} is not null and products.dt_time = '{data.date} {data.time}';''')

    async def get_type(self, data: CommonTimeItemsIn):
        return await self.database.fetch_all(query=f'''
            select name, description 
            from products 
            inner join type_prod on products.type_id=type_prod.id
            inner join value_lvls on value_lvls.id=products.value_id
            where products.dt_time = '{data.date} {data.time}' and lvl_{data.level} is not null ;
            ''')
