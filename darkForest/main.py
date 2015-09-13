import os,sys
import pygame
import loader
import Player
import Room0
import Solid
import random
from pygame.locals import *

os.system('cls' if os.name=='nt' else 'clear')
if not pygame.font: print "Warning, fonts disabled"
if not pygame.mixer: print "Warning, sound disabled"

pygame.init()
scale=2
screen = pygame.display.set_mode((320*scale,240*scale))

player = Player.Player(scale)

clock=pygame.time.Clock()
clockspeed=60
timer=0

whichRoom=0
lastRoom=None

while True:
  clock.tick(clockspeed)
  timer+=1
  if timer>clockspeed: timer=0
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit(1)
    elif event.type == KEYDOWN:
      if event.key == K_ESCAPE or event.key == K_q:
        pygame.quit()
        sys.exit(1)
      if event.key == K_SPACE or event.key == K_UP:
        player.keyInput("jump","none")
      if event.key == K_RIGHT:
        player.keyInput("right","none")
      elif event.key == K_LEFT:
        player.keyInput("left","none")
    elif event.type == KEYUP:
      if event.key == K_RIGHT:
        player.keyInput("none","right")
      if event.key == K_LEFT:
        player.keyInput("none","left")

  if whichRoom==0:
    if lastRoom!=0:
      lastRoom=0
      room0 = Room0.Room0(player,screen,scale*16)
    else:
      room0.update(player,timer)
