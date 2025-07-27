# Financial Dashboard Project

This project is a financial dashboard that aggregates and normalizes financial data from various sources, providing a unified interface for accessing, analyzing, and managing this information. It is built using FastAPI for the backend and React.js for the frontend.

## Features

- Real-time configurable dashboard visualizing financial data through multiple graphs.
- Role-based filtering using JWT for user, client, and admin segregation.
- Secure data segregation and implementation of security protocols.
- Additional backend layers for data performance analysis and scalability.

## Project Structure

```
financial-dashboard
├── backend
│   ├── src
│   │   ├── database
│   │   ├── routers
│   │   ├── schemas
│   │   ├── services
│   │   ├── utils
│   │   └── main.py
│   ├── alembic.ini
│   ├── requirements.txt
│   └── README.md
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── App.jsx
│   │   └── index.js
│   ├── package.json
│   └── README.md
└── README.md
```

## Backend

The backend is developed using FastAPI and includes:

- **Database Models**: Defined using SQLAlchemy for transactions, users, and merchants.
- **Authentication**: Handled through JWT for secure user access.
- **APIs**: Endpoints for managing transactions, users, and merchants.

## Frontend

The frontend is built with React.js and includes:

- **Dashboard**: A component for visualizing financial data.
- **Login**: A component for user authentication.
- **Charts**: A component for displaying various financial charts.

## Installation

To set up the backend, navigate to the `backend` directory and install the required dependencies:

```
pip install -r requirements.txt
```

For the frontend, navigate to the `frontend` directory and install the required dependencies:

```
npm install
```

## Running the Application

To run the backend, execute:

```
uvicorn src.main:app --reload
```

To run the frontend, execute:

```
npm start
```

## License

This project is licensed under the MIT License.