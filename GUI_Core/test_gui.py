"""import pygame

running = True
(width, height) = (600,600)
background_colour = (255,255,255)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

pygame.display.flip()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()"""


import pygame
from Character_creation import gamesetup
from Battlemenu import battleloop
from critter_stuffs import new_critterparts
from critter_stuffs import critter
from Player_stuffs import player
from Items import items


  
  
def go_gui():
  # initializing the constructor
  pygame.init()
    
  # screen resolution
  res = (300,300)
    
  # opens up a window
  screen = pygame.display.set_mode(res)
  pygame.display.set_caption('Critter World')
    
  # colors
  color = (255,255,255)
  color_light = (170,170,170)
  color_dark = (100,100,100)
  color_red = (255,0,0)
  color_blue = (0,0,255) 
    
  # stores the width of the
  # screen into a variable
  width = screen.get_width()
    
  # stores the height of the
  # screen into a variable
  height = screen.get_height()
    
  # defining a font
  smallfont = pygame.font.SysFont('Corbel',18)
    
  # rendering a text written in
  # this font
  critter_test_text = smallfont.render('Critter Test' , True , color)
  battle_test_text = smallfont.render("Battle Test", True, color)
  title1 = smallfont.render("Reese's Adventures", True, color)
  title2 = smallfont.render("in", True, color)
  title3 = smallfont.render("Critter World", True, color)

    
  while True:
        
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
      if ev.type == pygame.QUIT:
        pygame.quit()
                
    #checks if a mouse is clicked
    if ev.type == pygame.MOUSEBUTTONDOWN:
                
      #if the mouse is clicked on the
      # critter test
      if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        new_obj = player.warrior([],'Fabio')
        new_obj.check_stats()
        print(new_obj.inventory)
        new_obj.new_equip(items.sword(items.weaponmat["irondagger"]))
        print(new_obj.inventory)
        new_obj.update_stats()
        new_obj.check_stats()
      # battle_test
      elif 10 <= mouse[0] <= width/2 and height/2 <= mouse[1] <= height/2+40:
        new_person,critter1 = gamesetup.gamesetup()
        battleloop.battleloop(new_person, critter1)
  
  
                    
    # fills the screen with a color
    screen.fill((60,25,60))
        

        
    # if mouse is hovered on a button it
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
      pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
            
    else:
      pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])

    #option one button
    if 10 <= mouse[0] <= width/2 and height/2 <= mouse[1] <= height/2+40:
      pygame.draw.rect(screen,color_red,[width/width + 10,height/2,140,40])
            
    else:
      pygame.draw.rect(screen,color_blue,[width/width + 10,height/2,140,40])
        
    # text on buttons
    screen.blit(critter_test_text , (width/2+45,height/2 + 20))
    screen.blit(battle_test_text , (width/2-120,height/2 + 20))
    screen.blit(title1, (width/3 - 5, height/5))
    screen.blit(title2,(width/2-2, height/5 + 20))
    screen.blit(title3,(width/3+12,height/5 + 40))
        
    # updates the frames of the game
    pygame.display.update()

  return
