from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Order Service")

# DB connection
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cur = conn.cursor()

class Order(BaseModel):
    username: str
    item: str

@app.post("/create_order")
def create_order(order: Order):
    cur.execute("INSERT INTO orders (username, item) VALUES (%s, %s)", (order.username, order.item))
    conn.commit()
    return {"message": f"Order created for {order.username}"}

@app.get("/orders")
def get_orders():
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    return {"orders": rows}
