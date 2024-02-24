from pydantic import BaseModel


class AddCitySchema(BaseModel):
    name: str
    lat: float
    lon: float


class CitySchemaView(BaseModel):
    name: str
    lat: float
    lon: float
    tmp: str
