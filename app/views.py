from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal, engine
from database.model import Address,Base
from schemas import *
from typing import List
from geopy.distance import geodesic

router = APIRouter()

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AddressResponse)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


@router.put("/{address_id}/", response_model=AddressResponse)
def update_address(
    address_id: int, address: AddressUpdate, db: Session = Depends(get_db)
):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    for field, value in address.dict().items():
        setattr(db_address, field, value)
    db.commit()
    db.refresh(db_address)
    return db_address


@router.delete("/{address_id}/", status_code=204)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(db_address)
    db.commit()


@router.get("/", response_model=List[AddressResponse])
def get_addresses_within_distance(
    latitude: float, longitude: float, distance: float, db: Session = Depends(get_db)
):
    user_location = (latitude, longitude)
    addresses = db.query(Address).all()
    addresses_within_distance = []

    for address in addresses:
        address_location = (address.latitude, address.longitude)
        if geodesic(user_location, address_location).miles <= distance:
            addresses_within_distance.append(address)

    return addresses_within_distance

