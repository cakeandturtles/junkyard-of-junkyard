import os,sys
import pygame
import loader
from pygame.locals import *

class monkStatue(pygame.sprite.Sprite):
  """Ook ook ook statue"""
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.rmsad = pygame.transform.scale(loader.load_image("redmonkstatuesad.png",-1),(32,32))
    self.rmhap = pygame.transform.scale(loader.load_image("redmonkstatuehappy.png",-1),(32,32))
    self.image = self.rmsad
    self.rect = self.image.get_rect()
    self.rect.topleft = 5*32,0*32
    self.updateimage=0

  def update(self):
    pass
