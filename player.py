import lib;

inventory = {}

def print_inventory():
  print "You have: "
  for name, qty in inventory.items():
    print (name + " X " + str(qty))
    
def addInventory(item, qty):
  inventory[item] = qty