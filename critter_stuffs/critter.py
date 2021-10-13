import random
from critter_stuffs import new_critterparts
import math

"""Critter Class

The Critter class takes a name as a str, the mode which switches between random and manual creation, and the part list which expects a list of strings containing the part names

needs new_critterparts and the parts.txt file


  

Critter attributes:
  self.name--String-- should be the name of the critter
  self.atk = 5 -- sets the attack attribute used in damage determination
  self.hp = 5 -- sets the health
  self.defense = 5 -- sets the defense used in damage reduction
  self.luc = 5 -- currently unused (would be used for crits)
  self.dex = 5 -- used to determine speed for priority
  self.spc  = 5 -- mostly unused, used by some specials attacks for dmg
  self.lvl = 1 -- sets the critter level most unused
  self.exp = self.lvl * 10 sets an exp value
  self.special_attacks = [basic_special, basic_special, basic_special, basic_special]
  self.counter = 0
  self.atkboost = 0
  self.atkboost_counter = 0
  self.hpboost = 0
  self.hpboost_counter = 0
  self.defense_boost = 0
  self.defense_boost_counter = 0
  self.luc_boost = 0
  self.luc_boost_counter = 0
  self.dex_boost = 0
  self.dex_boost_counter = 0
  self.spc_boost = 0
  self.spc_boost_counter = 0
  self.is_burn = False
  self.is_poisoned = False
  self.is_chilled = False
  self.is_shocked = False
  self.is_retaliating = False
  self.retaliate_Dmg = 0
  
Critter has four methods

print_features(self)
  simply prints a blurb about the creatures using move, feat1 and feat2

check_stats(self)
  prints out the critters stats

take_damage(self, damage = 0)
  takes damage as an int and the maths it against self.defense to determine how much to decrement self.hp before returning the value decremented from self.hp

deal_damage(self)

  uses self.atk, self.luc, self.dex to determine how much damage to return


give_stats(self)
  simply returns a tuple with all the stats
  (self.atk, self.hp, self.defense, self.luc, self.dex, self.spc, self.name)


is_alive(self)
  returns a bool True if hp > 0 and False otherwise



  """

def basic_special(crit):
  """takes in the atk, special, and dex of the critter and returns it"""
  print("BOOOOOP!!!!!")
  return crit.atk
  
