from Items import item_attrs

#weaponmats organsied (speed, crit chance, crit multi, damage, hit rate, special affect)
weaponmat = {"irondagger":(2,5,2,3,50, item_attrs.still_nothing), "ironsword":(1,3,1.5,6,55, item_attrs.still_nothing), "playingcard":(3,15,3,1,50, item_attrs.still_nothing), "stick":(1,1,1,1,50, item_attrs.still_nothing), "steeldagger":(2,7,2.5,5,60, item_attrs.still_nothing), "steelsword":(1,4,2,8,65, item_attrs.still_nothing), "steelcard":(3,20,4,1,60, item_attrs.still_nothing), "flametongue":(1,4,2,6,65,item_attrs.flametounge), "cooksuten":(2,4,2,2,50, item_attrs.still_nothing)}
#armormat organised (def (get hit chance), dam reduction)
#want to make their armor their defense, if wearing leater add 1/3 of dex to defense 
armormat = {"leather":(3, 2, item_attrs.leatherarm_defup), "mail":(10, 3, item_attrs.chainmail_dexdown), "gamclothes":(2,1, item_attrs.leatherarm_defup), "cookapr":(1, 3, item_attrs.leatherarm_defup), "scale":(11, 4, item_attrs.still_nothing), "plate":(12, 6, item_attrs.still_nothing), "rags":(3, 2, item_attrs.still_nothing)}

def nothing_attribute():
  pass
  return


class item:
  def __init__(self):
    self.type = None


class sword(item):
  def __init__(self, temp_weapon_mat):
    super().__init__()
    self.aspeed = temp_weapon_mat[0]
    self.critch = temp_weapon_mat[1]
    self.critmultiplier = temp_weapon_mat[2]
    self.dam = temp_weapon_mat[3]
    self.hr = temp_weapon_mat[4]
    self.type = 'weapon'
    self.special_attr = temp_weapon_mat[5]




class armor(item):
  def __init__(self, temp_armormat):
    self.type = 'armor'
    self.defen = temp_armormat[0]
    self.dmgreduc = temp_armormat[1]
    try:
      self.special_attr = temp_armormat[-1]
      
    except:
      pass



"""Super things: 
class weapons:
  def __init__(self, s, cc, cm, d, hr)
  
class axe(weapons)
  def __init__(self, s, cc, cm, d, hr)
    super().__init__(s, cc, cm, d, hr)

class bow(weapons)
  def __init__()"""