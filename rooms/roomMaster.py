import lib
import player

def quit():
  exit()

class ROOMMaster:
  commands = {}
  def synopsis(self):
    pass
  
  def __init__(self):
    self.commands["inventory"] = player.printInventory
    self.commands["quit"] = quit;
    self.synopsis()

  def run(self):
    cmd = ''
    while not cmd == 'quit':
      cmd = lib.readcmd().lower();
      if(cmd in self.commands):
        result = self.commands[cmd]()
        if not result == None:
          return result