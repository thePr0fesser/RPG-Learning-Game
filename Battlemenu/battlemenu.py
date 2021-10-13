from Player_stuffs import player
import random



def battlemenu(new_person, critter1):
  while True:
    print("1) Attack")
    print("2) Use Item")
    print("3) Use Trick")
    print("4) Run Away")
    menuselc = input(">")
    if menuselc == "1":
      new_person.do_dmg(critter1)
      if not new_person.is_alive():
        return False
    elif menuselc == "2":
      #itemmenu.itemmenu
      pass
    elif menuselc == "3":
      trickmenu.trickmenu = True
    elif menuselc == "4":
      def run_away():
        run_away_var = random.randint(1,100)
        if run_away_var >= 100 - (player.dex):
          print("You Coward!")
          return False
        else:
          print("You couldn't get away :(")
          

          
  return 0

def trickmenu():
 while True:
   print(special_ability[0])