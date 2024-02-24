from typing import Optional
from pydantic import BaseModel


class AddCitySchema(BaseModel):
    name: str
    lat: float
    lon: float


class CitySchemaView(BaseModel):
    name: str
    lat: float
    lon: float
    tmp: Optional[str] = None
    data: Optional[str] = None
