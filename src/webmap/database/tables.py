from sqlalchemy import Column, DateTime, ARRAY, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from decimal import Decimal
from ..database.database import metadata, Base


class DeteCoord(Base):
    __tablename__ = 'date_coord'

    dt_time = Column(DateTime(timezone=False), primary_key=True, index=True)
    coord = Column(ARRAY(Numeric(5, 2)))
    lat = Column(ARRAY(Numeric(5, 1)))
    lon = Column(ARRAY(Numeric(5, 1)))

    product = relationship('Products', back_populates='products')


class TypeProduct(Base):
    __tablename__ = 'type_prod'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    product = relationship('Products', back_populates='products')


class ValueLVL(Base):
    __tablename__ = 'value_lvls'

    id = Column(Integer, primary_key=True)
    lvl_100 = Column(ARRAY(Numeric(5, 1)))
    lvl_200 = Column(ARRAY(Numeric(5, 1)))
    lvl_300 = Column(ARRAY(Numeric(5, 1)))
    lvl_400 = Column(ARRAY(Numeric(5, 1)))
    lvl_500 = Column(ARRAY(Numeric(5, 1)))
    lvl_700 = Column(ARRAY(Numeric(5, 1)))
    lvl_850 = Column(ARRAY(Numeric(5, 1)))
    lvl_925 = Column(ARRAY(Numeric(5, 1)))
    lvl_1000 = Column(ARRAY(Numeric(5, 1)))

    product = relationship('Products', back_populates='products')


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    dt_time = Column(DateTime(timezone=False), ForeignKey('date_coord.dt_time'))
    type_id = Column(Integer, ForeignKey('type_prod.id'))
    value_id = Column(Integer, ForeignKey('value_lvls.id'))

    datecoord = relationship('DeteCoord', back_populates='date_coord')
    value = relationship('ValueLVL', back_populates='value_lvls')
    type_product = relationship('TypeProduct', back_populates='type_prod')
