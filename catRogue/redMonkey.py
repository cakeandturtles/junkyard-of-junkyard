import os,sys
import pygame
import loader
from pygame.locals import *

class redMonkey(pygame.sprite.Sprite):
  """Ook ook ook. MAG/AGL"""
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.rmf1 = pygame.transform.scale(loader.load_image("redmonkeyfront1.png",-1),(32,32))
    self.rmf2 = pygame.transform.scale(loader.load_image("redmonkeyfront2.png",-1),(32,32))
    self.rmb1 = pygame.transform.scale(loader.load_image("redmonkeyback1.png",-1),(32,32))
    self.rmb2 = pygame.transform.scale(loader.load_image("redmonkeyback2.png",-1),(32,32))
    self.rml1 = pygame.transform.scale(loader.load_image("redmonkeyleft1.png",-1),(32,32))
    self.rml2 = pygame.transform.scale(loader.load_image("redmonkeyleft2.png",-1),(32,32))
    self.rmr1 = pygame.transform.scale(loader.load_image("redmonkeyright1.png",-1),(32,32))
    self.rmr2 = pygame.transform.scale(loader.load_image("redmonkeyright2.png",-1),(32,32))
    self.image = self.rmf1
    self.rect = self.image.get_rect()
    self.rect.topleft = 0*32,0*32
    self.updateimage=0
    self.collision=0
    
    self.statlist=(10,1,1,5,5) #HP,ATK,DFC,AGL,MAG or... HADAM

  def keyMove(self,direction,target):
    if direction == "up" and self.rect.y>0*32:###########

      for i in target:
        if self.rect.move(0,-32).colliderect(i.rect):
          self.collision=1

      if self.collision!=1:
        self.rect.y-=32

      if not self.image == self.rmb1 or self.image == self.rmb2:
        self.image = self.rmb1

    elif direction =="down" and self.rect.y<32*9:##########
 
      for i in target:
        if self.rect.move(0,32).colliderect(i.rect):
          self.collision=1

      if self.collision!=1:
        self.rect.y+=32

      if not self.image == self.rmf1 or self.image == self.rmf2:
        self.image = self.rmf1

    elif direction == "left" and self.rect.x>0*32:##########
    
      for i in target:
        if self.rect.move(-32,0).colliderect(i.rect):
          self.collision=1

      if self.collision!=1:
        self.rect.x-=32

      if not self.image == self.rml1 or self.image == self.rml2:
        self.image = self.rml1

    elif direction == "right" and self.rect.x<9*32:###########
      
      for i in target:
        if self.rect.move(32,0).colliderect(i.rect):
          self.collision=1

      if self.collision!=1:
        self.rect.x+=32

      if not self.image == self.rmr1 or self.image == self.rmr2:
        self.image = self.rmr1

    self.collision=0


  def update(self):
    if self.updateimage>0:
      self.updateimage+=1
    elif self.image == self.rmf1 and self.updateimage==0:
      self.image = self.rmf2
      self.updateimage+=1
    elif self.image == self.rmf2 and self.updateimage==0:
      self.image = self.rmf1
      self.updateimage+=1
    elif self.image == self.rmb1 and self.updateimage==0:
      self.image = self.rmb2
      self.updateimage+=1
    elif self.image == self.rmb2 and self.updateimage==0:
      self.image = self.rmb1
      self.updateimage+=1
    elif self.image == self.rml1 and self.updateimage==0:
      self.image = self.rml2
      self.updateimage+=1
    elif self.image == self.rml2 and self.updateimage==0:
      self.image = self.rml1
      self.updateimage+=1
    elif self.image == self.rmr1 and self.updateimage==0:
      self.image = self.rmr2
      self.updateimage+=1
    elif self.image == self.rmr2 and self.updateimage==0:
      self.image = self.rmr1
      self.updateimage+=1
    if self.updateimage>=30:
      self.updateimage=0
