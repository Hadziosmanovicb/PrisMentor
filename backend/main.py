
from fastapi import FastAPI
from .products import products

app = FastAPI(title="PrisMentor API", version="0.1.0")


@app.get("/")
def home():
    return {"message": "PrisMentor virker!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/products")
def search_products(max_price: int = 10000):
    results = [
        product for product in products
        if product["price"] <= max_price
    ]
    return {"products": results}
