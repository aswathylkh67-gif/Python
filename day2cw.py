header = """\n\tBOOKSTORE RECEIPT\t\n"""

item1  = "Python Basics"
price1 = 450
item2 = "Data Science Intro"
price2 = 600
stack1= "BOOK: {0} - \t₹{1}"
stack2 = "BOOK: {0} - ₹{1}"
total= price1 + price2
thank_you = "\tThank you for shopping with us!\n"
receipt = header + "\n" + stack1.format(item1, price1) + "\n" + stack2.format(item2, price2) + "\n" + "Total Amount: ₹" + str(total) + "\n\n" + thank_you
print(receipt.upper())
