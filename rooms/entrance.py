import lib
import player
from rooms import room2
from roomMaster import ROOMMaster
import roomlist


def goNorth():
  return roomlist.room2

def pickUpBat():
  if player.checkInventory("Bat") <=0:
    print "You pick up a bat. It looks like its made out of oak."
    player.addInventory("Bat", 1);
  else:
    print "You already have a Bat no sense in picking up another."

synopsis = '''
You enter a cave and there are bats on the walls.
There is a door to the North.
'''

class Entrance (ROOMMaster):
  commands = {};
  def __init__(self):
    print synopsis
    self.commands["go north"] = goNorth
    self.commands["open door"] = goNorth
    self.commands["pick up a bat"] = pickUpBat
    self.commands["grab a bat"] = pickUpBat
    