from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from src.models import Customers

def insert_table_data(session: Session, data):
    """Insert data."""
    try:
        session.add_all(data)
        session.commit()
    except SQLAlchemyError as e:
        print(f"Error inserting data: {e}")
        session.rollback()
        raise

def query_table_data(session: Session, table):
    """Query data."""
    try:
        return session.query(table).all()
    except SQLAlchemyError as e:
        print(f"Error querying data: {e}")
        raise