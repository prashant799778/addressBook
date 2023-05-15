from pydantic import BaseModel
from typing import List



class AddressCreate(BaseModel):
    street: str
    city: str
    state: str
    country: str
    latitude: float
    longitude: float


class AddressUpdate(BaseModel):
    street: str
    city: str
    state: str
    country: str


class AddressResponse(BaseModel):
    id: int
    street: str
    city: str
    state: str
    country: str
    latitude: float
    longitude: float
