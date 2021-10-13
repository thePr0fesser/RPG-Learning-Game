import math
from statusEffects import statusLibrary

def still_nothing(player):
  return statusLibrary.statusEffect()

def leatherarm_defup(player):
  """increases defense by 20% of the players dex"""
  player.defen = player.defen + math.floor(player.dex * 0.3)
  return 

def chainmail_dexdown(player):
  """Decreases player dex while wearing item by 10%"""
  player.dex = player.dex - math.ceil(player.dex * 0.1)
  return

def flametounge(player):
  """unique sword that applies burn"""
  return statusLibrary.dealBurn()


"""

def leatherup(player):
  player.def = self.def * player.dex
  return

player object();
  self.def
  self.inventory = [armor]

  def update_stats(self):
    various stat update_stats

    for items in inventory:
        do more stat updates 
        try:
            item.special_atter(self)
        except:
          pass



armor object();
  def __init__(blah):
    self.def
    self.special_atter = blah


player1 = player_object()
new_armor = armor_object(via magic)

"""