from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import transactions, users, merchants
from db_config import create_tables

app = FastAPI()

# Create database tables on startup
@app.on_event("startup")
async def startup():
    create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(transactions.router)
app.include_router(users.router)
app.include_router(merchants.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Financial Dashboard API"}