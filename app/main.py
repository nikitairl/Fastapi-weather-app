from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.get('/cities', response_model=list[schemas.CitySchemaView])
def get_cities(db: Session = Depends(get_db)):
    cities = crud.get_cities(db)
    return cities


@app.post('/cities', response_model=schemas.AddCitySchema)
def add_city(db: Session = Depends(get_db), city: schemas.AddCitySchema = Depends()):
    db_city = crud.add_city(db, city)
    return db_city
