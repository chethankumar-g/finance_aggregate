# Financial Dashboard Project

This project is a financial dashboard that aggregates and normalizes financial data from various sources, providing a unified interface for accessing, analyzing, and managing this information. It is built using FastAPI for the backend and React.js for the frontend.
(HSBC Hackathon Project)
## Features

- Real-time configurable dashboard visualizing financial data through multiple graphs.
- Role-based filtering using JWT for user, client, and admin segregation.
- Secure data segregation and implementation of security protocols.
- Additional backend layers for data performance analysis and scalability.

## Table of Contents
1. [Features](#features)
2. [Architecture](#architecture)
3. [Project Structure](#project-structure)
4. [Database Schema](#database-schema)
5. [API Documentation](#api-documentation)
6. [Frontend Components](#frontend-components)
7. [Setup Instructions](#setup-instructions)
8. [Security Features](#security-features)

## Features

### Backend Features
- JWT-based authentication and authorization
- Role-based access control (User, Admin, Merchant)
- RESTful API endpoints for data management
- MySQL database with SQLAlchemy ORM
- Secure password hashing using bcrypt
- Environment variable configuration
- CORS middleware for frontend integration

### Frontend Features
- Material-UI based responsive design
- Real-time data visualization using Chart.js
- Protected routes with JWT authentication
- Dynamic dashboard with transaction analytics
- User authentication and session management
- Error handling and loading states

## Architecture

### Backend Stack
- FastAPI (Python web framework)
- MySQL (Database)
- SQLAlchemy (ORM)
- PyJWT (Authentication)
- Uvicorn (ASGI server)

### Frontend Stack
- React.js
- Material-UI
- Chart.js
- Axios
- React Router

## Project Structure

```
financial-dashboard/
├── backend/
│   ├── src/
│   │   ├── models.py          # Database models
│   │   ├── db_config.py       # Database configuration
│   │   ├── auth.py           # Authentication logic
│   │   ├── transactions.py   # Transaction routes
│   │   ├── users.py         # User management
│   │   └── merchants.py     # Merchant management
│   ├── .env                # Environment variables
│   └── requirements.txt    # Python dependencies
└── frontend/
    ├── src/
    │   ├── components/     # Reusable components
    │   ├── pages/         # Page components
    │   ├── services/      # API services
    │   └── App.jsx       # Main application
    ├── .env             # Frontend environment
    └── package.json     # Node dependencies
```

## Database Schema

### Transactions Table
```sql
CREATE TABLE transactions (
    step INTEGER PRIMARY KEY,
    customer_id VARCHAR(10),
    age INTEGER,
    gender VARCHAR(10),
    zipcodeOri INTEGER,
    merchant_id INTEGER,
    zipMerchant INTEGER,
    category VARCHAR(50),
    amount FLOAT,
    fraud INTEGER,
    FOREIGN KEY (customer_id) REFERENCES users(customer_id),
    FOREIGN KEY (merchant_id) REFERENCES merchants(merchant_id)
);
```

### Users Table
```sql
CREATE TABLE users (
    customer_id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    password VARCHAR(128),
    gender VARCHAR(10)
);
```

### Merchants Table
```sql
CREATE TABLE merchants (
    merchant_id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    category VARCHAR(50),
    password VARCHAR(128)
);
```

## API Documentation

### Authentication Endpoints

#### Login
```http
POST /auth/login
Content-Type: application/json

Request:
{
    "email": "string",
    "password": "string"
}

Response:
{
    "access_token": "string",
    "token_type": "bearer"
}
```

### Transaction Endpoints

#### Get All Transactions
```http
GET /api/transactions
Authorization: Bearer {token}
```

#### Create Transaction
```http
POST /api/transactions
Authorization: Bearer {token}
Content-Type: application/json

{
    "amount": float,
    "category": string,
    "merchant_id": integer
}
```

## Frontend Components

### 1. Authentication
- Login form with JWT token management
- Protected route wrapper
- Session management

### 2. Dashboard
- Transaction history visualization
- Category distribution charts
- Financial overview statistics

### 3. Data Visualization
- Line charts for transaction history
- Pie charts for category distribution
- Bar charts for fraud detection

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- MySQL 8.0+

### Backend Setup

1. Create virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Configure environment:
```bash
# backend/.env
DB_USER=root
DB_PASSWORD=Root
DB_HOST=localhost
DB_PORT=3306
DB_NAME=hsbc_hackathon
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
```

4. Start backend server:
```bash
cd src
uvicorn main:app --reload --port 8000
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Configure environment:
```bash
# frontend/.env
REACT_APP_API_URL=http://localhost:8000
```

3. Start frontend server:
```bash
npm start
```

## Security Features

### JWT Authentication
- Token-based authentication
- Password hashing with bcrypt
- Protected API endpoints
- Session management

### Data Security
- CORS protection
- SQL injection prevention
- XSS protection
- Secure password storage

## Access Points

- Backend API: http://localhost:8000
- Frontend App: http://localhost:3000
- API Documentation: http://localhost:8000/docs

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
