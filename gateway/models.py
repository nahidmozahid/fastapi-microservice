from pydantic import BaseModel

# User model
class User(BaseModel):
    username: str
    email: str

# Order model
class Order(BaseModel):
    username: str
    item: str
