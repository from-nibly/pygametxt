from roomMaster import ROOMMaster
import lib
import player

def test():
  print "this is working";


class ROOM2(ROOMMaster):
  commands = {};
  def __init__(self):
    self.commands["testing"] = test