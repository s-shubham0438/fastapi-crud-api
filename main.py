from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
items = {}

class Item(BaseModel):
    name: str
    price: float
    in_stock:  bool=True


@app.get("/")
def read():
    return{"message":"welcome to the api"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        return{"error":"item not found"}
    return items[item_id]
@app.post("/items/{item_id}")
def create_item(item_id: int,data:Item):
    items[item_id] = data
    return{"item_id":item_id, "item":data}
@app.get("/items")
def list_items():
    return items