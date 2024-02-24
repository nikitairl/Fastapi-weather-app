from sqlalchemy import Column, String, Integer, Float
from . db import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    tmp = Column(String, nullable=True)
    data = Column(String, nullable=True)
