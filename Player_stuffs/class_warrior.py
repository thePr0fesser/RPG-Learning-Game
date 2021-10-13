from Player_stuffs import player
import random
from statusEffects import statusLibrary


class warrior(player.everyone):
  def __init__(self,inventory,name):
    super().__init__(inventory)
    
    #char_class is the variable the person class uses to pass the stats
    self.user_choice_class = "Warrior"
    self.name = name
    self.stren = 20
    self.luck = 10
    self.dex = 10
    self.con = 15
    self.hp = (5 + self.con)
    self.statusEffects = [statusLibrary.multihit()]
    
    #self.defense = (self.stren + self.dex)

  