import os,sys
import pygame
import loader
import Player
import Solid
import random
from pygame.locals import *

class Room0():
  """Container class for the first room"""
  def __init__(self,player,screen,scale):
    pygame.display.set_caption("theforestisdark: Chapter 1")
    pygame.init()
    pygame.mouse.set_visible(0)
    self.screen = screen
    self.scale=scale

    self.background = pygame.Surface(self.screen.get_size())
    self.background = self.background.convert()
    self.background.fill((0,0,0))

    self.screen.blit(self.background, (0,0))
    pygame.display.flip()

    self.s0=Solid.Solid(0*self.scale,8*self.scale,scale)
    self.s1=Solid.Solid(1*self.scale,8*self.scale,scale)
    self.s2=Solid.Solid(2*self.scale,8*self.scale,scale)
    self.s3=Solid.Solid(3*self.scale,8*self.scale,scale)
    self.s4=Solid.Solid(3*self.scale,7*self.scale,scale)
    self.s5=Solid.Solid(3*self.scale,6*self.scale,scale)
    self.s6=Solid.Solid(4*self.scale,8*self.scale,scale)
    self.s7=Solid.Solid(5*self.scale,8*self.scale,scale)
    self.s8=Solid.Solid(6*self.scale,8*self.scale,scale)
    self.s9=Solid.Solid(7*self.scale,8*self.scale,scale)
    self.allSolids=[self.s0,self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9]
    self.allSolidSprites = pygame.sprite.RenderPlain(self.allSolids)

    player.PlaceMe(0,0)

  
  def update(self,player,timer):
    player.update(self.allSolids)
    self.allSolidSprites.update()
    self.screen.blit(self.background, (0,0))
    pygame.sprite.RenderPlain(player).draw(self.screen)
    self.allSolidSprites.draw(self.screen)
    pygame.display.flip()
