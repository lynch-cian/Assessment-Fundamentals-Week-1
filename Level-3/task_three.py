"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""

"""VAT RECEIPT

Bread x 2 - £2.88
Milk x 1 - £0.64
Butter x 1 - £0.96

Total: £4.48
VAT: £1.12
Total inc VAT: £5.60"""


def generate_invoice(receipt_string: str) -> str:
    """Generates a VAT invoice given a receipt"""
    receipt_list = receipt_string.splitlines(
    )  # Splits the string into a list by each new line
    invoice_string = "VAT RECEIPT\n\n"
    excluding_vat = 0.00
    total = 0.00
    if "Total" not in receipt_list[0]:
        for item in receipt_list:  # Finds the name and price of each item

            if item.find("Total") == -1:  # Checks to exclude the original total
                price_index = (item.find("£") + 1)
                name_index = item.find(" - ")
                item_price = item[price_index:]
                item_name = item[:name_index]

                total += float(item_price)
                excluding_vat = (float(item_price) / 100) * 80
                # Fills a line with item name and total exl VAT
                invoice_string += (f"{item_name} - £{excluding_vat:.2f}\n")
        invoice_string += "\n"

    # Maths for calculating VAT
    total_excluding_vat = (float(total) / 100) * 80
    vat = total - total_excluding_vat

    invoice_string += (f"Total: £{total_excluding_vat:.2f}")
    invoice_string += (f"\nVAT: £{vat:.2f}")
    invoice_string += (f"\nTotal inc VAT: £{total:.2f}")
    return invoice_string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
