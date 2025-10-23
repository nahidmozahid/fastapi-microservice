from fastapi import FastAPI
import httpx
from models import User, Order  # import models

app = FastAPI(title="API Gateway")

USER_SERVICE = "http://127.0.0.1:8001"
ORDER_SERVICE = "http://127.0.0.1:8002"

@app.get("/")
def home():
    return {"message": "Welcome to the Microservice Gateway"}

@app.get("/users")
async def users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE}/users")
        return response.json()

@app.get("/orders")
async def orders():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ORDER_SERVICE}/orders")
        return response.json()

# Forward user registration
@app.post("/register")
async def register_user(user: User):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE}/register", json=user.dict())
        return response.json()

# Forward order creation
@app.post("/create_order")
async def create_order(order: Order):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{ORDER_SERVICE}/create_order", json=order.dict())
        return response.json()
