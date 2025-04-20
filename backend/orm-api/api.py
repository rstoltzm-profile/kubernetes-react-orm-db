from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.models import Customers
from src.schemas import CustomersCreate, CustomersResponse
from src.crud import insert_table_data, query_table_data
from typing import List

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/customers/", response_model=dict)
def insert_customers(data: List[CustomersCreate], db: Session = Depends(get_db)):
    try:
        db_data = [Customers(**item.dict()) for item in data]
        insert_table_data(db, db_data)
        return {"message": "Customers inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/customers/", response_model=List[CustomersResponse])
def get_customers(db: Session = Depends(get_db)):
    try:
        results = query_table_data(db, Customers)
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))