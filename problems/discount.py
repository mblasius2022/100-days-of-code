"""
8. Give me the discount
Create a function in Python that accepts two parameters. The first should be
the full price of an item as an integer. The second should be the discount
percentage as an integer.

The function should return the price of the item after the discount has been
applied. For example, if the price is 100 and the discount is 20, the function
should return 80.
"""
def apply_discount(amount, discount):
    """ calculate the discount """
    if type(amount) == int and type(discount) == int:
        discount = round(discount/100,2)
        discounted_amount = float(amount - (amount*discount))
        return round(discounted_amount,2)
    return 0

amount = int(input("Enter Amount: "))
discount = int(input("Discount to apply: "))
print(f"Discounted amount = {apply_discount(amount, discount)}")



