fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
vegetables = ['carrot', 'potato', 'cabbage']
beverages = ['water', 'juice', 'soda']
fruits.append('grape')
vegetables.insert(1, 'spinach')
beverages.pop()
inventory = [fruits, vegetables, beverages]
print("first two fruits:", fruits[:2])
print("last vegetable:", vegetables[-1])
fruits_length = [len(fruits) for fruits in fruits]
print("fruits lengths:", fruits_length)
if 'water' in beverages:
    print("Beverage 'water' is available.")
first_item = (fruits[0], vegetables[0], beverages[0])
print("First items:", first_item)