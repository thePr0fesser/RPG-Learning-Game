#special attack declarations

def sanguine_teeth(crit):
  number = crit.atk + crit.dex + crit.spc
  print("{0} attacks with blood dripped teeth, it's rage healing it for {1}".format(crit.name, number))
  crit.im_heal(number)
  return number
  

def mega_horn(crit):
  return crit.atk 

def rip_n_tear(crit):
  print("{0} begins to attack over and over getting stronger each time".format(crit.name))
  crit.counter += 1
  return crit.atk * 2 * crit.counter

def acid_rain(crit):
  #uses the critters counter to check to see if this move has been used before, don't increase defense again  
  
  if crit.counter == 0:
    print("{0} sprays acid into the sky and it rains down on the field increasing it's defense".format(crit.name))
    crit.defense = crit.defense * 1.1
    crit.counter += 1
    
    return crit.atk * 1.5
  else:
    print("{0} is still swimming in acid and is recieving healing".format(crit.name))
    crit.im_heal(crit.hp * 0.05)
    return crit.atk * 1.5

  

def standard_special(crit):
  return crit.atk 




names = ["Rico","Dashido","Fabio","Ryan","Danielle","Sarah","Sally"]

#list of all attack features
moves = ["Teeth", "Horns", "Claws", "Acid Spit","Pounce"]

#list of all appearnce features
features = ["Hooved Feet","Tail","Spots","Quills","Paws","Two Feets","Stripes","Whiskers","Anetnna","Bug Eyes","Wings","Pointy Ears"]

#dictionary of stat modifiers related to appearence with states in format (atk,hp,def,luc,dex,spc,special attack)
stats = {"Teeth":(2,0,0,0,0,2,sanguine_teeth),"Horns":(1,0,1,0,0,1,mega_horn),"Claws":(1,0,0,0,1,0,rip_n_tear),"Acid Spit":(1,0,0,1,0,4,acid_rain),"Hooved Feet":(0,0,0,0,2,0),"Tail":(0,2,0,1,1,0),"Spots":(0,3,1,0,0,0),"Quills":(0,2,2,0,0,0),"Paws":(1,0,0,0,1,0),"Two Feets":(2,0,1,0,0,0),"Stripes":(0,3,1,0,0,0),"Whiskers":(0,0,0,4,0,0),"Anetnna":(0,0,0,2,1,0),"Bug Eyes":(0,0,0,1,2,0),"Wings":(0,0,0,0,4,0),"Pointy Ears":(0,0,0,3,1,0), "Pounce":(2,0,0,0,0,2,standard_special)}