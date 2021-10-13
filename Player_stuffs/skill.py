import random

class tricks():
  def __init__(self):
    self.fortunepts = 10
    self.cooldown = 0
    self.stun = 0
    self.useable = True

  def cooldowntimer(self):  
    if self.cooldown != 0:
      self.usable = False
      self.cooldown -= 1

class pommelstr(tricks):
  def __init__(self):
    super().__init__()
    self.hit_roll = 0
    self.dam_num = 0

  def activate(self, player, critter):
    if self.useable == True:
      self.hit_roll = random.randint(1,100)
      if self.hit_roll >= 100 - (player.hr + player.stren):
        print("Your pommel strike has hit!")
        critter.is_stunned = True
        self.dam_num = (random.randint(1,(player.stren//2)))
        critter.hp = critter.hp - self.dam_num
        return critter.hp
        self.cooldown = 3
        player.fortunepts -= 1  
        self.cooldowntimer()
      else:
        print("You missed your pommel strike!")
        self.cooldown = 3
        self.cooldowntimer()
    else:
      return


