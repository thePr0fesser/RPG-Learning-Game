import random

"""Critter Class

The Critter class takes a name as a str, moves as a list of strings, feats as a list of strings, stats as a dictionary of tuples with the format described later, a mode as an int, and manual as a tuple described latter

Best if used in combination with critterparts.py or in manual mode. Otherwise you'll have to create your own list of critterparts

arguments in detail

name => Str
  sets the name of the Critter
  
moves => list
  a list of strings
  Should contain animal weapons like Teeth and Claws

feats => list
  a list of strings
  Should contain animal features like Wings and Tails

stats => dictionary
  this is a dictionary describing the stat bonuses conveyed by the previous parts. Every move and feat should have a corresponding stat in stats  

  the breakdown of the stat's tuples is (atk,hp,defense,luc,dex)


mode => int default is 0
  toggles between the previous requirements for making a critter or utilizing manual mode
  0 for random generator mode
  1 for manual part selection but stats from the stats dictionary
  anything else for manual everything

manual_parts => tuple (move, feat1, feat2)

  a tuple of the parts you want the critter to have, will still need to 
  pass the moves, feats list and the stats dictionary and the move and feats need to be spelled exactly how they are in the aforementioned lists and dictionary.
  


manual_stats
  used in mode > 2
  This allows a bypass of the randomly generated critter mechanics and for a direct creation of a critter. will still need to supply a name with a tuple detailing the rest of the stats

  tuple breakdown is (atk,hp,defense,luc,dex,spc)
  and that should be (int,int,int,int,int,int,int) respectively



Critter attributes:
  self.name--String-- should be the name of the critter
  self.move--String--the name of the Critters attack method(used in stat calculation if in random generator mode)
  self.feat1--Stiring--a characteristic of the critter(used in stat calculation if in random generator mode)
  self.feat2--String--a characteristic of the critter(used in stat calculation if in random generator mode)
  self.atk--int--how much damage the critter can do base
  self.hp--int--total health of critter
  self.defense--int-- the bigger the number the more incoming damage it can block
  self.luc--int--the bigger the number the higher the crit chance, also plays a small role in chance to hit
  self.dex--int--the bigger the number the higher the hit rate, also plays a small role in crit chance

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
  return crit.atk + crit.dex + crit.spc
  
class Critter:
  def __init__ (self, moves = ["Bubbles"],feats = ["Feet", "Fuzz"],stats = {"Bubbles":(0,50,0,0,0,5,basic_special),"Feet":(0,0,0,0,0,0),"Fuzz":(0,0,0,0,0,0)},names = ["Rico"],mode = 0,manual_parts = ("Bubbles","Feet","Fuzz"),manual_stats = (5,5,5,5,5,5), manual_special = basic_special, manual_level = 1):

    if mode == 0: 
      self.name = names[random.randint(0,len(names) - 1)] 
      # set up the Critter's first move and it's first feature 
      self.move = moves[random.randint(0,len(moves) - 1)]
      self.feat1 = feats[random.randint(0,len(feats) - 1)]

      

      #Create a temp variable, then keep generating feats until the second feat is the same as the first then set self.feat2 to it.
      temp_feat2 = feats[random.randint(0,len(feats) - 1)]
      while temp_feat2 == self.feat1:
        temp_feat2 = feats[random.randint(0,len(feats) - 1)]
      
      self.feat2 = temp_feat2

      #set up the stats + modifies from moves and feats
      self.atk = 5 + stats[self.move][0] + stats[self.feat1][0] + stats[self.feat2][0]
      self.hp = 5 + stats[self.move][1] + stats[self.feat1][1] + stats[self.feat2][1]
      self.defense = 5 + stats[self.move][2] + stats[self.feat1][2] + stats[self.feat2][2]
      self.luc = 5 + stats[self.move][3] + stats[self.feat1][3] + stats[self.feat2][3]
      self.dex = 5 + stats[self.move][4] + stats[self.feat1][4] + stats[self.feat2][4]
      self.spc = 5 + stats[self.move][5] + stats[self.feat1][5] + stats[self.feat2][5] 

      try:
        self.special_move = stats[self.move][6]
      except:
        self.special_move = 0

    
    elif mode == 1:
      # this is for manual parts but psuedorandom stats
      self.name = names[0]
      self.move = manual_parts[0]
      self.feat1 = manual_parts[1]
      self.feat2 = manual_parts[2]

      #set up the stats + modifies from moves and feats
      self.atk = 5 + stats[self.move][0] + stats[self.feat1][0] + stats[self.feat2][0]
      self.hp = 5 + stats[self.move][1] + stats[self.feat1][1] + stats[self.feat2][1]
      self.defense = 5 + stats[self.move][2] + stats[self.feat1][2] + stats[self.feat2][2]
      self.luc = 5 + stats[self.move][3] + stats[self.feat1][3] + stats[self.feat2][3]
      self.dex = 5 + stats[self.move][4] + stats[self.feat1][4] + stats[self.feat2][4]
      self.spc = 5 + stats[self.move][5] + stats[self.feat1][5] + stats[self.feat2][5]

      try:
        self.special_move = stats[self.move][6]
      except:
        self.special_move = 0
    
    else:
      #this is full manual mode everything must be declared 
      self.name = names[0]
      self.move = manual_parts[0]
      self.feat1 = manual_parts[1]
      self.feat2 = manual_parts[2]

      self.atk = manual_stats[0]
      self.hp = manual_stats[1]
      self.defense = manual_stats[2]
      self.luc = manual_stats[3]
      self.dex = manual_stats[4]
      self.spc = manual_stats[5]

      try:
        self.special_move = manual_special
      except:
        self.special_move = 0

    self.counter = 0
    self.atkboost = 0
    self.hpboost = 0
    self.defense_boost = 0
    self.luc_boost = 0
    self.dex_boost = 0
    self.spc_boost = 0
    self.is_burn = False
    self.is_poisoned = False
    self.is_chilled = False
    self.is_shocked = False
    

    





  def print_features(self):
    #just prints of the features
    print("\nMy Name is {0}!".format(self.name))
    print("I use {0} to attack. I have {1} and {2}\n".format(self.move,self.feat1,self.feat2))

  def check_stats(self):
    #just prints off his stats
    print("\n=========================================")
    print("Critter Attack is: " + str(self.atk))
    print("Critter HP is: " + str(self.hp))
    print("Critter Defense is: " + str(self.defense))
    print("Critter Luck is: " + str(self.luc))
    print("Critter Dexterity is: " + str(self.dex))
    print("========================================\n")

  def give_stats(self):
    """returns all teh stats as a tuple"""
    return (self.atk, self.hp, self.defense, self.luc, self.dex, self.spc, self.name)

  
  def take_damage(self,damage = 0):
    """Takes incoming damage as an int and returns damage dealt to hp as an int/ while also modifying self.hp """
    print("\n{0}'s hp is currently: {1}".format(self.name, self.hp))
    if damage <= 0:
      return 0

    dmg_taken = damage - (round(self.defense/1.5))
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
    if self.is_alive():
      dice_roll = random.randint(1,100)
      if dice_roll > (100//(self.spc * 0.2)) and not self.special_move == 0:
        return self.special_move(self)
      elif dice_roll + round(self.dex / 2) >= 100 - round(self.luc * 1.4):
        print("\n{0} attempts to slam you in a vulnerable location".format(self.name))
        return self.atk * 2
      
      elif dice_roll + round(self.luc / 5) <= round(100/ self.dex * 1.15) + 20:
        print("\n{0} misses the attack".format(self.name))
        return 0
      
      else:
        print("\n{0} lunges forward".format(self.name))
        return self.atk
    else:
      return 0
  
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


