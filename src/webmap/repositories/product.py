from .base import BaseRepository
from ..database.tables import DeteCoord

class ProductRepository(BaseRepository):

    async def get_all_data(self):
        # query = DateCoord.select().with_only_columns([DateCoord.c.dt_time])
        query = "SELECT dt_time::date from date_coord;"
        return await self.database.fetch_all(query=query)

    async def get_all_time_coord(self, date: str):
        return await self.database.fetch_all(
            query=f"SELECT dt_time::time, coord from date_coord where dt_time::date = date '{date}'; ")

    async def get_value_by_lon_lat(self,lo: float, la: float, date_pr: str, time: str, type_pr: str, lvl: int):
        return await self.database.fetch_one(
            query=f'''select lvl_{lvl}[get_index_lonlat({lo}, {la},'{date_pr} {time}')] as lvl_value
                from products inner join type_prod on type_prod.id=products.type_id
    			  inner join value_lvls on value_lvls.id=products.value_id
                where  name = '{type_pr}' and lvl_{lvl} is not null and products.dt_time = '{date_pr} {time}';''')

    async def get_type(self, date: str, time: str):
        level: int = 100
        return await self.database.fetch_all(query=f'''
            select name, description 
            from products 
            inner join type_prod on products.type_id=type_prod.id
            inner join value_lvls on value_lvls.id=products.value_id
            where main_tbl.dt_time = '{date} {time}' and lvl_{level} is not null ;
            ''')
