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
    receipt_list = receipt_string.splitlines()
    invoice_string = "VAT RECEIPT \n\n"
    excluding_vat = 0.00
    total = 0.00
    for item in receipt_list:
        if item.find("Total") == -1:
            price_index = (item.find("£") + 1)
            name_index = item.find(" - ")
            item_price = item[price_index:]
            item_name = item[:name_index]

            total += float(item_price)
            excluding_vat = (float(item_price) / 100) * 80
            invoice_string += (item_name + " - £" +
                               str(f"{excluding_vat: .2f}") + "\n")
    invoice_string += (f"\nTotal: £{total:.2f}")
    invoice_string += (f"\nTotal: £{total:.2f}")
    invoice_string += (f"\nTotal: £{total:.2f}")
    return invoice_string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
