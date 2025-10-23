from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="User Service")

# DB connection
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cur = conn.cursor()

class User(BaseModel):
    username: str
    email: str

@app.post("/register")
def register_user(user: User):
    cur.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (user.username, user.email))
    conn.commit()
    return {"message": f"User {user.username} registered successfully"}

@app.get("/users")
def get_users():
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return {"users": rows}
