def basic_special(crit):
  """takes in the atk, special, and dex of the critter and returns it"""
  print("BOOOOOP!!!!!")
  return crit.atk

def sanguine_teeth(crit):
  number = crit.atk + crit.dex /2
  print("{0} attacks with blood dripped teeth, it's rage healing it for {1}".format(crit.name, number))
  crit.im_heal(number)
  return number
  

def mega_horn(crit):
  return crit.atk 

def rip_n_tear(crit):
  print("{0} begins to attack over and over getting stronger each time".format(crit.name))
  crit.counter += 1
  return crit.atk * crit.counter

def acid_rain(crit):
  #uses the critters counter to check to see if this move has been used before, don't increase defense again  
  
  if crit.counter == 0:
    print("{0} sprays acid into the sky and it rains down on the field increasing it's defense".format(crit.name))
    crit.defense = crit.defense * 1.5
    crit.counter += 1
    
    return crit.spc * 1.5
  else:
    print("{0} is still swimming in acid and is recieving healing".format(crit.name))
    crit.im_heal(crit.hp * 0.05)
    return crit.spc * 1.5

  

def standard_special(crit):
  return crit.spc


def counter_attack(crit):
  print("{0} is preparing to counter an attack!".format(crit.name))
  crit.is_retaliating = True
  return 0

critter_special_dict = {'sanguine_teeth':sanguine_teeth,'mega_horn':mega_horn,'rip_n_tear': rip_n_tear,'acid_rain':acid_rain,'standard_special':standard_special,'basic_special': basic_special,'counter_attack':counter_attack}