# backend information

## Start up
```
docker-compose -f docker-compose.orm.yml up -d
docker-compose -f docker-compose.orm.yml build
docker-compose -f docker-compose.orm.yml down
```

## Project Structure

```
backend/
├── api.py                # FastAPI application exposing API endpoints
├── .env                  # usernames, passwords, and other environment variables
├── main.py               # Script for one-time database operations
├── start.sh              # Startup script to run either the API or main.py
├── Dockerfile            # Dockerfile for the backend service
├── docker-compose.orm.yml # Docker Compose file for the backend service
├── src/
│   ├── crud.py           # CRUD operations for database tables
│   ├── database.py       # Database connection and session management
│   ├── models.py         # SQLAlchemy models (database schema)
│   ├── schemas.py        # Pydantic models for API validation and serialization
database/
├── docker-compose.db.yml # Docker Compose file for PostgreSQL and pgAdmin
```

### Access the API
- The FastAPI application will be available at: [http://localhost:8000](http://localhost:8000)
- Interactive API documentation (Swagger UI) is available at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Run `main.py` for One-Time Operations
To run `main.py` instead of the API, set the `MODE` environment variable to `main`:
```bash
docker-compose -f docker-compose.orm.yml run -e MODE=main backend
```

###
```
curl -X POST "http://localhost:8000/customers/" \
-H "Content-Type: application/json" \
-d '[
    {
        "FirstName": "Test",
        "LastName": "Doe",
        "Email": "john.doe@example.com",
        "Phone": "123-456-7890",
        "Address": "123 Elm Street",
        "City": "Springfield",
        "State": "IL",
        "ZipCode": "62704",
        "Country": "USA",
        "DateCreated": "2025-04-08T12:00:00",
        "DateOfBirth": "1990-05-15T00:00:00"
    }
]'
```