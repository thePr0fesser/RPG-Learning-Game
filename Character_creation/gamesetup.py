from critter_stuffs import critter
from Player_stuffs import player
from Player_stuffs import class_warrior
from Items import items



def gamesetup():
  #class selector
  temp_name = input("Please enter your name: ")
  print("1)Gambler")
  print("2)Rogue")
  print("3)Warrior")
  print("4)Cook")
  user_choice_class = (input("Please give class: ")) 
  if user_choice_class == "1":
    print("As a gambler, you start with playing cards and leather armor!")
    inventory = [items.sword(items.weaponmat["playingcard"])]
    inventory.append(items.armor(items.armormat["gamclothes"]))
    new_person = player.gambler(inventory, temp_name)
    new_person.update_stats()
  elif user_choice_class == "2":
    print("As a Rogue, you start with an iron dagger and leather armor!")
    inventory = [items.sword(items.weaponmat["irondagger"])]
    inventory.append(items.armor(items.armormat["leather"]))
    new_person = player.rogue(inventory, temp_name)
    new_person.update_stats()
  elif user_choice_class == "3":
    print("As a warrior, you start with an iron sword and chain mail!")
    inventory = [items.sword(items.weaponmat["ironsword"])]
    inventory.append(items.armor(items.armormat["mail"]))
    new_person = player.warrior(inventory, temp_name)
    new_person.update_stats()
  elif user_choice_class == "4":
    print("As a cook, you start with cook's utensils and a cook's apron!")
    inventory = [items.sword(items.weaponmat["cooksuten"])]
    inventory.append(items.armor(items.armormat["cookapr"]))
    new_person = player.cook(inventory, temp_name)
    new_person.update_stats()
  else:
    print("If you won't dance to that tune, I got others. Code Yellow!")
    print("You are a bum, armed with only a Stick")
    inventory = [items.sword(items.weaponmat["stick"])]
    new_person = player.warrior(inventory, temp_name)
    new_person.update_stats()

  critter1 = critter.Critter()
  critter1.update_stats()

  return new_person,critter1



def create_party(num_members = 3):
  party = []
  for x in range(0,num_members):
    party.append(gamesetup())
  
  return party
  
