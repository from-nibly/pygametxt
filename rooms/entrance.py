import lib
import player
from roomMaster import ROOMMaster



def goNorth():
  from rooms import troll
  return troll.Troll()

def pickUpBat():
  if player.checkInventory("Bat") <=0:
    print "You pick up a bat. It looks like its made out of oak."
    player.addInventory("Bat", 1)
  else:
    print "You already have a Bat no sense in picking up another."



class Entrance (ROOMMaster):
  def synopsis(self):
    print '''
    You enter a cave and there are bats on the walls.
    There is a door to the North.
    '''
  def __init__(self):
    ROOMMaster.__init__(self)
    self.commands["go north"] = goNorth
    self.commands["open door"] = goNorth
    self.commands["pick up a bat"] = pickUpBat
    self.commands["grab a bat"] = pickUpBat
    