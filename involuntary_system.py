class Inventory:
    def __init__(self) :
        self.items={}
 
    def add_item(self,item_name,quantity,price_per_unit):  #Adds new products to the inventory or update the quantity 
                                                           #if the item already exists
        if item_name in self.items:                           
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity,'price_per_unit':price_per_unit}

            print (f"Added {quantity} units of {item_name} at R {price_per_unit:.2f} each.")
  
    def update_stock(self, item_name,quantity):   #allows the the user to increase or decrease the stock       
        if item_name in self.items:                #level of a specific item       
            self.items[item_name]['quantity'] += quantity

            if self.items[item_name]['quantity']<0:               
                self.items[item_name]['quantity']=0               

            print(f"Updated{item_name} stock by {quantity} units.")
        else:
            print(f"Error:{item_name} not found in inventory")
        
    def view_inventory(self):            # displays a list of all items in the inventory along with thier
        print("\nCurrent Inventory:")    # current stock level and price per unit
        for item_name, details in self.items.items():
            print(f"{item_name}:{details['quantity']} units available at R{details['price_per_unit']:.2f}each")
            print()

    def check_stock(self,item_name):    #allows the user to view the stock level of a specific item 
        if item_name in self.items:

            quantity = self.items[item_name]['quantity']
            return f"{item_name} has {quantity} units in stock."
        else:
            return f"error:{item_name} not found in inventory."

inventory=Inventory ()

inventory.add_item("Smartphone", 50, 2500)
inventory.add_item("laptop", 30, 8000)
inventory.add_item("bracelet", 60,1500)
inventory.add_item("Tablet", 50, 4000)
inventory.add_item("Smart Watch", 55, 1500)


inventory.update_stock("laptops",15)
inventory.update_stock("Smartphone",-12)

inventory.view_inventory()

print(inventory.check_stock("laptop"))