class Critter:
  def __init__ (self, name = 'Rico', mode = 0, set_parts = []):
    
    self.atk = 5
    self.hp = 5
    self.defense = 5
    self.luc = 5
    self.dex = 5
    self.spc  = 5
    self.name = name
    self.lvl = 1 * random.randint(0,100)
    self.exp = self.lvl ^ 3
    self.special_attacks = [basic_special, basic_special, basic_special, basic_special]
    self.counter = 0
    self.atkboost = 0
    self.atkboost_counter = 0
    self.hpboost = 0
    self.hpboost_counter = 0
    self.defense_boost = 0
    self.defense_boost_counter = 0
    self.luc_boost = 0
    self.luc_boost_counter = 0
    self.dex_boost = 0
    self.dex_boost_counter = 0
    self.spc_boost = 0
    self.spc_boost_counter = 0
    self.is_burn = False
    self.is_poisoned = False
    self.is_chilled = False
    self.is_shocked = False
    self.is_stunned = False
    self.is_retaliating = False
    self.retaliate_Dmg = 0

    self.statusEffects =[]

    self.held_item = "Sitrus Berry"

    self.partlist = set_parts
    
    if mode == 0:
      while len(self.partlist) < 3:
        next_part = new_critterparts.critter_part(new_critterparts.make_part_list(new_critterparts.random_critterpart_ingest()))

        flag = 0

        for part in self.partlist:
          if next_part.name == part.name:
            flag = 1

      
        if flag != 1:
          self.partlist.append(next_part)

    if mode == 1:
      pass

        

    

    





  def print_features(self):
    #just prints of the features
    print("\nMy Name is {0}!".format(self.name))
    print("\nI am level {0}".format(self.lvl))
    print("I have {0}, {1} and {2}\n".format(self.partlist[0].name,self.partlist[1].name,self.partlist[2].name))

  def check_stats(self):
    #just prints off his stats
    print("\n=========================================")
    print("Critter Attack is: " + str(self.atk))
    print("Critter HP is: " + str(self.hp))
    print("Critter Defense is: " + str(self.defense))
    print("Critter Luck is: " + str(self.luc))
    print("Critter Dexterity is: " + str(self.dex))
    print("Critter Experience is: " + str(self.exp))
    print("========================================\n")

  def give_exp(self):
    """Just returns exp"""
    return self.exp

  def give_stats(self):
    """returns all teh stats as a tuple"""
    return (self.atk, self.hp, self.defense, self.luc, self.dex, self.spc, self.name)

  
  def take_damage(self,damage = 0):
    
    if isinstance(damage,tuple):
      incomingStates = damage[1]
      damage = damage[0]
      
    """Takes incoming damage as an int and returns damage dealt to hp as an int/ while also modifying self.hp """
    for x in incomingStates:
      self.statusEffects.append(x)
      
    print("\n{0}'s hp is currently: {1}".format(self.name, self.hp))
    if damage <= 0 or self.is_retaliating:
      self.retaliate_Dmg = damage
      return 0

    dmg_taken = damage - (round(self.defense * 0.75))
    if dmg_taken >= 0 and self.hp >=0 and self.hp >= dmg_taken:
      self.hp -= dmg_taken
      return dmg_taken
    elif dmg_taken >=0 and self.hp >=0:
      dmg_taken = self.hp
      self.hp = 0
      return dmg_taken
    else:
      return 0

  def deal_damage(self):
    """Takes in nothing does some math and poops out damage as an int"""

    #what's the random number of the day going be
    if self.is_alive() and not self.is_retaliating:
      dice_roll = random.randint(1,100)
      if dice_roll <= 25:
        return self.special_attacks[0](self)
      elif dice_roll <= 50:
        return self.special_attacks[1](self)
      elif dice_roll <= 75:
        return self.special_attacks[2](self)
      elif dice_roll <= 100:
        return self.special_attacks[3](self)
    
    elif self.is_retaliating:
      self.is_retaliating = False
      return self.retaliate_Dmg * 2
        

  def is_alive(self):
    """Checks health and reports if he's still alive"""
    if self.hp > 0:
      return True
    else:
      return False
  
  def im_heal(self,heal_amount):
    heal = round(heal_amount)
    if heal <= 0:
      heal = 1
    self.hp += heal
    return
  
  def update_stats(self):
    self.atk = 5
    self.hp = 50
    self.defense = 5
    self.luc = 5
    self.dex = 5
    self.spc  = 5



  def loop_update(self):
    for x in self.statusEffects:
      if x.passive == True:
        if x.self_target == True:
          x.effects(self)

    return





    for part in self.partlist:
      self.atk = self.atk + part.atk
      self.hp = self.hp + part.hp
      self.defense = self.defense + part.defense
      self.luc = self.luc + part.luc
      self.dex = self.dex + part.dex
      self.spc = self.spc + part.spc


    for x in range(1,len(self.special_attacks)):
      self.special_attacks.pop(x)
      self.special_attacks.insert(x,self.partlist[x - 1].special_attack)

    if self.lvl > 1:
      self.atk = math.ceil(self.atk + (self.lvl * 0.2))
      self.hp = math.ceil(self.hp + (self.lvl * 0.2))
      self.defense = math.ceil(self.defense + (self.lvl * 0.2))
      self.luc = math.ceil(self.luc + (self.lvl * 0.2))
      self.dex = math.ceil(self.dex + (self.lvl * 0.2))
      self.spc = math.ceil(self.spc + (self.lvl * 0.2))






  




