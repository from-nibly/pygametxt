import lib
import player
from rooms import room2
from roomMaster import ROOMMaster
import roomlist

def youwin():
  print "You WIN!"
  player.addInventory("gold", 100000000);
  player.print_inventory();

def goleft():
  print "You enter a dark and scary room"
  return roomlist.room2;

class ROOM1 (ROOMMaster):
  commands = {};
  def __init__(self):
    self.commands["Win the game"] = youwin
    self.commands["go left"] = goleft  
  

    