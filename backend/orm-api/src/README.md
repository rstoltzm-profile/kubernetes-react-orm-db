## Adding New Tables

1. **Define the Table**:
   Add a new SQLAlchemy class in `models.py`:
   ```python
   class NewTable(Base):
       __tablename__ = "new_table"
       __table_args__ = {"schema": "big_banker_schema"}
       id = Column(Integer, primary_key=True)
       name = Column(String)
   ```

2. **Create the Table**:
   Run `Base.metadata.create_all()` in `main.py` to create the new table in the database.

3. **Add CRUD Functions**:
   Add functions in `crud.py` for inserting, querying, updating, or deleting data in the new table.

4. **Add Pydantic Models**:
   Define Pydantic models in `schemas.py` for request validation and response serialization:
   ```python
   class NewTableBase(BaseModel):
       name: str

   class NewTableCreate(NewTableBase):
       pass

   class NewTableResponse(NewTableBase):
       id: int
       class Config:
           orm_mode = True
   ```

5. **Add API Endpoints**:
   Add endpoints in `api.py` to expose the new table's functionality:
   ```python
   @app.post("/new_table/", response_model=dict)
   def insert_new_table(data: List[NewTableCreate], db: Session = Depends(get_db)):
       # Insert logic here
       pass

   @app.get("/new_table/", response_model=List[NewTableResponse])
   def get_new_table(db: Session = Depends(get_db)):
       # Query logic here
       pass
   ```

---

```
1. Customers
This table stores information about the bank's customers.

CustomerID (Primary Key)
FirstName
LastName
DateOfBirth
Address
PhoneNumber
Email
DateJoined
2. Accounts
This table stores information about the bank accounts.

AccountID (Primary Key)
CustomerID (Foreign Key referencing Customers.CustomerID)
AccountType (e.g., Savings, Checking)
Balance
DateOpened
Status (e.g., Active, Closed)
3. Transactions
This table records all transactions made in the bank accounts.

TransactionID (Primary Key)
AccountID (Foreign Key referencing Accounts.AccountID)
TransactionType (e.g., Deposit, Withdrawal, Transfer)
Amount
TransactionDate
Description
4. Loans
This table stores information about loans taken by customers.

LoanID (Primary Key)
CustomerID (Foreign Key referencing Customers.CustomerID)
LoanType (e.g., Personal, Mortgage)
LoanAmount
InterestRate
StartDate
EndDate
Status (e.g., Active, PaidOff)
5. Branches
This table stores information about the bank's branches.

BranchID (Primary Key)
BranchName
Address
PhoneNumber
ManagerID (Foreign Key referencing Employees.EmployeeID)
6. Employees
This table stores information about the bank's employees.

EmployeeID (Primary Key)
FirstName
LastName
Position
BranchID (Foreign Key referencing Branches.BranchID)
HireDate
Salary
7. AccountTypes
This table stores information about different types of accounts.

AccountTypeID (Primary Key)
AccountTypeName (e.g., Savings, Checking)
InterestRate
```