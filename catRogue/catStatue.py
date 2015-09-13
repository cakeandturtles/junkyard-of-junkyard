import os,sys
import pygame
import loader
from pygame.locals import *

class catStatue(pygame.sprite.Sprite):
  """Meow meow meow statue"""
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.bcsad = pygame.transform.scale(loader.load_image("bluecatstatuesad.png",-1),(32,32))
    self.bchap = pygame.transform.scale(loader.load_image("bluecatstatuehappy.png",-1),(32,32))
    self.image = self.bchap
    self.rect = self.image.get_rect()
    self.rect.topleft = 3*32,0*32
    self.updateimage=0

  def update(self):
    pass
