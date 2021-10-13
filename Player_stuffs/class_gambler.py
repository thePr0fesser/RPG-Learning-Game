"""from player import everyone
import random


class gambler(everyone):
  def __init__(self,inventory,name):
    super().__init__(inventory)
    
    #char_class is the variable the person class uses to pass the stats
    self.user_choice_class = "Gambler"
    self.name = name
    self.stren = 10
    self.luck = 20
    self.dex = 15
    self.con = 10
    self.hp = (5 + self.con)
    #self.def = (self.stren + self.dex)

  def misstohit(self, target_critter):
    mth_chance = random.randint(1,100)
    if mth_chance >= 100 - (self.luck):
      print("{0} turned the Missed attack into a hit!".format(self.name))
      self.autohit = 1
      return self.do_dmg(target_critter)
    else:
      return 0"""