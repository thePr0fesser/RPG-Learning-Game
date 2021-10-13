import math
import random


class statusEffects():
  def __init__(self):
    self.self_target = False
    self.target = False
    self.on_attack = False
    self.on_defen = False
    self.passive = False

  def effects(self):
    pass
    return
    

class multihit(statusEffects):
  def __init__(self):
    super().__init__()
    self.passive = True
    self.on_attack = True
    self.self_target = True
    self.counter = 0
  
  def effects(self, target):
    mh_roll = random.randint(1,100)
    if mh_roll >= 100 - (target.stren) and self.counter == 0:
      self.counter = 1
      return target.do_dmg()
    else:
      return 0


class rogue_dodge(statusEffects):
  def __init__(self):
    super().__init__()
    self.on_defen = True
    self.passive = True
    self.self_target = True
  
  def effects(self,target):
    rd_roll = random.randint(1,100)
    if rd_roll >= 100 - (target.dex):
      print("I activated")
      myvar = 0
      return 0
    else:
      return 0


class Burn(statusEffects):
  def __init__(self):
    super().__init__()
    self.self_target = True
    self.passive = True

  def effects(self,target):
    target.hp = math.ceil(target.hp - target.hp * 0.1)
    return



class dealBurn(statusEffects):
  def __init__(self):
    super().__init__()
    self.target = True
    self.on_attack = True

  def effects(self,target):
    new_burn = Burn()
    return new_burn 

    
    