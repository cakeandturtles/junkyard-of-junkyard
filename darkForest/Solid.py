import pygame
import loader
from pygame.locals import *

class Solid(pygame.sprite.Sprite):
  """Parent class for all solid objects """
  def __init__(self,x,y,scale):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(loader.load_image("redMonkey.png",-1),(scale,scale))
    self.rect = self.image.get_rect()
    self.rect.topleft = x,y

  def update(self):
    pass
