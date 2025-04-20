from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customers(Base):
    """Customers table model."""
    __tablename__ = "Customers"
    __table_args__ = {"schema": "big_banker_schema"}

    CustomerID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Email = Column(String(100))
    Phone = Column(String(20))
    Address = Column(String(200))
    City = Column(String(50))
    State = Column(String(50))
    ZipCode = Column(String(10))
    Country = Column(String(50))
    DateCreated = Column(DateTime)
    DateOfBirth = Column(DateTime)
