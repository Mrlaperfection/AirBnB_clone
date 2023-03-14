def calculate_total_price(price_per_unit, quantity):
    """Calculate the total price for a given quantity of items."""
    total_price = price_per_unit * quantity
    return total_price


def main():
    """Main function to demonstrate calculate_total_price function."""
    price_per_unit = 10.5
    quantity = 25
    total_price = calculate_total_price(price_per_unit, quantity)
    print(f"The total price for {quantity} items at {price_per_unit} per unit is {total_price}.")


if __name__ == "__main__":
    main()
