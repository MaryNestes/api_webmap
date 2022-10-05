from ..repositories.product import ProductRepository
from ..database.database import database

def get_main_repository() -> ProductRepository:
    return ProductRepository(database)
