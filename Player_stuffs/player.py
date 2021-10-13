import random
import math
from statusEffects import statusLibrary
from Items import item_attrs






#preset_classes are what classes that can get picked organized (stren, luck, dex, con)

class everyone:
  def __init__(self,inventory):
    self.aspeed = 1
    self.critch = 1
    self.critmultiplier = 1
    self.dam = 1
    self.hr = 50
    self.stren = 10
    self.dex = 10
    self.luck = 10
    self.con = 10
    self.inventory = inventory
    self.equipped_armor = None
    self.equipped_weapon = None
    self.next_lvl = 100
    self.fortunepts = 1

    if len(self.inventory) >= 1:
      for x in inventory:
        if x.type == 'weapon':
          self.equipped_weapon = x
          break

    if len(self.inventory) >= 1:
      for x in inventory:
        if x.type == 'armor':
          self.equipped_armor = x
          break
    

    self.xp = 0
    self.counter = 0
    self.autohit = 0
    self.dmgreduc = self.con
    self.defen = self.dex
    self.poisoned = 0
    self.burned = 0
    self.stunned = 0
    self.level = 1
    self.burnchance = 0

    self.statusEffects = []


  def reset_self(self):
    self.counter = 0
    self.autohit = 0
    

  def gethit(self, damage):
    """armordeflect_chance = random.randint(1,100)
    if armordeflect_chance >= 100 - (self.defen):
      print("Your armor protected you!")
      dmg_taken = 0
      return dmg_taken
    else:"""
    self.take_damage()
    for x in self.statusEffects:
      if x.on_defen:
        x.effects(self)
      else:
        pass 
    return



  def take_damage(self, damage = 0):
    """Takes incoming damage as an int and returns damage dealt to hp as an int/ while also modifying self.hp """
    if damage <= 0:
      return 0

    dmg_taken = damage - (round(self.dmgreduc))
    if dmg_taken > 0:
      self.hp -= dmg_taken
      return dmg_taken
    else:
      return 0

  def is_alive(self):
    if self.hp > 0:
      return True
    else:
      return False




  def check_stats(self):
    print("\n=========================================")
    print("{0}'s HP is: ".format(self.name) + str(self.hp))
    print("{0}'s FP is: ".format(self.name) + str(self.fortunepts))
    print("{0}'s EXP is: ".format(self.name) + str(self.xp))
    print("{0}'s Level is: ".format(self.name) + str(self.level))
    print("{0}'s Strength is: ".format(self.name) + str(self.stren))
    print("{0}'s Constitution is: ".format(self.name) + str(self.con))
    print("{0}'s Luck is: ".format(self.name) + str(self.luck))
    print("{0}'s Dexterity is: ".format(self.name) + str(self.dex))
    print("{0}'s Damage Reduction is: ".format(self.name) + str(self.dmgreduc))
    print("{0}'s Defense is: {1}".format(self.name,self.defen))
    print("{0}'s Attack Speed is: ".format(self.name) + str(self.aspeed))
    print("{0}'s Critical Hit Chance is: {1}".format(self.name,(self.critch + self.luck//2)))
    print("{0}'s Critical Multiplyer is: {1}".format(self.name,self.critmultiplier))
    print("{0}'s Hit Rate is: {1}".format(self.name,self.hr))
    print("{0}'s Damage is: ".format(self.name) + str(self.dam))
    print("Next level up: {0}".format(self.next_lvl))
    print("========================================\n")



  def do_dmg(self):
    #amount of dmg
    dmg_total = 0
    #if it hits
    hit_roll = random.randint(1,100)
    #check to see crit
    if hit_roll >= 100 - (self.critch + (self.luck//2)):
      dmg_total = math.ceil(self.critmultiplier * (random.randint(1,self.dam) + math.ceil(self.stren//2)))
      return dmg_total
    #check to see hit
    elif hit_roll >= 100 - (self.hr + (self.dex//2)) or self.autohit == 1:
      dmg_total = math.ceil(random.randint(1,self.dam) + (self.stren//2))
      return dmg_total
    #miss check
    else:
      return 0



  def setStatus(self, effect):
    self.statusEffects.append(effect)
    return



  def basic_atk(self,target):
    my_attack_effects = []
    my_dmg_amount = 0
    i_give_states = []
    for x in self.statusEffects:
      if x.on_attack == True:
        my_attack_effects.append(x)
      
    for x in my_attack_effects:
      if x.self_target == True:
        my_effects_return = x.effects(self)
      elif x.target == True:
        i_give_states.append(x.effects((target)))
        target.setStatus(i_give_states)


    my_dmg_amount = self.do_dmg()
    if type(my_effects_return) == type(int()):
      my_dmg_amount += my_effects_return

    return (my_dmg_amount)
    
        





  def update_stats(self):
    """updates the stats"""
    if self.equipped_weapon != None:
      self.aspeed = math.ceil(self.equipped_weapon.aspeed * (self.dex * 0.5))
      self.critch = self.equipped_weapon.critch
      self.critmultiplier = self.equipped_weapon.critmultiplier
      self.dam = self.equipped_weapon.dam
      self.hr = self.equipped_weapon.hr
      if self.equipped_weapon.special_attr.__name__ != "still_nothing":
        print("Hello")
        self.setStatus(self.equipped_weapon.special_attr(self))
      else:
        print("not hello")

      
    if self.equipped_armor != None:
      self.defen = self.equipped_armor.defen
      self.dmgreduc = self.equipped_armor.dmgreduc
    self.gainxp()
    self.level_up
    self.next_lvl
    self.fortunepts = round(self.luck/2)
    


    for item in self.inventory:
      try:
        item.special_attr(self)
        
      except:
        pass


  def new_equip(self,new_item):
    if new_item.type == 'weapon':
      self.inventory.append(new_item)
      self.equipped_weapon = new_item
    elif new_item.type =='armor':
      self.inventory.append(new_item)
      self.equipped_armor = new_item
    return

  def gainxp(self, expgain = 0):
    if expgain > 0:
      print("You gained {0} experience points!".format(expgain))
      self.xp = self.xp + expgain
      self.level_up()
  
  def level_up(self):
    if self.xp >= self.next_lvl:
      self.level += 1
      print("Congrats! You Leveled UP")
      self.next_lvl = round(self.next_lvl * 2)
      if self.user_choice_class == "Warrior":
        strenvar = random.randint(5,8)
        self.stren += strenvar
        print("Your Strength increased by {0} to {1}!".format(str(strenvar),self.stren))
        convar = random.randint(4,7)
        self.con += convar
        print("Your Constitution increased by {0} to {1}!".format(str(convar),self.con))
        dexvar = random.randint(3,6)
        self.dex += dexvar
        print("Your Dexterity increased by {0} to {1}!".format(str(dexvar),self.dex))
        luckvar = random.randint(3,6)
        self.luck += luckvar
        print("Your Luck increased by {0} to {1}!".format(str(luckvar),self.luck))
      elif self.user_choice_class == "Rogue":
        strenvar = random.randint(3,6)
        self.stren += strenvar
        print("Your Strength increased by {0} to {1}!".format(str(strenvar),self.stren))
        convar = random.randint(3,6)
        self.con += convar
        print("Your Constitution increased by {0} to {1}!".format(str(convar),self.con))
        dexvar = random.randint(5,8)
        self.dex += dexvar
        print("Your Dexterity increased by {0} to {1}!".format(str(dexvar),self.dex))
        luckvar = random.randint(4,7)
        self.luck += luckvar
        print("Your Luck increased by {0} to {1}!".format(str(luckvar),self.luck))
      elif self.user_choice_class == "Gambler":
        strenvar = random.randint(3,6)
        self.stren += strenvar
        print("Your Strength increased by {0} to {1}!".format(str(strenvar),self.stren))
        convar = random.randint(3,6)
        self.con += convar
        print("Your Constitution increased by {0} to {1}!".format(str(convar),self.con))
        dexvar = random.randint(4,7)
        self.dex += dexvar
        print("Your Dexterity increased by {0} to {1}!".format(str(dexvar),self.dex))
        luckvar = random.randint(5,8)
        self.luck += luckvar
        print("Your Luck increased by {0} to {1}!".format(str(luckvar),self.luck))
      self.update_stats()
    else:
      return
      pass

    


 


class bum(everyone):
  def __init__(self,name):
    super().__init__()
    #char_class is the variable the person class uses to pass the stats
    self.user_choice_class = "Bum"
    self.name = name
    self.stren = random.randint(6,10)
    self.luck = random.randint(6,10)
    self.dex = random.randint(6,10)
    self.con = random.randint(6,10)
    self.hp = (5 + self.con)
    #self.def = (self.stren + self.dex)

  
