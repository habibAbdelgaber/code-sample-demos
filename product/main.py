# main.py

from cart import Cart
from products import PRODUCTS, list_products

TAX_RATE = 0.17  # for example 17% tax


def show_menu() -> None:
    print("\n==== Shopping Cart Menu ====")
    print("1. Show products")
    print("2. Add product to cart")
    print("3. View cart")
    print("4. Update quantity")
    print("5. Remove item from cart")
    print("6. Checkout")
    print("0. Exit")


def main() -> None:
    cart = Cart()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_products()

        elif choice == "2":
            list_products()
            product_id = input("Enter product id to add: ").strip()
            if product_id not in PRODUCTS:
                print("Invalid product id.")
                continue

            try:
                qty = int(input("Enter quantity: ").strip())
            except ValueError:
                print("Quantity must be a number.")
                continue

            product = PRODUCTS[product_id]
            cart.add_item(
                product_id=product_id,
                name=product["name"],
                price=product["price"],
                quantity=qty,
            )
            print(f"Added {qty} x {product['name']} to cart.")

        elif choice == "3":
            print()
            print(cart)

        elif choice == "4":
            if cart.is_empty():
                print("Cart is empty.")
                continue

            print(cart)
            product_id = input("Enter product id to update: ").strip()
            if product_id not in cart.items:
                print("This product is not in your cart.")
                continue

            try:
                qty = int(input("Enter new quantity (0 to remove): ").strip())
            except ValueError:
                print("Quantity must be a number.")
                continue

            cart.update_quantity(product_id, qty)
            print("Cart updated.")

        elif choice == "5":
            if cart.is_empty():
                print("Cart is empty.")
                continue

            print(cart)
            product_id = input("Enter product id to remove: ").strip()
            cart.remove_item(product_id)
            print("Item removed (if it existed).")

        elif choice == "6":
            if cart.is_empty():
                print("Your cart is empty. Nothing to checkout.")
                continue

            print("\n=== Checkout ===")
            print(cart)
            subtotal = cart.subtotal()
            total = cart.total(TAX_RATE)
            tax = total - subtotal

            print(f"Tax ({TAX_RATE * 100:.0f}%): ${tax:.2f}")
            print(f"Total to pay: ${total:.2f}")
            print("Thank you for your purchase!")
            cart.clear()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
