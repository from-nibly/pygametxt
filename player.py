import lib;

inventory = {}

def printInventory():
  print "You have: "
  for name, qty in inventory.items():
    print (name + " X " + str(qty))

def haveAtleast(item, qty):
  if inventory[item] >= qty:
    return true
  else:
    return false

def addInventory(item, qty):
  if item in inventory:
    inventory[item] += qty
  else:
    inventory[item] = qty
    
def remInventory(item, qty):
  if item in inventory:
    inventory[item] -= qty;
  else:
    raise item + " was not in the inventory this is a BUG"
  if inventory[item] == 0:
    del inventory[item]
  elif inventory[item] < 0:
    raise "there was not enough of " + item;

def checkInventory(item):
  try:
    return inventory[item];
  except:
    return 0