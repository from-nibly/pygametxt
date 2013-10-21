import lib;

inventory = {}

def printInventory():
  print "You have: "
  for name, qty in inventory.items():
    print (name + " X " + str(qty))

    
def addInventory(item, qty):
  if item in inventory:
    inventory[item] += qty
  else:
    inventory[item] = qty

def checkInventory(item):
  try:
    return inventory[item];
  except:
    return 0