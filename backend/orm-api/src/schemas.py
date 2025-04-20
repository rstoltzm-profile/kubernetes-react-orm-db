from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Base Pydantic model for Customers
class CustomersBase(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    Phone: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    ZipCode: Optional[str] = None
    Country: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateOfBirth: Optional[datetime] = None

# Model for creating a new Customer
class CustomersCreate(CustomersBase):
    pass

# Model for returning Customer data (response)
class CustomersResponse(CustomersBase):
    CustomerID: int

    class Config:
        orm_mode = True
