
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
def search_products(
    max_price: int = 10000,
    min_ram: int = 0,
    min_ssd: int = 0,
    gpu: str | None = None,
    in_stock: bool = True,
    condition: str = "new"
):
    results = []

    for product in products:
        if product["price"] > max_price:
            continue

        if product["ram"] < min_ram:
            continue

        if product["ssd"] < min_ssd:
            continue

        if gpu and gpu.lower() not in product["gpu"].lower():
            continue

        if in_stock and not product["in_stock"]:
            continue

        if product["condition"] != condition:
            continue

        results.append(product)

    return {"products": results}
