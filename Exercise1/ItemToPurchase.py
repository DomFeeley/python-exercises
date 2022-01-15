class ItemtoPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quant = 0.0

    def __init__(self,name,price,quant):
        self.item_name = name
        self.item_price = price
        self.item_quant = quant

    def setItemName(self, name):
        self.item_name = name

    def setItemPrice(self, price):
        self.item_price = price
    
    def setItemQuant(self, quant):
        self.item_quant = quant

    def print_item_cost(self):
        print(self.item_name + " " + self.item_quant + " @ $" + self.item_price + " = $" + str(self.item_price*self.item_quant))

