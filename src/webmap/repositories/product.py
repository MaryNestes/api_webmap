from .base import BaseRepository
from ..database.tables import DeteCoord
from ..models.product import TypeProductOut, DateIn


class ProductRepository(BaseRepository):

    async def get_all_data(self):
        # query = DateCoord.select().with_only_columns([DateCoord.c.dt_time])
        query = "SELECT DISTINCT dt_time::date from date_coord;"
        return await self.database.fetch_all(query=query)

    async def get_all_time_coord(self, date: str):
        return await self.database.fetch_all(
            query=f"SELECT dt_time::time, coord from date_coord where dt_time::date = date '{date}'; ")

    async def get_value_by_lon_lat(self, lon, lat, date, time, level, tp):
        return await self.database.fetch_all(
            query=f'''select lvl_{level}[get_index_by_lonlat({lon}, {lat},'{date} {time}')] as lvl_value
                from products inner join type_prod on type_prod.id=products.type_id
    			  inner join value_lvls on value_lvls.id=products.value_id
                where  name = '{tp}' and lvl_{level} is not null and products.dt_time = '{date} {time}';''')

    async def get_type(self, date: str, time: str, level):
        return await self.database.fetch_all(query=f'''
            select name, description 
            from products 
            inner join type_prod on products.type_id=type_prod.id
            inner join value_lvls on value_lvls.id=products.value_id
            where products.dt_time = '{date} {time}' and lvl_{level} is not null ;
            ''')
