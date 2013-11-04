import player
from roomMaster import ROOMMaster

local = {}

def attackTheTroll():
  if("bat" in play.inventory):
    
  


class Troll(ROOMMaster):
  def synopsis(self):
    if(local.get('trollisdead') or '' == ''):
      print '''
      you hear a growl in the cave.
      '''
    else:
      print '''
      you can smell the dead troll
      '''
    
  def __init__(self):
    ROOMMaster.__init__(self)
    self.commands["attack the troll"] = attackTheTroll;
    