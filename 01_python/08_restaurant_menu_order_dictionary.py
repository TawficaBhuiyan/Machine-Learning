"""
Restaurant menu ordering program using a dictionary in python


A simple menu-based ordering program that demonstrates dictionaries,
loops, conditions, and user input in Python.

Note: this program uses input(), so it is interactive.
      In Google Colab or a terminal it will pause and ask you to type.
"""

# The menu: item name -> price in dollars
menu = {
    "Coffee": 5,
    "Pasta": 15,
    "Pizza": 20,
    "Burger": 10,
    "Chicken Fry": 30,
    "Sandwitch": 12
}


def show_menu():
    """Print a clean welcome banner and the full menu."""
    print("=" * 40)
    print("  Welcome to Tawfica Bhuiyan's Restaurant!")
    print("  Please place your order below.")
    print("=" * 40)
    for item, price in menu.items():
        # ':<10' left-aligns the name so prices line up neatly
        print(f"  {item:<10} {price}৳")
    print("=" * 40)


def take_orders():
    """Keep taking orders until the customer is done, then return the total."""
    total_price = 0

    while True:
        item = input("\nEnter an item to order (or type 'done' to finish): ").strip().title()

        if item.lower() == "done":
            break

        if item in menu:
            total_price += menu[item]
            print(f"  Added {item} (${menu[item]}). Running total: ${total_price}")
        else:
            print("  Invalid item. Please order something from the menu.")

    return total_price


def main():
    show_menu()
    total_price = take_orders()

    print("\n" + "=" * 40)
    if total_price > 0:
        print(f"  Your total is {total_price}৳.")
        print("  Thank you for ordering from Tawfica Bhuiyan's Restaurant!")
    else:
        print("  No items ordered. See you next time!")
    print("=" * 40)


# This runs main() only when the file is executed directly.
if __name__ == "__main__":
    main()
