import os,sys
import pygame
import loader
import playerCharacter
import catStatue
import redCat
import monkStatue
import orangeCloud
import random
from pygame.locals import *

os.system('cls' if os.name=='nt' else 'clear')
if not pygame.font: print "Warning, fonts disabled"
if not pygame.mixer: print "Warning, sound disabled"

pygame.display.set_caption("Meow")

pygame.init()
screen = pygame.display.set_mode((10*32,10*32))
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

screen.blit(background, (0,0))
pygame.display.flip()

player = playerCharacter.playerCharacter()
HkeyDirect = None
VkeyDirect = None

block1 = orangeCloud.orangeCloud(9,9)
block2 = orangeCloud.orangeCloud(0,9)
enemy = redCat.redCat(5,5)
monkstatue = monkStatue.monkStatue()
catstatue = catStatue.catStatue()

allenemies = pygame.sprite.RenderPlain((enemy))
allsolid = pygame.sprite.RenderPlain((block1,block2,catstatue,monkstatue))
clock=pygame.time.Clock()
clockspeed=60

print "Press return to pull up menu."
isMenu=False

while True:
  clock.tick(clockspeed)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit(1)
    elif event.type == KEYDOWN:
      if event.key == K_ESCAPE or event.key == K_q:
        if isMenu or event.key == K_ESCAPE:
          pygame.quit()
          sys.exit(1)
      if event.key == K_UP:
        VkeyDirect="up"
      elif event.key == K_DOWN:
        VkeyDirect="down"
      if event.key == K_LEFT:
        HkeyDirect="left"
      elif event.key == K_RIGHT:
        HkeyDirect="right"

      if event.key == K_SPACE:
        print "VKEY: ",VkeyDirect
        print "HKEY: ",HkeyDirect

      elif event.key == K_RETURN:
        if not isMenu:
          isMenu=True
          print "(E)quipment, S(t)ats, (S)ave, (Q)uit"
        else:
          isMenu=False
      elif event.key == K_e and isMenu:
        print "EQUIPMENT"
      elif event.key == K_t and isMenu:
        print "HP: ",player.rmStatlist[0]
        print "ATK: ",player.rmStatlist[1]
        print "DEF: ",player.rmStatlist[2]
        print "AGL: ",player.rmStatlist[3]
        print "MAG: ",player.rmStatlist[4]
    elif event.type == KEYUP:
      if event.key == K_UP and VkeyDirect == "up":
        VkeyDirect=None
      elif event.key == K_DOWN and VkeyDirect == "down":
        VkeyDirect=None
      if event.key == K_LEFT and HkeyDirect == "left":
        HkeyDirect=None
      elif event.key == K_RIGHT and HkeyDirect == "right":
        HkeyDirect=None

  player.update(HkeyDirect,VkeyDirect,(block1,block2,enemy,catstatue,monkstatue))
  allsolid.update()
  allenemies.update((block1,block2,catstatue,monkstatue,player))
  screen.blit(background, (0,0))
  pygame.sprite.RenderPlain(player).draw(screen)
  allsolid.draw(screen)
  allenemies.draw(screen)
  pygame.display.flip()
