import os,sys
import pygame
import loader
from pygame.locals import *

class orangeCloud(pygame.sprite.Sprite):
  """Solid Block"""
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.OC = pygame.transform.scale(loader.load_image("orangeCloud.png",-1),(32,32))
    self.TS = pygame.transform.scale(loader.load_image("tealSpiral.png",-1),(32,32))
    self.PB = pygame.transform.scale(loader.load_image("purpleBlock.png",-1),(32,32))
    self.image=self.OC
    self.updateimage=0
    self.rect = self.image.get_rect()
    self.rect.topleft = x*32,y*32

  def update(self):
    if self.updateimage>0:
      self.updateimage+=1
    elif self.image == self.OC and self.updateimage==0:
      self.image = self.TS
      self.updateimage+=1
    elif self.image == self.TS and self.updateimage==0:
      self.image = self.PB
      self.updateimage+=1
    elif self.image == self.PB and self.updateimage==0:
      self.image = self. OC
      self.updateimage+=1
    if self.updateimage>=90:
      self.updateimage=0 
