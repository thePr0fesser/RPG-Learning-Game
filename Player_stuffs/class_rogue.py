from Player_stuffs import player
import random
from statusEffects import statusLibrary


class rogue(player.everyone):
  def __init__(self,inventory,name):
    super().__init__(inventory)
    
    #char_class is the variable the person class uses to pass the stats
    self.user_choice_class = "Rogue"
    self.name = name
    self.stren = 15
    self.luck = 10
    self.dex = 20
    self.con = 10
    self.hp = (5 + self.con)
    self.statusEffects = [statusLibrary.rogue_dodge()]

    #self.defense = (self.stren + self.dex)
