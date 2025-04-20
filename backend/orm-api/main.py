from sqlalchemy.exc import SQLAlchemyError
from src.models import Base, Customers
from src.database import engine, SessionLocal
from src.crud import insert_table_data, query_table_data
from datetime import datetime

data = [
    Customers(
        FirstName="John",
        LastName="Doe",
        Email="john.doe@example.com",
        Phone="123-456-7890",
        Address="123 Elm Street",
        City="Springfield",
        State="IL",
        ZipCode="62704",
        Country="USA",
        DateCreated=datetime.now(),
        DateOfBirth=datetime(1990, 5, 15)
    ),
    Customers(
        FirstName="Jane",
        LastName="Smith",
        Email="jane.smith@example.com",
        Phone="987-654-3210",
        Address="456 Oak Avenue",
        City="Shelbyville",
        State="IL",
        ZipCode="62565",
        Country="USA",
        DateCreated=datetime.now(),
        DateOfBirth=datetime(1985, 8, 25)
    )
]

def create_schema_and_table():
    """Create schema and tables."""
    try:
        Base.metadata.create_all(bind=engine)
    except SQLAlchemyError as e:
        print(f"Error creating schema or tables: {e}")

def main():
    """Main function to orchestrate database operations."""
    create_schema_and_table()

    session = SessionLocal()
    table = Customers
    try:
        # Insert data
        insert_table_data(session, data)

        # Query data
        results = query_table_data(session, table)
        for row in results:
            print(f"row: {row}")
    finally:
        session.close()

if __name__ == "__main__":
    main()