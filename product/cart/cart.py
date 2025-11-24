# cart/cart.py

from typing import Dict
from .item import CartItem


class Cart:
    def __init__(self) -> None:
        # key: product_id, value: CartItem
        self.items: Dict[str, CartItem] = {}

    def add_item(self, product_id: str, name: str, price: float, quantity: int = 1) -> None:
        if product_id in self.items:
            # If already exists, just increase quantity
            self.items[product_id].quantity += quantity
        else:
            self.items[product_id] = CartItem(
                product_id=product_id,
                name=name,
                price=price,
                quantity=quantity
            )

    def remove_item(self, product_id: str) -> None:
        if product_id in self.items:
            del self.items[product_id]

    def update_quantity(self, product_id: str, quantity: int) -> None:
        if product_id in self.items:
            if quantity <= 0:
                # Remove if quantity is zero or negative
                self.remove_item(product_id)
            else:
                self.items[product_id].quantity = quantity

    def clear(self) -> None:
        self.items.clear()

    def subtotal(self) -> float:
        return sum(item.total_price for item in self.items.values())

    def total(self, tax_rate: float = 0.0) -> float:
        subtotal = self.subtotal()
        tax = subtotal * tax_rate
        return subtotal + tax

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def __str__(self) -> str:
        if self.is_empty():
            return "Your cart is empty."

        lines = ["Your cart:"]
        for item in self.items.values():
            lines.append(
                f"- {item.name} (x{item.quantity}) @ ${item.price:.2f} = ${item.total_price:.2f}"
            )
        lines.append(f"Subtotal: ${self.subtotal():.2f}")
        return "\n".join(lines)
