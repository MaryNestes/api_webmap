from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

from ..settings import settings

engine = create_engine(
    settings.database_url
)

database = Database(settings.database_url)
metadata = MetaData()

Base = declarative_base()
