# cart/item.py

from dataclasses import dataclass

@dataclass
class CartItem:
    product_id: str
    name: str
    price: float       # price per unit
    quantity: int = 1

    @property
    def total_price(self) -> float:
        return self.price * self.quantity
