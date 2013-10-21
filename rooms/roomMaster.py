import lib

class ROOMMaster:
  commands = {}
  
  def run(self):
    cmd = ''
    while not cmd == 'quit':
      cmd = lib.readcmd().lower();
      if(cmd in self.commands):
        result = self.commands[cmd]()
        if not result == None:
          return result