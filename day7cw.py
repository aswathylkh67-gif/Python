
grocery_list = ["milk", "bread", "eggs"]
def add_item(item):
    grocery_list.append(item)
def remove_last_item():
            
        grocery_list.pop()
    
display_item = lambda item: print(f"Item: {item}")
def count_characters(items):
    if len(items) == 0:
        return 0
    return len(items[0]) + count_characters(items[1:])

print("Initial List:", grocery_list)

add_item("butter")
print("\nAfter Adding Items:", grocery_list)

remove_last_item()
print("\nAfter Removing Last Item:", grocery_list)

print("\nDisplaying Items:")
for i in grocery_list:
    display_item(i)

print("\nTotal Characters in List:", count_characters(grocery_list))
