# products.py

# In a real-world app this would come from a database or API.
# For now we keep it very simple: a dict of product_id -> data.
PRODUCTS = {
    "p1": {"name": "T-Shirt", "price": 19.99},
    "p2": {"name": "Jeans", "price": 39.99},
    "p3": {"name": "Sneakers", "price": 59.99},
    "p4": {"name": "Hat", "price": 14.99},
}


def list_products() -> None:
    print("Available products:")
    for product_id, info in PRODUCTS.items():
        print(f"{product_id}: {info['name']} - ${info['price']:.2f}")
