from ItemToPurchase import ItemtoPurchase as i
item1 = i()
item2 = i()

item1.setItemName(input("Please enter the first item's name: "))
item1.setItemPrice(input("Please enter the first item's price: "))
item1.setItemQuant(input("Please enter the quantity of first item: "))

item2.setItemName(input("Please enter the second item's name: "))
item2.setItemPrice(input("Please enter the second item's price: "))
item2.setItemQuant(input("Please enter the quantity of second item: "))

item1.print_item_cost()
item2.print_item_cost()

total = item1.calc_item_cost()+item2.calc_item_cost()
print("Total: $" + str(total))