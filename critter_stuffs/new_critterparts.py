from critter_stuffs import critter_specials
import random


class critter_part():
  """a class for critter parts, creates critter part objects to be used by the critter class. Everything else in this doc is functions to create the critterpart_line list this class wants from parts.txt"""

  def __init__(self,critterpart_line):
    self.name = critterpart_line[0]
    self.atk = critterpart_line[1]
    self.hp = critterpart_line[2]
    self.defense = critterpart_line[3]
    self.luc = critterpart_line[4]
    self.dex = critterpart_line[5]
    self.spc = critterpart_line[6]
    self.special_attack = critterpart_line[7]

  def give_stats(self):
    return (self.name,self.atk,self.hp,self.defence,self.luc,self.dex,self.spc,self.special_attack)



special_dict = {"standard_special":critter_specials.standard_special,"sanguine_teeth":critter_specials.sanguine_teeth, "mega_horn":critter_specials.mega_horn,"rip_n_tear":critter_specials.mega_horn,"acid_rain":critter_specials.acid_rain,"basic_special":critter_specials.basic_special}



def specific_critterpart_ingest(part_name):
  """Takes a part name in caps and returns its entry from parts.txt"""
  parts_ingest = open("parts.txt")
  
  for line in parts_ingest:
    line_search = line
    line_name = line_search.split(',')[0]
    if line_name == part_name:
      parts_ingest.close()
      return line_search


  print('Part Not FOUND')
  parts_ingest.close()


def random_critterpart_ingest():
  """returns a random entry from parts.text"""
  parts_ingest = open("./critter_stuffs/parts.txt")
  line_list = parts_ingest.readlines()
  parts_ingest.close()

  line_num = random.randint(0,len(line_list) - 1)

  return line_list[line_num]

  
def make_part_list(part_string):
  """Cleans up the part list and makes it actually ingestable."""
  stat_list = part_string.split(',')
  final_list = []
  for x in stat_list:
    try:
      final_list.append(int(x))
    except:
      final_list.append(x)

  for key in critter_specials.critter_special_dict:
    if key + '\n' == final_list[-1]:
      final_list.remove(key + '\n')
      final_list.append(critter_specials.critter_special_dict[key])
    elif key == final_list[-1]:
      final_list.remove(key)
      final_list.append(critter_specials.critter_special_dict[key])

  return final_list
