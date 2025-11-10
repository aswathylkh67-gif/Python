rice_price = 40
sugar_price = 30
oil_price = 130
rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8
rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty
print("total price of rice:", rice_total)
print("Total price of sugar:", sugar_total)
print("Total price of oil:", oil_total)
final_bill = rice_total + sugar_total + oil_total
print("Final bill amount:", final_bill)
final_bill_int = int(final_bill)
final_bill_str = str(final_bill)
print("Final Bill ", final_bill)
print("Final bill as integer:", final_bill_int)
print("Final bill as string:", final_bill_str)
import random
delivery_charge = random.randrange(5,10)
final_amount = final_bill + delivery_charge
print("Delivery charge added:", delivery_charge)
print("Final amount after adding delivery charge:", final_amount)

