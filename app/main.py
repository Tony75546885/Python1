from fastapi import FastAPI
from app.api.v1 import customers, auth

app = FastAPI(title="Company Management System")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(customers.router, prefix="/api/v1/customers", tags=["customers"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

