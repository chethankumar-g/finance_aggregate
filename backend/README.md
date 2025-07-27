# Financial Dashboard Backend API

A FastAPI-based backend that provides RESTful APIs for financial data management.

## Features

- JWT-based authentication
- Role-based access control
- Financial transaction management
- User and merchant management
- Secure password hashing
- Environment variable configuration

## Project Structure
```
backend/
├── src/
│   ├── database/      # Database models and configuration
│   ├── routers/       # API route handlers
│   ├── schemas/       # Pydantic models
│   ├── services/      # Business logic
│   ├── utils/         # Helper functions
│   └── main.py       # Application entry point
├── .env              # Environment variables
└── requirements.txt  # Python dependencies
```

## Setup Instructions

1. Create a MySQL database:
```sql
CREATE DATABASE hsbc_hackathon;
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`:
```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=hsbc_hackathon
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. Run the application:
```bash
cd src
uvicorn main:app --reload --port 8000
```

5. Access API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- POST /auth/token - Get access token
- POST /auth/refresh - Refresh access token

### Users
- POST /users/ - Create new user
- GET /users/{id} - Get user details
- GET /users/ - List users

### Transactions
- POST /transactions/ - Create transaction
- GET /transactions/{id} - Get transaction details
- GET /transactions/ - List transactions

### Merchants
- POST /merchants/ - Create merchant
- GET /merchants/{id} - Get merchant details
- GET /merchants/ - List merchants