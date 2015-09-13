import os,sys
import pygame
import random
import loader
from pygame.locals import *
os.system('cls' if os.name=='nt' else 'clear')
if not pygame.font: print "Warning, fonts disabled"
if not pygame.mixer: print "Warning, sound disabled"

pygame.init()
scale=1
screen = pygame.display.set_mode((320*scale,240*scale))

darkWorld = loader.load_image("palettes/dark.png",-1).convert()
lightWorld = loader.load_image("palettes/light.png",-1).convert()
image = darkWorld
area = ((39,99,99,99))

clock=pygame.time.Clock()
clockspeed=60
xx=0
yy=0

while True:
  clock.tick(clockspeed)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit(1)
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit(1)
  pos = pygame.mouse.get_pos()

  image = pygame.Surface((256,222))
  image.blit(darkWorld,(0,0))
  pygame.draw.circle(image,(111,111,111),pos,60)
  image.set_colorkey((111,111,111))
  screen.blit(lightWorld,(0,0))
  screen.blit(image,(0,0))
  
  pygame.display.flip()
