from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import generate_description

app = FastAPI()

class Order(BaseModel):
    order: str 
    units: int

class Product(BaseModel):
    name: str 
    notes: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/hello")
async def hello_endpoint(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@app.post("/orders")
async def place_order(product: str, units: int):
    return {"message": f"Order for {units} units of {product} placed successfully."}

@app.post("/orders_pydantic")
# This POST endpoint uses Pydantic model Order
async def place_order(order: Order):
    return {"message": f"Order for {order.units} units of {order.order} placed successfully."}

@app.post("/product_description")
async def generate_product_description(product: Product):
    description = generate_description(f"Generate a product description for a product named '{product.name}'. Notes: {product.notes}.")
    return {"product_description": description}
