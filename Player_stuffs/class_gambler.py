from Player_stuffs import player
import random
from statusEffects import statusLibrary


class gambler(player.everyone):
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
    self.statusEffects = [statusLibrary.gambler_mth()]
    #self.def = (self.stren + self.dex)