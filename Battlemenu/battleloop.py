from critter_stuffs import critter
import os
from Battlemenu import battlemenu

def player_turn(targetCritter, currentPlayer):

  targetCritter.print_features()
  info = targetCritter.take_damage(currentPlayer.do_dmg(targetCritter))
  currentPlayer.reset_self()
  print("{0} took {1} damage".format(targetCritter.name, info))
  critter_dps = targetCritter.deal_damage()
  if not targetCritter.is_alive():
    print('{0} has died'.format(targetCritter.name))
    print('Critter gave {0} Experience Points'.format(targetCritter.give_exp()))
    currentPlayer.gainxp(targetCritter.give_exp())
    del critter1
    currentPlayer.update_stats()
    targetCritter = critter.Critter()
    targetCritter.update_stats()
    print("\nA new critter has appeared!\n")
    return #maybe everything else can go to hell
  print("{0} is winding up to deal {1}".format(targetCritter.name, critter_dps))
  playerinfo = currentPlayer.take_damage(critter_dps)
  print("{0} took {1} damage".format(currentPlayer.name, playerinfo))
  if not currentPlayer.is_alive():
    print("{0} has died".format(currentPlayer.name))
    return



def critter_turn(currentCritter, targetPlayer):
  currentCritter.print_features()
  critter_dps = currentCritter.deal_damage()
  info = targetPlayer.take_damage(currentCritter.do_dmg(targetPlayer))
  print("{0} is winding up to deal {1}".format(currentCritter.name, critter_dps))
  targetPlayer = targetPlayer.take_damage(critter_dps)
  print("{0} took {1} damage".format(targetPlayer.name, info))
  if not targetPlayer.is_alive():
    print("{0} has died".format(targetPlayer.name))
    print("{0} murdered {1} critters before dying!".format(targetPlayer.name))
    




def battleloop(player_character,creature):
  new_person = player_character
  critter1 = creature
  gamestate = True
  kill_count = 0
  player_status = 0
  critter_status = 0
  while gamestate:
    

    #battle menu
    myvar = (input("Type Exit to exit or type check stats orterwise type enter: ")).lower()
    os.system('clear')
    if myvar == "check stats":
      new_person.check_stats()
      critter1.check_stats()
      input(": ")
      os.system('clear')
      
    elif myvar == "exit":
      break
      gamestate = False

    elif myvar == "die critter":
      print("\n auto killing {0}....\n".format(critter1.name))
      del critter1
      critter1 = critter.Critter()
      critter1.update_stats()
      print("\n New critter generated\n")
      input(": ")
      continue
    #weapon1 = sword(weaponmat[myvar])
    #user_choice_class is the variable that gets passed to new_person object to define what class the player wants to play
    #new_person = person(weapon1, user_choice_class)
    
    #clears the screen for cleaner output
    new_person.update_stats()
    
    if player_character.aspeed >= critter1.dex:
      """do_player_turn(player_action)
      #turn this into a player turn function.
      if player_action == 'attack':
        player attack"""
      
      critter1.print_features()
      info = critter1.take_damage(new_person.do_dmg(critter1))
      new_person.reset_self()
      print("{0} took {1} damage".format(critter1.name, info))
      critter_dps = critter1.deal_damage()
      if not critter1.is_alive():
        print('{0} has died'.format(critter1.name))
        print('Critter gave {0} Experience Points'.format(critter1.give_exp()))
        new_person.gainxp(critter1.give_exp())
        del critter1
        player_character.update_stats()
        critter1 = critter.Critter()
        critter1.update_stats()
        print("\nA new critter has appeared!\n")
        kill_count = kill_count + 1
        critter_status == 'critter dead'
        break
        #return 'Player won'
      print("{0} is winding up to deal {1}".format(critter1.name, critter_dps))
      playerinfo = new_person.take_damage(critter_dps)
      print("{0} took {1} damage".format(new_person.name, playerinfo))
      if not new_person.is_alive():
        print("{0} has died".format(new_person.name))
        print("{0} murdered {1} critters before dying!".format(new_person.name, kill_count))
        player_status == 'player dead'
        break
        #return 'critter won'

    else:
      #turn me into a function that is critter turn
      critter_dps = critter1.deal_damage()
      print("{0} is winding up to deal {1}".format(critter1.name, critter_dps))
      playerinfo = new_person.take_damage(critter_dps)
      print("{0} took {1} damage".format(new_person.name, playerinfo))
      critter1.print_features()
      if not new_person.is_alive():
        print("{0} has died".format(new_person.name))
        print("{0} murdered {1} critters before dying!".format(new_person.name, kill_count))
        break
      info = critter1.take_damage(new_person.do_dmg(critter1))
      new_person.reset_self()
      print("{0} took {1} damage".format(critter1.name, info))
      if not critter1.is_alive():
        print('{0} has died'.format(critter1.name))
        print('Critter gave {0} Experience Points'.format(critter1.give_exp()))
        new_person.gainxp(critter1.give_exp())
        del critter1
        player_character.update_stats()
        critter1 = critter.Critter()
        critter1.update_stats()
        print("\nA new critter has appeared!\n")
        kill_count = kill_count + 1
        new_person.gainxp()
        continue

    """critter1.print_features()
    info = critter1.take_damage(new_person.do_dmg(critter1))
    new_person.reset_self()
    print("{0} took {1} damage".format(critter1.name, info))"""

 
    

    if not critter1.is_alive():
      print('{0} has died'.format(critter1.name))
      del critter1
      critter1 = critter.Critter()
      critter1.update_stats()
      print("\nA new critter has appeared!\n")
      kill_count = kill_count + 1
      continue
      #deletes the previous critter, makes a new one and then skips the rest of the loop
      

    """critter_dps = critter1.deal_damage()
    print("{0} is winding up to deal {1}".format(critter1.name, critter_dps))
    playerinfo = new_person.take_damage(critter_dps)
    print("{0} took {1} damage".format(new_person.name, playerinfo))"""

    if not new_person.is_alive():
      print("{0} has died".format(new_person.name))
      print("{0} murdered {1} critters before dying!".format(new_person.name, kill_count))
      break

    

  