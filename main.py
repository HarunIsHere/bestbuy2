import products
import promotions
import store


def list_products(store_obj):
    """Print and return all active products in the store."""
    active_products = store_obj.get_all_products()
    print("------")
    for i, prod in enumerate(active_products, start=1):
        print(f"{i}. {prod}")
    print("------")
    return active_products


def make_order(store_obj):
    """Interactively collect an order from the user and execute it."""
    active_products = list_products(store_obj)

    shopping_list = []
    print("When you want to finish order, enter empty text.")

    while True:
        choice = input("Which product # do you want? ")
        if choice == "":
            break

        amount_str = input("What amount do you want? ")
        if amount_str == "":
            print("********")
            break

        try:
            choice_num = int(choice)
            amount = int(amount_str)
        except ValueError:
            print("Error adding product!\n")
            continue

        if choice_num < 1 or choice_num > len(active_products) or amount <= 0:
            print("Error adding product!\n")
            continue

        product = active_products[choice_num - 1]

        already = sum(qty for p, qty in shopping_list if p is product)
        if hasattr(product, "maximum") and already + amount > product.maximum:
            print("Error adding product!\n")
            continue

        if hasattr(product, "get_quantity") and product.get_quantity() != 0:
            if already + amount > product.get_quantity():
                print("Error adding product!\n")
                continue

        shopping_list.append((product, amount))
        print("Product added to list!\n")

    if not shopping_list:
        return

    try:
        total_price = store_obj.order(shopping_list)
    except Exception as e:
        print(f"Error making order: {e}\n")
        return

    if total_price == int(total_price):
        total_price_int = int(total_price)
    else:
        total_price_int = total_price

    print(f"Order made! Total payment: ${total_price_int}\n")


def start(store_obj):
    """Run the main store menu loop."""
    while True:
        print(
            """
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""".rstrip()
        )

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            print(f"Total: {store_obj.get_total_quantity()} items in store\n")
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            break


def main():
    """Create default inventory and start the user interface."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
