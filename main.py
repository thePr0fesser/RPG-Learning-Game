from Character_creation import gamesetup
from Battlemenu import battleloop
from critter_stuffs import new_critterparts
from critter_stuffs import critter
from Player_stuffs import player
from Items import items
from GUI_Core import test_gui
from Player_stuffs import skill
from Battlemenu import battlemenu
from Player_stuffs import class_warrior
from Player_stuffs import class_gambler
from Player_stuffs import class_rogue

"""import battleloop
import new_critterparts
import critter
import player
import items
import test_gui
import skill
import battlemenu"""






print("Welcome to menu!")
user_input = input("Would you like to go to (1)Battletest,(2)Critter_Test or (3)Gui_Test: ")
print("------------------------------------------------------------------------\n\n\n\n")


if user_input == "1":
  #print('Critters are all away right now training. Please come back later')
  new_person,critter1 = gamesetup.gamesetup()
  battlemenu.battlemenu(new_person, critter1)
  #battleloop.battleloop(new_person, critter1)

elif user_input == "2":
  inventory = [items.sword(items.weaponmat["flametongue"])]
  inventory.append(items.armor(items.armormat["mail"]))
  new_person = player.warrior(inventory, 'Fabio')
  new_person.update_stats()

  critter1 = critter.Critter()
  critter1.update_stats()

  print("It's a fight against {0} and {1}".format(new_person.name, critter1.name))
  print("\nFabio attacks with {0}!!!!!".format(inventory[0]))
  print(new_person.statusEffects)
  outcome = new_person.imma_attack(critter1)
  print()
  print(outcome)
  print("\n That looked like a doozy!!!!")

  critter1.take_damage(outcome)
  print("\n{0} has the following status: {1}".format(critter1.name, critter1.statusEffects))

  print("\nTime to see if the dmg works!!!")
  print("{0}'s HP is:{1}".format(critter1.name, critter1.hp))
  print("\nAnd after the burn effect!")
  critter1.loop_update()
  print("{0}'s HP is:{1}".format(critter1.name, critter1.hp))
  input("Did it work?")


  
  
  

elif user_input == "3":
  print("\n Gui initializing, main menu starting\n")
  test_gui.go_gui()


elif user_input == "4":
  inventory = [items.sword(items.weaponmat["ironsword"])]
  inventory.append(items.armor(items.armormat["mail"]))
  new_person = player.warrior(inventory, 'Fabio')
  new_person.update_stats()
  critter1 = critter.Critter()
  critter1.update_stats()

  my_skill = skill.pommelstr()
  print(my_skill.activate(new_person, critter1))

elif user_input == "5":
  inventory = [items.sword(items.weaponmat["playingcard"])]
  inventory.append(items.armor(items.armormat["gamclothes"]))
  new_person = class_gambler.gambler(inventory, 'Jacob')
  new_person.update_stats()

  inventory = [items.sword(items.weaponmat["ironsword"])]
  inventory.append(items.armor(items.armormat["leather"]))
  new_person2 = class_rogue.rogue(inventory, 'Jacob')
  new_person2.update_stats()
    
  for x in range(0,10):
    #print(new_person2.statusEffects)
    currentdps = new_person.basic_atk(new_person2)
    #print(new_person2.take_damage())
    if currentdps != 0:
      new_person2.gethit(currentdps)
      if new_person2.gethit(currentdps):
        new_person2.take_damage(currentdps)
      else:
        pass
    else:
      print("miss")

  
   

#elif user_input == "6":
  #also if you just want to not have the logic in a code block run just toss a pass at the top like in elif user_input == 5.

  #you right, i was trying to do a test of run_away but got distracted
  #player_attack return (dmg, status)
  """class Player():
        status = [stunned, burned, poisoned, dumb, armored]
    class Critter():
        status = [stunned]
        
    
    
     class status_effect():
        __init__(self):
          self = True
          target = True
          on_attack = True
          on_def = True
          passive = True
        
        def effect(self)
        
        
        
        def player_attack():
          for x in self.status:
            if x.on_attack == True:
              
        """


      

      


  

  

else:
  print("Free will is an illusion")
  new_person,critter1 = gamesetup.gamesetup()
  battleloop.battleloop(new_person, critter1)









