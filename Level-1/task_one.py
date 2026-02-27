
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    basket_output = ""
    total = 0.00
    if basket == []:
        return "Basket is empty"
    for item in basket:
        if float(item["price"]) > 0:
            basket_output += (f"{item["name"]} - £{item["price"]:.2f}\n")
        else:
            basket_output += (f"{item["name"]} - Free\n")
        total += float(item["price"])
    basket_output += (f"Total: £{total:.2f}")
    return basket_output


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
