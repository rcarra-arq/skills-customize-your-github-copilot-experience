from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Dockerized FastAPI app"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return Item(id=item_id, name=f"Item {item_id}")
