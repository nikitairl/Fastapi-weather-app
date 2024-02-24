from sqlalchemy.orm import Session

from . import models, schemas


def get_cities(db: Session):
    return db.query(models.City)


def add_city(db: Session, city: schemas.AddCitySchema):
    db_city = models.City(name=city.name, lat=city.lat, lon=city.lon)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city
